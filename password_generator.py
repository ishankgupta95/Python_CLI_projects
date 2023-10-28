import random
import string

lowercase_alphabets = string.ascii_lowercase
uppercase_alphabets = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

def generate_password(length, mix_case_flag, numbers_flag, special_characters_flag):
    password_string = lowercase_alphabets
    if mix_case_flag:
        password_string += uppercase_alphabets
    if numbers_flag:
        password_string += numbers
    if special_characters_flag:
        password_string += special_characters
    
    temp_password = ''.join(random.choice(password_string) for _ in range(length))
    return temp_password

def get_password_length():
    while True:
        length = input('Enter password length: ')
        if length.isdigit():
            return int(length)
        print('Please enter a valid number.')

def get_user_choice(message):
    return input(message).lower() == 'y'

def main():
    length = get_password_length()
    mix_case_flag = get_user_choice('Mix case? (y for yes): ')
    numbers_flag = get_user_choice('Do you want numbers in your password? (y for yes): ')
    special_characters_flag = get_user_choice('Do you want special characters in your password? (y for yes): ')
    
    password = generate_password(length, mix_case_flag, numbers_flag, special_characters_flag)
    print(f'Your generated password is: {password}')

if __name__ == "__main__":
    main()
