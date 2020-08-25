# README

This repository contains the sample data for the [Programming Historian](https://programminghistorian.org/)'s lesson *Detecting Text Reuse with Passim*, written by [Matteo Romanello](https://github.com/mromanello) and [Simon Hengchen](http://github.com/faustusdotbe) (currently in [preparation](https://github.com/programminghistorian/ph-submissions/issues/294)).

Data come from two different sources (see respective READMEs for license statements and further details):

1. books from EEBO (Early English Books Online) → [more info](eebo/README.md)
2. newspaper articles from [*impresso*](https://impresso-project.ch/) → [more info](impresso/README.md)  

The Jupyter notebook [`explore-passim-output.ipynb`](./explore-passim-output.ipynb) contains an example of how to load `passim`'s JSON output into a `pandas` `DataFrame` to compute some statistics.

To run the notebook as well as the scripts contained in [`eebo/code/*.py`] make sure that you install the required dependencies into a new virtual environment (created by using `conda`, `pyenv`, `venv`, etc.):

```bash
pip install -r requirements.txt
```
