# had to install regex library which exppands on re, in order to use "overlapped" param for edge ccase
import regex as re

# read file and initialise variables
file = open('input.txt', 'r')
# note how the dictionary uses string for the digits, as our regex also returns strings making it easier to concat and convert after
num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
split_lines = []
result_values = []
result = 0

pattern = '|'.join(num_dict.keys())  # concatenate the dictionary with pipe to build the pattern for the regex


# function to convert text to number from the dictionary, for tidier main function
def str_to_num(val):
    if val.isdigit():
        return val
    else:
        return num_dict.get(val)


# loop through input, for every line get list of digits using regex, try to convert first and last if they are a string,
# then concat the first and last, cast to int and add to the result
for line in file:
    re_digits = re.findall(r'\d|' + pattern, line, overlapped=True)  # regex to find all digits AND number strings from the dict
    concat_val = str_to_num(re_digits[0]) + str_to_num(re_digits[-1])  # + concatenates here as the digits are still strings
    result += int(concat_val)

file.close()  # we are done reading the file

print("The sum of all calibration values is", result)