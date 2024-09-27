import os
import re
import sys
import hashlib

regex = r"^[0-9(D|C)].*"

def hash_file_md(path):
    if path != None :
        # BUF_SIZE is totally arbitrary, change for your app!
        BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
        md5 = hashlib.md5()
        with open(path, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                # sha1.update(data)
    print("MD5: {0}".format(md5.hexdigest()))        
        
def extract_number_before_first_code(target):
    # Mencari posisi 'C' pertama
    if target.find('CR') and target.find('CR') != -1:
      code ='C'
      pos = target.find('CR')
      if pos != -1:
          # print(f"C  : {target.find('CR')}")
          # Ambil substring sebelum 'CR'
          substring = target[:pos]
          # Ambil hanya angka dari substring
          numbers = ''.join(filter(str.isdigit, substring))
          return numbers+code
    # Mencari posisi 'D' pertama
    elif target.find('DR') and target.find('DR') != -1:
      code ='D'
      pos = target.find('DR')
      if pos != -1:
          # print(f"Debit : {target.find('DR')}")
          # Ambil substring sebelum 'DR'
          substring = target[:pos]
          # Ambil hanya angka dari substring
          numbers = ''.join(filter(str.isdigit, substring))
          return numbers+code
    return '0'

def parse_mt940_files(directory):
    if directory != None :
        transactions = {'case_in': 0, 'case_out': 0}
        # Loop melalui semua file di direktori yang ditentukan
        for filename in os.listdir(directory):
            # if filename.endswith('.txt'):  # Sesuaikan ekstensi jika perlu
            if filename != None :  # Sesuaikan ekstensi jika perlu
                print(filename)
                
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(content)
                    print(file.name)
                    hash_file_md(file.name)
                # Pisahkan konten menjadi entri transaksi
                for entry in content.split(':61:')[1:]:
                    lines = entry.splitlines()
                    # print(f"entry: {lines}")
                    print(f"entry: {(lines)}")
                    if len(lines) > 0:
                        amount_line = lines[0].strip()
                        #print(f"amount_line: {amount_line}")
                        # Ambil jumlah, dengan asumsi format seperti "1234,56CR" atau "5678,90DR"
                        amount_credit_debit = extract_number_before_first_code(amount_line[:-1])
                        print(amount_credit_debit)
                        if amount_credit_debit[-1] == 'C':  # Kredit
                            amount = float(amount_credit_debit[:-1])
                            lo = extract_number_before_first_code(amount_credit_debit[:-1])
                            #print(f"amount: {lo}")
                            transactions['case_in'] += amount
                            #print(f"amount: {amount}")
                        elif amount_credit_debit[-1] == 'D':  # Debit
                            amount = float(amount_credit_debit[:-1].replace(',', '.'))
                            lo = extract_number_before_first_code(amount_credit_debit[:-1])
                            #print(f"amount: {lo}")
                            transactions['case_out'] += amount
                        #print(f"amount_line: {amount_line[:-1]}")
    return transactions

# Contoh penggunaan
directory_path = 'D:/MT940/BANKK/'  # Ganti dengan direktori Anda
result = parse_mt940_files(directory_path)
print(f"Total Case In: {result['case_in']}, Total Case Out: {result['case_out']}")

# targets = "240924CR373698NTRF"
# results = extract_number_before_first_code(targets)
# print(f"Angka sebelum 'C' pertama: {results}")
# sys.argv[1]
