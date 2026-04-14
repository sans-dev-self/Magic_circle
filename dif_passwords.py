import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."


chars = ""

amount_pass = int(input("Количество паролей "))
lengt_pass = int(input("Длина пароля "))
include_num = input("Вкл цифры? (y/n)")
include_upper_let = input("Вкл прописные буквы? (y/n)")
include_lower_let = input("Вкл строчные буквы? (y/n)")
include_symbols = input("Вкл символы? (y/n)")
exclude_same_symbols = input("Исключать ли неоднозначные символы? (y/n)")

#привет


if include_num == "y".lower():
    chars += digits
if include_upper_let == "y".lower():
    chars += uppercase_letters
if include_lower_let == "y".lower():
    chars +=lowercase_letters
if include_symbols == "y".lower():
    chars += punctuation
if exclude_same_symbols == "н".lower():
    for c in "il1Lo0O":
        chars = chars.replace(c,"")

def generate(lentgh,chars):
    password = ""
    for i in range(lentgh):
        password += random.choice(chars)
    return password

for _ in range(amount_pass):
    print(generate(lengt_pass,chars))
print()
        
