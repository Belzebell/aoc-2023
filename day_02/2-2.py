# read file and initialise variables
file = open('input.txt', 'r')
result = 0

# loop through input, for every line get list of digits using regex,
# then concat the first and last, cast to int and add to the result
for line in file:
    line = line.strip()
    game_id, rounds = line.split(': ', 1)  # split by colon to get game ID part and round part
    game_id = game_id.split(' ', 1)[1]  # split "Game X" by  space and get second half to have actual ID
    max_counts = {'blue': 0, 'red': 0, 'green': 0}  # initialise all as 0 for rounds where one colour doesn't appear at all
    for game_round in rounds.split('; '):
        for dice in game_round.split(', '):
            count, colour = dice.split(' ')
            if int(count) > max_counts[colour]:  # we still want to find MAX, as that is the MIN the bag has to have
                max_counts[colour] = int(count)

    # increase result by multiplication of the dict
    result += (max_counts['blue'] * max_counts['red'] * max_counts['green'])

file.close()  # we are done reading the file

print("The sum of possible Game IDs is", result)