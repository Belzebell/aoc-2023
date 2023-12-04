# read file and initialise variables
file = open('input.txt', 'r')
result = 0

# loop through input, split into winning numbers and scratch numbers
# then find the intersection and use that to calculate score
for line in file:
    line = line.strip()
    winning_nrs, scratch_nrs = line.split(' | ')  # split the string in the middle

    # we want double space to be single space (single digit case), and split by space
    # for winning numbers, slice and ignore the first two items as they are "Card" and the Card Number
    winning_nrs = winning_nrs.replace('  ', ' ').split(' ')[2:]
    scratch_nrs = scratch_nrs.replace('  ', ' ').split(' ')

    # list every scratch number that is also in the winning number list
    winning_count = len([nr for nr in scratch_nrs if nr in winning_nrs])

    # calculate score, either just 1, or 2 to the power of matches - 1
    if winning_count == 1:
        result = result + 1
    elif winning_count > 1:
        result = result + (2**(winning_count-1))


file.close()  # we are done reading the file

print("The scratchcards are worth a total of", result)