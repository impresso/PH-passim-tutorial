### What

This is the accompanying code for the ProgrammingHistorian lesson on passim. This specific folder contains code and data for the Bible exercise.


- Python code to transform EEBO-TCP and Bible is in `code`
- Data is in `data`:
	- `sgml` contains the original EEBO TCP files in SGML
	- `txt` contains the textual content of the SGML files 
-`ref` contains the King James Bible from Project Gutenberg
- The already-prepared input file for passim is in this directory: `passim_in.json`. Due to size restrictions on Github's side, it is limited to 200 books picked randomly. A full compressed version is available as `passim_in.json.gz`.

### How-to

If you're only interested in trying out passim, simply use `passim_in.json`. If you want to play around with the code: 

- `python3 main.py` will transform SGML files into TXT if needed, and then create a `passim_in.json` file with all the books. 
- `python3 main.py INTEGER` (where `INTEGER` is an integer) will do as above, but will limit the number of books in the final `json` to whatever integer you specify.

### References

Data from EEBO-TCP:
- EEBO-TCP. 2003-2019. Early English Books Online. eebo.chadwyck.com & https://www.textcreationpartnership.org/

Data from Gutenberg:
- http://www.gutenberg.org/ebooks/10


