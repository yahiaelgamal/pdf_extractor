# How to run
## Setup
```bash
pyenv virtualenv create pdf_extractor # not sure if this works
pyenv activate pdf_extractor
pip install -r requirements.txt
```
## Run
An example is in the makefile. Help docs is
```
usage: main.py [-h] input_dir output_file keywords [keywords ...]

This script will scrape the PDF

positional arguments:
  input_dir    Input dir, will be recursively explored
  output_file  The CSV output file
  keywords     List of keywords to match

options:
  -h, --help   show this help message and exit
```


The command should loo like:
`python src/main.py PDF_DIR CSV_OUTPUT word1 word2 word3 word4 ...`

For example:

`
	python src/main.py pdf_docs output_file.csv women women displace refugee migrant protection inclusion
`


# TODO:
1. Experiment with containerized with docker