import sys, os

# Get the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Add the project root to the sys.pats
# sys.path.append(os.path.join("/Users/yahiaelgamal/pdf_extractor/", "src"))
sys.path.append("/Users/yahiaelgamal/pdf_extractor/")

from src.main import extract_keywords_and_paragraphs_from_pdf


directory_path = "/Users/yahiaelgamal/pdf_extractor/pdf_docs/"
file_path = "/Users/yahiaelgamal/pdf_extractor/pdf_docs/CFM general/1978.pdf"
# file_path = "/Users/yahiaelgamal/pdf_extractor/pdf_docs/Humanitarian resolutions/Humanitarian Pakistan 2023 March.pdf"

ss = extract_keywords_and_paragraphs_from_pdf(file_path, ["women", "refugee"])
assert len(ss) == 2
print(ss)
