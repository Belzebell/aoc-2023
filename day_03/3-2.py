import copy

# read file and initialise variables
file = open('input.txt', 'r')
result = 0
ratio_result = 0
schematic_map = []
gear_ratio_map = {}

# We solve both parts of day 3 in part 2

# loop through input and build the full schematic map before we can iterate through
for line in file:
    line = line.strip()
    schematic_row = list(line)  # cast the line to an array
    schematic_map.append(schematic_row)

file.close()  # we are done reading the file

# iterate through the map, if we find a symbol adjacent to a number, we need to "complete" the number,
# add it to the result, and continue from behind the number
for i, row in enumerate(schematic_map):
    next_j = 0
    for j, location in enumerate(row):
        if next_j > j:
            continue  # if next_j is greater, means we already grabbed this number due to adjacency of an earlier digit
        if location.isdigit():
            adjacent_map = {}  # build a map of the (up to) 9 symbols around the number (incl number itself)
            for x_i in range(i-1,i+2):  # because of Part 2, the adjacent map needs to be a dict instead of a list
                if x_i < 0 or x_i > len(schematic_map)-1:
                    continue
                for x_j in range(j-1, j+2):
                    if x_j < 0 or x_j > len(schematic_map[x_i])-1:
                        continue
                    adjacent_map[str(x_i) + '_' + str(x_j)] = schematic_map[x_i][x_j]

            symbol_found = False
            for item_id in adjacent_map:
                item = adjacent_map[item_id]
                if not item == '.' and not item.isdigit():  # if we find any item that is NOT a . or number, we have a match!
                    symbol_found = True
                    number = ''
                    next_digit = prev_digit = location
                    next_j = copy.copy(j)
                    prev_j = copy.copy(j)
                    while next_digit.isdigit():  # find all digits behind as they belong to the number
                        number += next_digit  # we are starting with the number itself
                        next_j += 1
                        if(next_j > len(row)-1):
                            break
                        next_digit = row[next_j]

                    while prev_digit.isdigit():  # find all digits before as they belong to the number
                        prev_j -= 1
                        if(prev_j < 0):
                            break
                        prev_digit = row[prev_j]
                        # it can happen that we find a not-digit, in that case don't append,
                        # the while loop won't continue anyway
                        if prev_digit.isdigit():
                            number = prev_digit + number

                    # now that we have the final number, set our j iterator to the end of the number
                    j = next_j
                    result += int(number)
                    break  # stop looking through the adjacent map

            # THIS IS THE SOLUTION FOR PART 2
            if symbol_found:  # if we found a symbol, let's look thoroughly for every star as this number belongs to that gear ratio
                for item_id in adjacent_map:
                    if adjacent_map[item_id] == '*':
                        # thanks to our adjacent_map now being a dict, we know the location of the star
                        if item_id not in gear_ratio_map:  # if key doesn't exist, initialise
                            gear_ratio_map[item_id] = []
                        gear_ratio_map[item_id].append(number)  # map the number to the star location

# loop through gear ratio map, if a * has exactly 2 numbers, multiply and add to the result
for ratio_loc in gear_ratio_map:
    gear_ratio = gear_ratio_map[ratio_loc]
    if len(gear_ratio) == 2:
        ratio_result += int(gear_ratio[0]) * int(gear_ratio[1])

print(gear_ratio_map)

print("The sum of all part numbers in the schematic is", result)
print("The sum of all gear ratios in the schematic is", ratio_result)