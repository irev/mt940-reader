import re
from colorama import Fore

def get_nominal_debit(string):
    match = re.search(r'(?<=C)\d+|(?<=DR)\d+', string)
    if match:
        nominal = match.group()
        print(Fore.RED + "Nominal: " + match.group() + Fore.RESET)
        print(nominal)  # Output: 129187217
        return "D" + nominal
    else:
        print("Nominal tidak ditemukan.")
        return 0

def extrak_statement(string):
    type_match = re.search(r'\d{6}C|\d{6}D', string)
    nominal_match = re.search(r'(?<=C)\d+|(?<=CR)\d+|(?<=D)\d+|(?<=DR)\d+', string)
    
    if type_match and nominal_match:
        if type_match.group()[-1] == 'C':
            transaction_type = "credit"  
        elif type_match.group()[-1] == 'D':
            transaction_type = "debit"
        else:
            transaction_type = "unknown"
        nominal = nominal_match.group()
        return f"{type_match.group()} {transaction_type} {nominal}"
    else:
        return "unknown"

# Example usage
transaction_type = extrak_statement(':61:240831CR12345678NINT')
print(transaction_type)  # Output: credit 168868
transaction_type = extrak_statement(':61:240831C234334445NDINT')
print(transaction_type)  # Output: credit 168868
transaction_type = extrak_statement(':61:240831DR345645NINT')
print(transaction_type)  # Output: debit 168868
transaction_type = extrak_statement(':61:240831D456756756NINT')
print(transaction_type)  # Output: debit 168868