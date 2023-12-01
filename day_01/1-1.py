import re

# read file and initialise variables
file = open('testinput.txt', 'r')
digits = []
result_values = []
result = 0

# loop through input, for every line get list of digits using regex,
# then concat the first and last, cast to int and add to the result
for line in file:
    re_digits = re.findall(r'\d', line) #regex to find all digits in the line
    concat_val = re_digits[0] + re_digits[-1]  # + concatenates here as the digits are still strings
    result += int(concat_val)

file.close()  # we are done reading the file

print("The sum of all calibration values is", result)