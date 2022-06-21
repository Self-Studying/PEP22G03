x = 3  # hardcode your test data here
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1  # write your code here
print("y =", y)

# this program counts the number of seconds in a given hour
# this program has been written yestersay

a = 2  # assigning a value to our variable equal to two hours
seconds = 3600  # number of seconds in onwe hour
hour = 1800
print("Hours: ", a, hour, end="\n", sep=",")  # printing the number of hours
# print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

# here we should also
print("Goodbye")
# but a programmer didn't have time to write any code
# EOF that computes the number of seconds in 3 hour
# This is a multiline comment.

print("Hello!")
anything = input("Tell me about you?")
print("Hmm...", anything, "...Really?")

# Testing TypeError message.

anything = input("Enter a number: ")
something = int(anything) ** 2.0
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)


def hypotenuse():
    long_a = float(input("Please type the length for long_a:"))
    long_b = float(input("Please type second value for long_b:"))
    print("Hypotenuse is :", (long_a ** 2 + long_b**2) * .5)


hypotenuse()

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
print("+" + 10 * "_" + "+")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
height = 1.85 # input a float value for variable a here
weight = 90.5 # input a float value for variable b here

result = height + weight
print(result)# output the result of addition here
result_1 = height - weight# output the result of subtraction here
print(result_1)
print(height * weight)# output the result of multiplication here
print(float(weight / height))# output the result of division here

print("\nThat's all, folks!")

#x = input(str("Enter value for x: "))

#y = (1 / (x + (1/1))/(x + (1/1))/(x+ (1/x)))
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print(hour,mins,dura)# Write your code here.