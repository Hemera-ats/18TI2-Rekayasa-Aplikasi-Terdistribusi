import sys
import string
import time

user_input = sys.stdin

numbers = string.digits
characters = string.ascii_letters
symbol = string.punctuation

all_letter = 0
all_number = 0
unique_char = 0

for line in user_input:
    for char in line :
        if (char in numbers):
            all_number +=1
        elif (char in characters) :
            all_letter +=1
        elif (char in symbol):
            unique_char +=1

print ('------------------------------------------------------')
print ('Jumlah number                     : ', all_number)
print ('Jumlah char                       : ', all_letter)
print ('Jumlah simbol                     : ', unique_char)
print ('------------------------------------------------------')