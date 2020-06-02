import os
from bs4 import BeautifulSoup as bs
import sys
import re
from tqdm import tqdm
import multiprocessing
from multiprocessing import Pool
import random
NUM_CORES = multiprocessing.cpu_count()


data_in = os.path.join("..","data","sgml")
data_out = os.path.join("..","data","txt")
data_ref = os.path.join("..","ref")

if os.path.exists(data_out) == False:
	os.mkdir(data_out)

def SGML_to_TXT(path_in):
	''' Will take the path to an SGML file as input and write the text in a TXT file'''
	path_out = path_in.replace(data_in,data_out).replace(".sgm",".txt")
	

	if os.path.exists(path_out) == True:
		return None
	
	with open(path_in) as f:
		sgml = f.read()
		
	soup = bs(sgml,"lxml-xml")

	with open(path_out,"w") as f:
		tag = soup.find("TEXT")
		f.write(tag.get_text())


def TXT_to_passimJSON(path_in,final_json):
	'''Will take the path to a TXT file as input
	as well as the path to an outfile,
	will write the content in correct PASSIM json format'''

	if os.path.exists(final_json) == True:
		f = open(final_json,"a")
	else:
		f = open(final_json,"w")

	#print(path_in)
	with open(path_in) as f_in:
		id_ = os.path.basename(path_in).replace(".txt","")
		series = "not_bible"
		text = " ".join(f_in.read().replace("\n"," ").replace('"',"'").split())
		json = '{"id": "'+id_+'", "series": "'+series+'", "text": "'+text+'"}\n' #  yolo
		f.write(json)

	f.close()



if __name__ == "__main__":

	files = []
	for file in os.listdir(data_in):
		files.append(os.path.join(data_in,file))

	print("Transforming SGML to TXT")
	with Pool(NUM_CORES-1) as pool:
		r = list(tqdm(pool.imap(SGML_to_TXT, files), total=len(files)))

	## I do it in two times because lazy
	## multiprocessing would fail with writing to the same file i think
	files = [] 
	for file in os.listdir(data_out):
		files.append(os.path.join(data_out,file)) # adding to list so i can tqdm

	if len(sys.argv) > 1:
		limit_files_in_json = sys.argv[1]
		try:
			int(limit_files_in_json)
		except ValueError:
			sys.exit("sys.argv[1] must be an int, you put",sys.argv[1])
	
	else:
		limit_files_in_json = len(files)
	
		
	try:
		os.remove("passim_in.json")
	except FileNotFoundError:
		z = 0

	random.shuffle(files)  # in case we want a smaller subset this ensure we don't always pick the first x
	print("Formatting TXT into passim format")


	for file in tqdm(files[:int(limit_files_in_json)]):
		TXT_to_passimJSON(file,"passim_in.json")

	with open(os.path.join(data_ref,"king_james.txt")) as f:
		text = " ".join(f.read().replace("\n"," ").split())
		id_ = "king_james"
		series = "bible"
		json = '{"id": "'+id_+'", "series": "'+series+'", "text": "'+text+'"}\n'
		with open("passim_in.json","a") as f_out:
			f_out.write(json)
	print("Passim input file written to disk.")
