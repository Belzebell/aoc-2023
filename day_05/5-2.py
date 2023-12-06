# read file and initialise variables
file = open('testinput.txt', 'r')
lowest_loc = None
seeds = []
map_name = ''
seed_pairs = {}
mapper = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
}

def getLocationForSeed(seed):

    # we can just loop through as the mapper already has correct order of maps
    # if our seed falls between source and its offset, find the difference and map it to the destination
    # if it does not fall between, the value should stay the same for the next map
    for key in mapper:
        for map_part in mapper[key]:
            dest, source, offset = map_part  # unpack the map part
            if seed >= source and seed < (source + offset):
                diff = seed - source
                seed = dest + diff
                break
    return seed  # seed is now location

# loop through input, grab seed numbers and populate map dicts
for line_no, line in enumerate(file):
    line = line.strip()

    # get seed numbers (ignore first part, which is the identifier)
    if 'seeds:' in line:
        seeds = line.split(' ')[1:]

        # now convert these into pairs
        for key, seed in enumerate(seeds):
            if key%2 == 0:  # every other seed is a key for the following value
                seed_pairs[seed] = seeds[key+1]
        continue

    # if the line contains the word 'map', we start describing a new map from here
    # otherwise, add to current map (ignore empty lines)
    if 'map:' in line:
        map_name = line.split(' ')[0]
    elif not line == '':
        # now we have a map line
        # populating the array would become to big with the real input, so we only store the maps and calculate later
        dest, source, offset = line.split(' ')
        mapper[map_name].append([int(dest), int(source), int(offset)])

file.close()  # we are done reading the file

for seed, range in seed_pairs.items():
    i = 0
    while i < int(range):
        loc = getLocationForSeed(int(seed) + i)
        if lowest_loc is None:
            lowest_loc = loc  # first location we find is automatically lowest for now
        elif(loc < lowest_loc):
            lowest_loc = loc
        i = i + 1

print("The lowest location number for the initial seed numbers is", lowest_loc)

