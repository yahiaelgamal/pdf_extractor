import os
import PyPDF2
import re
from tqdm import tqdm
from typing import List
import pandas as pd


# Directory path to search for PDF files
# TODO make this relative
# DIRECTORY_PATH = "/Users/yahiaelgamal/pdf_extractor/pdf_docs_small/"
DIRECTORY_PATH = "/Users/yahiaelgamal/pdf_extractor/pdf_docs/"

# List of keywords to search for in PDF files
keywords = [
    "woman",
    "women",
    "displace",
    "refugee",
    "migrant",
    "protection",
    "inclusion",
]


def from_text_to_paragraphs(text: str) -> List[str]:
    yield from text.split("\n \n")


# Function to extract keywords and paragraphs from a PDF file
def extract_keywords_and_paragraphs_from_pdf(pdf_file_path, keywords):
    # Open the PDF file and extract text
    pdf_file = open(pdf_file_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    results = []

    # for page_num, page in tqdm(enumerate(range(len(pdf_reader.pages)))):
    for page_num, page in enumerate(range(len(pdf_reader.pages))):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        paragraphs = from_text_to_paragraphs(page_text)

        # Use regular expression to find paragraphs containing the keyword
        file_rel_path = os.path.relpath(pdf_file_path, DIRECTORY_PATH)
        kw_paragraph_matches = [
            (keyword, file_rel_path, page_num, paragraph.replace("\n", ""))
            for paragraph in paragraphs
            for keyword in keywords
            if re.compile(f".*{keyword}.*", re.IGNORECASE).findall(paragraph)
        ]
        results.extend(kw_paragraph_matches)

    pdf_file.close()

    return results


# Function to search for PDF files and save file paths with extracted keywords and paragraphs
def save_pdf_files_with_keywords_and_paragraphs(directory_path, keywords):
    pdf_files_with_keywords = []

    for root, dirs, files in os.walk(directory_path):
        print("current root is")
        print(root)
        # for file in tqdm(files, desc="Files", disable=True):
        for file in files:
            print(f"** file is {file}")
            if file.lower().endswith(".pdf"):
                pdf_file_path = os.path.join(root, file)
                results = extract_keywords_and_paragraphs_from_pdf(
                    pdf_file_path, keywords
                )

                if results:
                    pdf_files_with_keywords.extend(results)

    return pdf_files_with_keywords


if __name__ == "__main__":
    # Run the script
    pdf_files_with_keywords_and_paragraphs = (
        save_pdf_files_with_keywords_and_paragraphs(DIRECTORY_PATH, keywords)
    )
    df = pd.DataFrame(
        pdf_files_with_keywords_and_paragraphs,
        columns=["keword", "document", "page", "paragraph"],
    )
    output_file_path = f"keywords_output.csv"
    df.to_csv(output_file_path)

    print(f"Results saved to {output_file_path}")
