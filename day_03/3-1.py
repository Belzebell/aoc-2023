import copy

# read file and initialise variables
file = open('input.txt', 'r')
result = 0
schematic_map = []

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
            adjacent_map = []  # build a map of the (up to) 9 symbols around the number (incl number itself)
            for adjacent_row in schematic_map[max(i-1, 0):min(i+2,len(schematic_map))]:
                adjacent_map += adjacent_row[max(j-1, 0):min(j+2,len(adjacent_row))]

            for item in adjacent_map:
                if not item == '.' and not item.isdigit():  # if we find any item that is NOT a . or number, we have a match!
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

print("The sum of all part numbers in the schematic is", result)