import os
import re
import sys
import hashlib
import re


# regEx
# :61:240826DR176120660NTRF//0207150143062089
# :61: 240826 DR 176120660 NTRF // 0207150143062089
# Cari :61:
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# https://regex101.com/r/PnF6C5/1
# regex = r":61:(\d+)(\D{1,2})(\d+|\d+,\d{1,2})([A-Z]{4})(.{0,})"
regex = r"(\d+)(\D{1,2})(\d+|\d+,\d{1,2})([A-Z]{4})(.{0,})"
def parse_mt940_files(directory):
    # os.system('clear')  
    if directory != None :
        transactions = {'case_in': 0, 'case_out': 0}
        # Loop melalui semua file di direktori yang ditentukan
        for filename in os.listdir(directory):
            # if filename.endswith('.txt'):  # Sesuaikan ekstensi jika perlu
            if filename != None :  # Sesuaikan ekstensi jika perlu
                # print(filename) #tampil file Name
                file_path = os.path.join(directory, filename) 
                with open(file_path, 'r') as file:
                    content = file.read()
                    # print(content)
                    # print(file.name)
                    # hash_file_md(file.name)
                for entry in content.split(':61:')[1:]:  # regex = r"(\d+)(\D{1,2})(\d+|\d+,\d{1,2})([A-Z]{4})(.{0,})"
                    lines = entry.splitlines()
                    # print(lines[0])
                    # print(f"entry: {(lines)}") 
                    matches = re.search(regex, lines[0])
                    if matches:    
                        print(f"matches :61: tgl:{matches[1]} status:{matches[2]} amount:{matches[3]} code:{matches[4]} file:{file.name}")
                        amount = float(matches[3].replace(',', '.'))
                        if matches[2] == 'C' or matches[2] == 'CR':   # CREDIT
                            transactions['case_in'] += amount
                        elif matches[2] == 'D' or matches[2] == 'DR':  # DEBIT
                            transactions['case_out'] += amount

    return transactions

# print(len(sys.argv))
if len(sys.argv)>=2:
  if os.path.isdir(sys.argv[1]):
    directory_path = sys.argv[1] #'D:/MT940/MT940/INJOURNEY/BMRI/Agustus/'  # Ganti dengan direktori Anda
  else:
    print(f"Does {sys.argv[1]} exist or a file?")  
    sys.exit()
else:
  print(f"The directory has not yet stipulated, please select the destination directory. \nexp: python .\mt940.py /path/")  
  directory_path = '.\data'
#   sys.exit()
# print(directory_path)
result = parse_mt940_files(directory_path)
print(f"\n============================================================================")
print(f"\nTotal Case In: {result['case_in']} |  Total Case Out: {result['case_out']}\n")
print(f"============================================================================")


# sys.exit()
