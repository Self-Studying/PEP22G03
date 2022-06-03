year = int(input("Enter a year: "))

if year // 100:
    print("The year is a leap year!")
elif year // 400:
    print("It's a common yar!")
else:
    print("It's a leap year!")

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
