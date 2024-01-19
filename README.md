# Acceptance Letter Splitter

The purpose of this project is to split bulk printed Acceptance Letters from a single PDF into individual PDF files for each acceptance letter where the PDF name is the account name in all caps. In ProSystems eFiling System, bulk printing acceptance letters produces a single PDF file of all individuals acceptance letters. Each individual acceptance letter must be separated and saved as its own PDF file using the account name as the filename.

This script runs in the command line and does not have a user interface. At most, it will prompt the user to enter a path to the pdf or path to an output directory. However, if the user sets these as environmental variables or uses the '.env' file, then no interaction from the user is required.

## Contents

* [Setup](#Setup)
* [Usage](#Usage)
* [Features](#Features)
* [Technologies](#Technologies)
* [Contributors](#Contributors)
* [License](#License)

## Setup

This assumes you have python 3.10.6+ installed, a copy of this repository, and, optionally, an active virtual environment like venv. A virtual environment is not required but is highly recommended.

1. install dependancies.

```console
pip install -r requirements.txt
```

2. OPTIONAL - Set path to PDF and path to output directory as environment variable by using the below commands

```
set PDF_SPLITTER_PATH=path/to/pdf_file.pdf
set PDF_OUTPUT_DIRECTORY=output/
```

or, by setting the values in a .env file

```env
PDF_SPLITTER_PATH=path/to/pdf_file.pdf
PDF_OUTPUT_DIRECTORY=output/
```

By default, PDF_OUTPUT_DIRECTORY will be set to the 'output/' directory within the project root directory.

## Usage

Once setup is complete, follow the below instructions.

1. Change directory to root project directory

```console
cd path/to/AcceptanceLetters
```

2. Run main.py

```console
python main.py
```

3. When prompted, input your PDF to be split path. If you set this path as an environemnt variable, skip this step. Currently supports the following special characters: '#', '&', '/', '-', '_', '(', ')', and '.' in account names.

```console
Please enter the path to the PDF file: path/to/pdf_file.pdf
```

4. OPTIONAL - When prompted, input a suffix to be added to the end of each filename.

```console
Enter a suffix to add to the end of each filename. Leave blank and press enter to skip.
Suffix: -asdf
```

5. OPTIONAL - input your PDF output directory path. If you set this path as an environemnt variable, skip this step

```console
Please enter the path to the output PDF directory: path/to/output/
```

## Features

Can accept user input to split bulk printed Acceptance Letters as a single PDF into individual PDF files for each acceptance letter while providing a progres bar for user feedback.

### User Input

The path to the PDF file and path to the PDF output directory can be specified as environment variables or in a '.env' file. If they are not, the user will be prompted to enter them in the console. No matter what, the path to the pdf file will be validated as a file that exists and ends with extension '.pdf', and the output directory path will be validated as a directory that exists.

### PDF Splitting

Single PDF containing multiple individual reports will be split into multiple PDFs each with a single individual report. The PDF is split using a combination of PyPDF to create the individual PDFs and pdfplumber to parse and extract text from the PDF (findng the start of individual reports and getting account name).

### Progress Bar

Uses a progress bar for tqdm to provide user feedback for progress on splitting single PDF into multiple PDFs. The progress bar is displayed in the console and measures the progress of the number of individual reports that have been separated to PDF over the total number of individual reports combined in the single PDF.

## Technologies

Below is the list of technologies used in this project.

* dotenv to load environment variables from '.env' file
* os for path manipulation
* pdfplumber to parse and extract text from the PDF
* pypdf to create new PDF files
* re for regex pattern matching
* string for valid ascii letters and digits
* tqdm for progress bar

## Contributors

* Neil Crum

## License

MIT License

Copyright 2023 Neil Crum

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
