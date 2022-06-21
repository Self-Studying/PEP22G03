# reading two numbers
number = int(input("Enter th first number: \n"))
nr = int(input("Please type the second number: \n"))

# choosing between two numbers the larger one

if number > nr:
    larger_number = number
else:
    larger_number = nr

# printing the result

print("The larger number is :", larger_number)