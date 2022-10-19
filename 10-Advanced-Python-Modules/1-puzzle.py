import os
import shutil
import re

current_working_dir = os.getcwd()
zip_file_name = "unzip_me_for_instructions.zip"
search_dir = f"{current_working_dir}/extracted_content"

def unarchive():
    file_to_unzip = f"{current_working_dir}/{zip_file_name}"
    shutil.unpack_archive(file_to_unzip, current_working_dir)

def serach_for_ph_no():
    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    phone_numbers = []

    for folder, sub_folders, files in os.walk(search_dir):
        for file in files:
            file_path = f"{folder}/{file}"
            with open(file_path, "r") as f:
                content = f.readline()
                ph_no = re.search(phone_pattern, content)
                if ph_no:
                    # print(f"{folder}/{file}")
                    phone_numbers.append(ph_no.group())

    print("".join(phone_numbers))

if __name__ == "__main__":
    unarchive()
    serach_for_ph_no()