import random
import string

lowercase_alphabets = string.ascii_lowercase
uppercase_alphabets = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

def generate_password(length, mix_case_flag, numbers_flag, special_characters_flag):
    password_string = ''
    if mix_case_flag:
        password_string += lowercase_alphabets + uppercase_alphabets
    else:
        password_string += lowercase_alphabets
        
    if numbers_flag:
        password_string += numbers
    if special_characters_flag:
        password_string += special_characters
    
    matches_criteria = False
    while not matches_criteria:
        temp_password = ''
        for i in range(length):
            temp_password += random.choice(password_string)
        
        # Check if the password contains characters from the required sets
        if (mix_case_flag and any(char.islower() for char in temp_password) and any(char.isupper() for char in temp_password)) or not mix_case_flag:
            if numbers_flag and any(char.isdigit() for char in temp_password) or not numbers_flag:
                if special_characters_flag and any(char in special_characters for char in temp_password) or not special_characters_flag:
                    matches_criteria = True
                    
    print(f'length: {length}, mix_case_flag: {mix_case_flag}, numbers_flag: {numbers_flag}, special_characters_flag: {special_characters_flag}')
    
    print(f'your generated password is: {temp_password}')

length = input('enter password length: ')

while not length.isdigit():
    print(' please enter a valid number')
    length = input('enter password length: ')

length_int = int(length)
    
mix_case_input = input('mix case? (y for yes)')

if mix_case_input == 'y':
    mix_case_flag = True
else: 
    mix_case_flag = False
    
numbers_input = input('Do you want numbers in your password? (y for yes)')
if numbers_input == 'y':
    numbers_flag = True
else: 
    numbers_flag = False
    
    
special_characters_input = input('Do you want special characters in your password? (y for yes)')
if special_characters_input == 'y':
    special_characters_flag = True
else: 
    special_characters_flag = False

generate_password(length_int, mix_case_flag, numbers_flag, special_characters_flag)
