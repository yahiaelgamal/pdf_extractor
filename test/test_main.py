import sys, os

# Get the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Add the project root to the sys.pats
# sys.path.append(os.path.join("/Users/yahiaelgamal/pdf_extractor/", "src"))
sys.path.append("/Users/yahiaelgamal/pdf_extractor/")

from src.main import extract_keywords_and_paragraphs_from_pdf


# TODO make this reproducible
directory_path = "/Users/yahiaelgamal/pdf_extractor/pdf_docs/"
file_path = "/Users/yahiaelgamal/pdf_extractor/pdf_docs/CFM general/1978.pdf"

matches = extract_keywords_and_paragraphs_from_pdf(
    file_path, ["women", "refugee"], directory_path
)
assert len(matches) == 1
print(matches)
