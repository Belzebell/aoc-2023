# read file and initialise variables
file = open('input.txt', 'r')
seeds = []
map_name = ''
mapper = {
    'seed-to-soil': {},
    'soil-to-fertilizer': {},
    'fertilizer-to-water': {},
    'water-to-light': {},
    'light-to-temperature': {},
    'temperature-to-humidity': {},
    'humidity-to-location': {},
}

def getLocationForSeed(seed):

    # we can just loop through as the mapper already has correct order of maps
    for key in mapper:
        if seed in mapper[key]:
            seed = mapper[key][seed]
    return seed  # seed is now location

# loop through input, grab seed numbers and populate map dicts
for line_no, line in enumerate(file):
    line = line.strip()

    # get seed numbers (ignore first part, which is the identifier)
    if 'seeds:' in line:
        seeds = line.split(' ')[1:]
        continue

    # if the line contains the word 'map', we start describing a new map from here
    # otherwise, add to current map (ignore empty lines)
    if 'map:' in line:
        map_name = line.split(' ')[0]
    elif not line == '':
        # now we have a map line, and need to populate the map for the length of the offset
        dest, source, offset = line.split(' ')
        i = 0
        while i < int(offset):
            mapper[map_name][int(source) + i] = int(dest) + i
            i = i + 1

file.close()  # we are done reading the file

for key, seed in enumerate(seeds):
    loc = getLocationForSeed(int(seed))
    if key == 0:
        lowest_loc = loc
    elif(loc < lowest_loc):
        lowest_loc = loc

print("The lowest location number for the initial seed numbers is", lowest_loc)

