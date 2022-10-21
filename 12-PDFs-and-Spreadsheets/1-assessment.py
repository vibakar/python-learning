# PDFs and Spreadsheets Puzzle Exercise
# Let's test your skills, the files needed for this puzzle exercise

# You will need to work with two files for this exercise and solve the following tasks:

# Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
# Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can't download from Google Drive) and find the phone number that is in the document. Note: There are different ways of formatting a phone number!


# Task One: Grab the Google Drive Link from .csv File

import csv
import re
import PyPDF2

data = open("find_the_link.csv", mode="r", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

google_drive_link = ""

for index,line in enumerate(data_lines):
    google_drive_link += line[index]

data.close()

print(f"Google drive link from csv file: {google_drive_link}")


# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.
print("\n#####################\n")
f = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
phone_num_pattern = r"\d{3}.\d{3}.\d{4}"

for page in range(0, pdf_reader.numPages):
    # print(f"Searching in page {page}")
    page_data = pdf_reader.getPage(page)
    text = page_data.extractText()
    phone_num = re.search(phone_num_pattern, text)
    if phone_num :
        print(f"Phone number found: {phone_num.group()}")

f.close()