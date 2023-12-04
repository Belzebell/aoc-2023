# read file and initialise variables
file = open('input.txt', 'r')
result = 0
card_count = {}

# loop through input, split into winning numbers and scratch numbers
# then find the intersection and use that to calculate score
for line in file:
    line = line.strip()
    winning_nrs, scratch_nrs = line.split(' | ')  # split the string in the middle

    # we want double space to be single space (single digit case), and split by space
    # also split winning number part into card number and the winning numbers
    card_nr = int(winning_nrs.replace('Card ', '').split(':')[0].strip())
    winning_nrs = winning_nrs.replace('  ', ' ').split(' ')[2:]
    scratch_nrs = scratch_nrs.replace('  ', ' ').split(' ')

    # count the current card into the total card count
    if card_nr in card_count:
        card_count[card_nr] = card_count[card_nr] + 1 #
    else:
        card_count[card_nr] = 1 # if this is the first card, only count winnings once

    # find out how many more cards this card wins
    winning_count = len([nr for nr in scratch_nrs if nr in winning_nrs])

    # if this card won any cards, increase the next card counts
    if winning_count > 0:
        times_counted = 0
        while times_counted < card_count[card_nr]:  # if we have more than one card, this needs to be run multiple times
            won_card_nr = card_nr
            while not won_card_nr - card_nr == winning_count:  # run as many times as this card won
                won_card_nr = won_card_nr + 1

                # count the won card into the total card count
                if won_card_nr in card_count:
                    card_count[won_card_nr] = card_count[won_card_nr] + 1
                else:
                    card_count[won_card_nr] = 1

            times_counted = times_counted + 1

file.close()  # we are done reading the file

# get the sum of all scratchcards
result = sum(card_count.values())

print("The elf ended up with a scratchcard total of", result)