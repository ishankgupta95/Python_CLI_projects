import random

min_number = 1
max_number = 10
guessed_number = None
guesses = 0

number_to_guess = random.randint(min_number, max_number)
    
while True:
    guessed_number = input(f'Enter a number between {min_number} and {max_number} to guess: ')

    # Check if the input is a valid number
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
        
        # Check if the guessed number is within the valid range
        if min_number <= guessed_number <= max_number:
            guesses += 1

            if guessed_number > number_to_guess:
                print('Too high')
            elif guessed_number < number_to_guess:
                print('Too low')
            else:
                # Guessed correctly, break out of the loop
                print(f'Congratulations! You guessed the number {number_to_guess} in {guesses} {"guess" if guesses == 1 else "guesses"}.')
                break
        else:
            print(f'Please enter a number between {min_number} and {max_number}.')
    else:
        print('Invalid input. Please enter a valid number.')