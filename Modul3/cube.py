i = 2
while i > 2:
    print("*")
    i -= 2
print(i)

for i in range(-1, 1):
    print("#")
import pprint
my_list = [3, 1, -1]
my_list[-1] = my_list[-2]
print(my_list)

my_list = "Python is Great!"
print(my_list[1:6:2])

"""-> start slice; end slice; pas slice[literele,caracterele care se vor omite]"""
print(len(my_list))
print(id(str))
print(my_list[:18])
print(my_list[-6:])
print(my_list[-2])
print('King of Sun is :', my_list[11::2])  # eliminates values form ur string "::"

sir = "Hello Python {0} {1} {2}"

print(sir[:5],"+",sir[6:12],sep="_")
print("Hello Again!", + sir.__len__())
print("Hello Again!", sir.format("abcd", "hello", "watchdog"))
print("Hello Again!", sir.format("abcd", "hello", "MgHZ"))
my_input = input("Cum te numesti?\n")
varsta = int(input("Care este varsta ta , Ana? \n"))
an = 2022 - varsta
print(f"Deci te-ai nascut in {an} ")
