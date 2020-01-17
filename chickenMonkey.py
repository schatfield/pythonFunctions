# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.

# you are trying to print out numbers 1-100

# generate a list of 1-100
numbers_1_to_100 = range(1,101)

# iterate over the list to print it out


for i in numbers_1_to_100:
    if (i % 5 == 0) & (i % 7 == 0):
        print("chicken monkey")

    elif i % 5 == 0:
        print("chicken")
    elif i % 7 == 0:
        print("monkey")
    else:
        print(i)



