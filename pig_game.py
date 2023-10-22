
"""TODO: 
BUG 1: Game restarts even when all player's turns are over and it does not declare a winner
BUG 2: The game should stop the moment the last player has crossed the max_score
BUG 3: Game does not stop when any player score more than max_score
"""  

import random

def roll():
    min_value = 1
    max_value = 6
    
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input('enter number of player (2-4): ')
    
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 and 4')
    else:
        print('invalid, try again')
        
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print(f'\n player {player_idx + 1 }\'s turn just started \n')
        print(f'your total score is {player_scores[player_idx]}\n')
        current_score = 0
        
        while True:
            should_roll = input('would you like to roll (y)?')
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            
            if value == 1:
                print(f'you rolled a 1! turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'you rolled {value}')
                
            print(f'your score is {current_score}')
            
        player_scores[player_idx] += current_score
        print(f'your total score is {player_scores[player_idx]}')
        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print(f'player {winning_idx + 1} wins with score of {max_score}')
    
    
    
