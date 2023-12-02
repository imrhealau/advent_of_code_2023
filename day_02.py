from helper import get_day
import re

data = get_day(2)

def colour_dict(red_num, green_num, blue_num):
    return {'red': red_num, 'green': green_num, 'blue': blue_num}

game_colour_dict = colour_dict(12,13,14)

# data = ['Game 1: 4 blue, 7 red, 5 green; 3 blue, 4 red, 16 green; 3 red, 11 green']

sum_1 = 0
sum_2 = 0
for line in data:
    is_valid = True
    game, sets = line.split(': ')
    game = game[5:]
    max_dict = colour_dict(0,0,0)

    for round in sets.split("; "):
        for item in round.split(", "):
            num, colour = item.split(' ')
            max_dict[colour] = max(int(num), max_dict[colour])

    for key, val in game_colour_dict.items():
        if max_dict[key] > val:
            is_valid = False
    if is_valid:
        sum_1 += int(game)

    sum_2 += max_dict['red'] * max_dict['green'] * max_dict['blue']
    

print(sum_2)

        




    


