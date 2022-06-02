b = 13
h = 27

A = 1 / 2 * b * h
print(A)
print(type(A))

my_value = input("Please define the baze: ")
my_value1 = input("Please define your height? ")

password = 7710
guess_passwd = int(input("Please guess my password:?!"))
print(password == guess_passwd)


def check_password():
    if password is guess_passwd:
        print("Password guessed successfully!")
    else:
        pass


check_password()
