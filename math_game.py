import random
import time

number_of_question = 5
question_number = 0
min_value = 2
max_value = 10
operators = ['+', '-', '*']
wrong = 0


input('Press any key to start')
print('-------------------------')
start_time = time.time()

while question_number < number_of_question:
    digit_one = random.randint(min_value, max_value)
    digit_two = random.randint(min_value, max_value)
    operator = random.choice(operators)
    expression = f'{digit_one} {operator} {digit_two}'
    user_answer = input(f'{expression} = ')
    evaluated_answer = str(eval(expression))

    while user_answer != evaluated_answer:
        print('wrong')
        wrong += 1
        user_answer = input(f'{expression} = ')
    
    question_number += 1
    
    
end_time = time.time()
total_time = round((end_time - start_time), 2)
print(f'your took {total_time} seconds and answered incorret {wrong} times')
        
    
        
        
            
    