# storing the largest number

largest_number = -999999999

# input the first value

number = int(input("Enter a number or type -1 to stop: "))

# if the number is not equal to -1, continue

while number != -1:
    # is the number larger than largest_number?
    if number > largest_number:
        # yes, update largest_number
        largest_number = number
    # input the next number

    number = int(input("Enter a number or type -1 to stop : "))

# printing the largest number


print("The largest number is ", largest_number)