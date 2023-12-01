#read input
import re

input = open('input.txt')
digits = []
result_values = []
result = 0

#loop through input, for every line get list of digits using regex
for line in input:
    re_digits = re.findall(r'\d', line)
    digits.append(re_digits)

#loop through found digits and concat first and last for every row
for line_digits in digits:
    concat_val = line_digits[0] + line_digits[-1] #+ concatenates here as the digits are still strings
    result_values.append(concat_val)

#now we have an array of all calibration values and just need to sum them up
for value in result_values:
    result += int(value)

print("The sum of all calibration values is", result)