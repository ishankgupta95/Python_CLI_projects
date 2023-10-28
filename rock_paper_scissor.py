import random

rock_paper_scissor = ['rock', 'paper', 'scissor']

computer_choice = random.choice(rock_paper_scissor)

player_choice = input('please choose rock, paper or scissor: ').lower()

while player_choice not in rock_paper_scissor:
    player_choice = input('invalid option, please choose rock, paper or scissor: ').lower()
    
if (player_choice == 'rock' and computer_choice == 'scissor') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissor' and computer_choice == 'paper'):
    print('you won')
    
elif (player_choice == computer_choice):
    print('its a tie')
    
else:
    print('computer won')

print(f'computer chose {computer_choice} and you chose {player_choice}')