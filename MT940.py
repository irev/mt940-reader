import os
import re
import sys
import locale
import hashlib

# Set locale to the user's default setting (e.g., 'en_US.UTF-8')
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
from colorama import Fore
from tabulate import tabulate
# from termcolor import colored

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
    if target.find('C') and target.find('C') != -1:
      code ='C'
      pos = target.find('C')
      if pos != -1:
          # print(f"C  : {target.find('CR')}")
          # Ambil substring sebelum 'CR'
          substring = target[:pos]
          # Ambil hanya angka dari substring
          numbers = ''.join(filter(str.isdigit, substring))
          return numbers+code
    # Mencari posisi 'D' pertama
    elif target.find('D') and target.find('D') != -1:
      code ='D'
      pos = target.find('D')
      if pos != -1:
          # print(f"Debit : {target.find('DR')}")
          # Ambil substring sebelum 'DR'
          substring = target[:pos]
          # Ambil hanya angka dari substring
          numbers = ''.join(filter(str.isdigit, substring))
          return numbers+code   
    return '0'

def extract_number_after_first_code(target):
    match = re.search(r'(?<=DR|CR)\d+|(?<=D|C)\d+', target)
    if match:
        nominal = match.group()
        print(Fore.RED + "Nominal: " + match.group() + Fore.RESET)
        print(nominal)  # Output: 129187217
        return nominal
    else:
        print("Nominal tidak ditemukan.")       
        return 0

# fungsi untuk mengambil nominal kredit return C+nominal
def get_nominal_credit(target):
    match = re.search(r'(?<=C)\d+|(?<=CR)\d+', target)
    if match:
        nominal = match.group()
        print(Fore.RED + "Nominal: " + match.group() + Fore.RESET)
        print(nominal)  # Output: 129187217
        return "C"+nominal
    else:
        print("Nominal tidak ditemukan.")       
        return 0

# fungsi untuk mengambil nominal debit retun D+nominal       
def get_nominal_debit(target):
    match = re.search(r'(?<=C)\d+|(?<=DR)\d+', target)
    if match:
        nominal = match.group()
        print(Fore.RED + "Nominal: " + match.group() + Fore.RESET)
        print(nominal)  # Output: 129187217
        return "D"+nominal
    else:
        print("Nominal tidak ditemukan.")       
        return 0 

def extrak_statement(string):
    type_match = re.search(r'\d{6}C|\d{6}D', string)
    nominal_match = re.search(r'(?<=C)\d+|(?<=CR)\d+|(?<=D)\d+|(?<=DR)\d+', string)
    if type_match and nominal_match:
        if type_match.group()[-1] == 'C':
            # transaction_type = "credit" 
            transaction_type = type_match.group()[-1] 
        elif type_match.group()[-1] == 'D':
            # transaction_type = "debit"
            transaction_type = type_match.group()[-1]
        else:
            transaction_type = "unknown"
        nominal = nominal_match.group()
        # return f"{type_match.group()} {transaction_type} {nominal}"
        return f"{transaction_type}{nominal}"
    else:
        return "unknown"

def parse_mt940_files(directory):
    # print(Fore.RED + 'This text is red in color')
    if directory != None :
        statements = []
        statements_c = []
        statements_d = []
        transactions = {'case_in': 0, 'case_out': 0 , 'statement' : statements}
        # Loop melalui semua file di direktori yang ditentukan
        for filename in os.listdir(directory):
            # if filename.endswith('.txt'):  # Sesuaikan ekstensi jika perlu
            if filename != None :  # Sesuaikan ekstensi jika perlu
                print(Fore.MAGENTA + filename + Fore.RESET) 
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
                    print(Fore.YELLOW + f"Statement: {(lines)}" + Fore.RESET)
                    if len(lines) > 0:
                        statement_string = lines[0].strip()
                        print(f" amount_line: {statement_string}")
                        # Ambil jumlah, dengan asumsi format seperti "1234,56CR" atau "5678,90DR"
                        # date_credit_debit = extract_number_before_first_code(amount_line[:-1])
                        # amount_credit_debit = extract_number_after_first_code(statement_string[:-1])
                        amount_credit_debit  = extrak_statement(statement_string)
                        transactions['statements'] = ['dsdsd',extrak_statement(statement_string)]
                        print(Fore.GREEN + amount_credit_debit + Fore.RESET)
                        # print(Fore.RED + amount_credit_debit[1:] + Fore.RESET)
                        if amount_credit_debit[:1] == 'C':  # Kredit
                            amount = float(amount_credit_debit[1:])
                            statements.append([statement_string,'C',locale.currency(amount, symbol=False,grouping=True)])
                            statements_c.append([statement_string,'C',locale.currency(amount, symbol=False,grouping=True)])
                            print(Fore.GREEN + f"CREDIT: {amount}")
                            # print( f"amount_credit_debit: {amount_credit_debit}" + Fore.RESET)
                            # amount = float(extract_number_after_first_code(amount_credit_debit[:-1]))
                            # print(f"amount: {lo}")
                            transactions['case_in'] += amount
                            #print(f"amount: {amount}")
                        elif amount_credit_debit[:1] == 'D':  # Debit
                            amount = float(amount_credit_debit[1:].replace(',', '.'))
                            statements.append([statement_string,'D',locale.currency(amount, symbol=False,grouping=True)])
                            statements_d.append([statement_string,'D',locale.currency(amount, symbol=False,grouping=True)])
                            print(Fore.RED + f"DEBIT:  {amount}")
                            # print(f"{amount_credit_debit}" + Fore.RESET)
                            # amount = float(extract_number_after_first_code(amount_credit_debit[:-1]))
                            # print(f"amount: {lo}")
                            transactions['case_out'] += amount
                        #print(f"amount_line: {amount_line[:-1]}")
                    transactions['statements'] = statements
                    transactions['statements_c'] = statements_c
                    transactions['statements_d'] = statements_d
    return transactions

# Contoh penggunaan
if sys.argv[1]:
  print(sys.argv[1])
  if os.path.isdir(sys.argv[1]):
    directory_path = sys.argv[1] #'D:/MT940/MT940/INJOURNEY/BMRI/Agustus/'  # Ganti dengan direktori Anda
  else:
    print(f"Does {sys.argv[1]} exist or a directory?")  
    sys.exit()
else:
  directory_path = 'D:/MT940/MT940/INJOURNEY/BMRI/Agustus/'

# extract_number_after_first_code("240924CR9999NTRF")
# extract_number_after_first_code("240924D12345NTRF")
# extract_number_after_first_code("240924DR89898NTRF")
result = parse_mt940_files(directory_path)
print(f"\033[1;35m Total Case In (Credit):\033[1;33m {result['case_in']}, \033[1;35m Total Case Out (Debit):\033[1;33m {result['case_out']}"+Fore.RESET)
print(Fore.RESET)
# print(result['statements'])
print("\n"+ tabulate(result['statements'], 
        colalign=("right", "center", "right"),
        headers=['Name', 'Code', 'Amount'], 
        tablefmt='orgtbl'))
print("\nCREDIT:\n"+ tabulate(result['statements_c'], 
        colalign=("right", "center", "right"),
        headers=['Name', 'Code', 'Amount'], 
        tablefmt='orgtbl'))
print(f"\033[1;35m Total Case In (Credit):\033[1;33m {result['case_in']}"+Fore.RESET)

print("\nDEBIT:\n"+ tabulate(result['statements_d'], 
        colalign=("right", "center", "right"),
        headers=['Name', 'Code', 'Amount'], 
        tablefmt='orgtbl'))
print(f"\033[1;35m Total Case Out (Debit):\033[1;33m {result['case_out']}"+Fore.RESET)

print(f"\033[1;35m Total Case In (Credit):\033[1;33m {locale.currency(result['case_in'], symbol=False,grouping=True)}  \033[1;35m Total Case Out (Debit):\033[1;33m {locale.currency(result['case_out'], symbol=False,grouping=True)}"+Fore.RESET)
# targets = "240924CR373698NTRF"
# results = extract_number_before_first_code(targets)
# print(f"Angka sebelum 'C' pertama: {results}")
# sys.argv[1]


# transaction_type = extrak_statement("240924CR9999NTRF")
# print(transaction_type)  # Output: credit 168868
# transaction_type = extrak_statement(':61:240831CR12345678NINT')
# print(transaction_type)  # Output: credit 168868