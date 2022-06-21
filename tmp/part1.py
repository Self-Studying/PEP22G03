# defining and integer
number = 3

print(type(number))

# proceeding with casting, converting a string to integer
number = int('3')
print("Nr as text", type(number))
number = 3.1
print(type(number))

# knowing booleans

bool_object = False
print(type(bool_object))
# printing the address from memory of a builtin function
print("Address is : ", id(bool_object), ".")
print(id(9363136))

# float number and printing it's address from computer memory

number = 34687560707754458483040500
print(id(number))
number = 3

print(id(number))

number = '3'
print(id(number))

number1 = 34687560707754458483040500
number2 = '3'
print("Check numbers", number1 == number2 and number1 is number2)
number1 = 3
number2 = int('3')
print("Check numbers", number1 == number2 and number1 is number2)

print("Convert to bool: ", bool(0))
print("Convert to int: ", int(True))
