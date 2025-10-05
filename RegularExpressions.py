# To find and parse only number from rergex_sample.txt and print the sum of all numbers. Final output end with 908

import re # Importing regular expressions module or library

fname = 'rergex_sample.txt' # File name
handle = open(fname) # Open the file for reading
numlist = list() # Initialize an empty list to store numbers


for line in handle:
    line = line.rstrip() # Remove trailing whitespace characters
    stuff = re.findall('\d+', line) # Find all sequences of digits in the line
    if len(stuff) < 1: continue # If no digits found, skip to the next line
    for num in stuff: # Iterate over each found sequence of digits
        num = int(num) # Convert the string to an integer
        numlist.append(num) # Append the integer to the list

print(sum(numlist)) # Print the sum of the numbers in the list

# Final output end with 376908

#We can also use list comprehension to make the code more shorter and cleaner

import re

print(sum([int(num) for num in re.findall('\d+', open('rergex_sample.txt').read())]))
