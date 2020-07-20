### What

This folder contains a data from [*impresso*](https://impresso-project.ch/) for the PH tutorial on text reuse. Data consists of 1 year-worth of contents from the following Swiss newspapers (in French):

- *L'Express* (`EXP`)
- *Gazette de Lausanne* (`GDL`)
- *Journal de Genève* (`JDG`)
- *L'Impartial* (`IMP`)

Content of this folder:

- `data`: 
  - impresso sample data, already transformed into a *passim*-friendly JSON format;
  - format: bz2-compressed JSON line documents (each `.bz2` corresponds to one newspaper/year )
- `schema`: JSON schemas for the impresso sample data;
- `passim-output`: output obtained when running files in `data/`through *passim*

### License

Data are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a> 

### Reference

When referring to  [*impresso*](https://impresso-project.ch/)'s data please use the following reference:

```
@inproceedings{ehrmann-etal-2020-language,
    title = "Language Resources for Historical Newspapers: the Impresso Collection",
    author = {Ehrmann, Maud  and
      Romanello, Matteo  and
      Clematide, Simon  and
      Str{\"o}bel, Phillip Benjamin  and
      Barman, Rapha{\"e}l},
    booktitle = "Proceedings of The 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://www.aclweb.org/anthology/2020.lrec-1.121",
    pages = "958--968",
    language = "English",
    ISBN = "979-10-95546-34-4",
}
```

