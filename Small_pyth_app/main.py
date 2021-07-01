
import random
import string

pass_lenght=int(input("Enter the length of password (8+):"))
while True:
    if pass_lenght<8:
        pass_lenght = int(input("Enter the length of password (8+):"))
    else:
        break;

letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase
digits = string.digits
punctations =  string.punctuation


chars=letters_lowercase+letters_uppercase+digits+punctations

password = random.choices(chars, k=pass_lenght)

password = "".join(password)

pass_data_special_= ""

print(pass_lenght)
print(password)
#print(punctations)
