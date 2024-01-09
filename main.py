import os

from dotenv import load_dotenv

from splitter import split_pdf


def is_valid_pdf_file(file_path: str):
    return os.path.isfile(file_path) and file_path.lower().endswith('.pdf')

def is_valid_directory(directory_path):
    return os.path.isdir(directory_path)

def get_pdf_path():    
    # Get the path from an environment variable
    env_var_name = 'PDF_SPLITTER_PATH'
    path_from_env = os.getenv(env_var_name)

    if path_from_env and is_valid_pdf_file(path_from_env):
        return path_from_env

    # If not found or invalid, prompt the user
    while True:
        path_from_input = input("Please enter the path to the PDF file: ")
        if is_valid_pdf_file(path_from_input):
            return path_from_input
        else:
            print("Invalid file path or the file is not a PDF. Please try again.")

def get_output_pdf_directory():
    # Get the directory from an environment variable
    env_var_name = 'PDF_OUTPUT_DIRECTORY'
    directory_from_env = os.getenv(env_var_name)

    if directory_from_env and is_valid_directory(directory_from_env):
        return directory_from_env

    # If not found or invalid, prompt the user
    while True:
        directory_from_input = input("Please enter the path to the output PDF directory: ")
        if is_valid_directory(directory_from_input):
            return directory_from_input
        else:
            print("Invalid directory path. Please try again.")

def main():
    load_dotenv()
    pdf_path = get_pdf_path()
    output_directory = get_output_pdf_directory()
    split_pdf(pdf_path, output_directory)

if __name__ == "__main__":
    main()
