import os
import re
import string
from tqdm import tqdm

import pdfplumber
from pdfplumber.page import Page
from pypdf import PdfWriter, PdfReader, PageObject


def sanitize_filename(filename: str):
    valid_chars = "-_.()#& %s%s" % (string.ascii_letters, string.digits)
    # Replace '/' with '-'
    sanitized = filename.replace('/', '-')
    sanitized = ''.join(c for c in sanitized if c in valid_chars)
    return sanitized

def extract_account_name(text):
    account_name_pattern = r"Name: ([\w\s,\-\.#/&]+)\s+e-Postmark:"
    match = re.search(account_name_pattern, text)
    return sanitize_filename(match.group(1).strip()) if match else None

def write_to_pdf(start: int, end: int, pages: list[Page], reader_pages: list[PageObject], output_directory):
    writer = PdfWriter()
    try:
        account_name = None
        for i in range(start, end):
            page = pages[i]
            if i == start:
                account_name = extract_account_name(page.extract_text())
            writer.add_page(reader_pages[i])

        if account_name:
            output_filename = f"{account_name.upper()}.pdf"
            output_path = os.path.join(output_directory, output_filename)

            # Check if the file already exists and rename accordingly
            counter = 1
            while os.path.exists(output_path):
                output_filename = f"{account_name.upper()}-{counter}.pdf"
                output_path = os.path.join(output_directory, output_filename)
                counter += 1

            with open(output_path, "wb") as output_pdf:
                writer.write(output_pdf)
    except Exception as e:
        print(e.with_traceback())
    finally:
        writer.close()

def split_pdf(input_pdf_path, output_directory):
    report_start_pattern = r"Product:.*Category:.*IRS Center:"
    reader = PdfReader(input_pdf_path)

    try:
        with pdfplumber.open(input_pdf_path) as pdf:
            pages = pdf.pages
            start_indexes = []
            for i, page in enumerate(pages):
                text = page.extract_text()
                if re.search(report_start_pattern, text):
                    start_indexes.append(i)

            for i in tqdm(range(len(start_indexes))):
                start = start_indexes[i]
                end = start_indexes[i + 1] if i + 1 < len(start_indexes) else len(pages)
                write_to_pdf(start, end, pdf.pages, reader.pages, output_directory)
                
    except Exception as e:
        print(e.with_traceback())
    finally:
        reader.stream.close()
