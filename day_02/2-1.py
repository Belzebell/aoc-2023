# read file and initialise variables
file = open('input.txt', 'r')
result = 0
allowed_values = {'red': 12, 'green': 13, 'blue': 14}

# loop through input, for every line get list of digits using regex,
# then concat the first and last, cast to int and add to the result
for line in file:
    line = line.strip()
    possible = True  # assume the game is possible until proven it is not
    game_id, rounds = line.split(': ', 1)  # split by colon to get game ID part and round part
    game_id = game_id.split(' ', 1)[1]  # split "Game X" by  space and get second half to have actual ID
    max_counts = {'blue': 0, 'red': 0, 'green': 0}  # initialise all as 0 for rounds where one colour doesn't appear at all
    for game_round in rounds.split('; '):
        for dice in game_round.split(', '):
            count, colour = dice.split(' ')  # split dice into colour and count
            if int(count) > max_counts[colour]:
                max_counts[colour] = int(count)  # if this is the biggest count of the colour, set it

    # loop through max and compare against allowed, if any max is bigger, this game is not possible
    for colour, count in max_counts.items():
        if count > allowed_values[colour]:
            possible = False
            break

    # add game ID to the result if the game is possible
    if possible:
        result += int(game_id)


file.close()  # we are done reading the file

print("The sum of possible Game IDs is", result)