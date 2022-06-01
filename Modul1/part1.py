import datetime
from termcolor import colored
print("hello world!\n", 'My Object', end="#", sep="-abcd-", )
print(datetime.datetime.now())
print('print')

print("############################\n"
      "#                          #\n"
      "############################")
print(type(print))
print(type(3))
print(type('3'))
print(3 + 3)
print("3" + "3")
print("3" * 5)
print("#" * 30, "\n", "#                         #\n", "#" * 30)

print("#" * 30)
print(sep=" ")
print("#" * 28)
print("#" * 30)

my_value = "#" * 30
my_value1 = "#" + ' ' * 28 + "#"
print(my_value, my_value1, my_value, sep='\n')
print("my name", "is", end="")

print("#" * 30, "#" + ' ' * 28 + "#", "#" * 30, sep="\n")
print("My", 'name', "is", "Python", "Monty", "Python.", sep="-")
print("My", 'name', "is", "Python", "Monty", "Python.", sep="")
print("My", 'name', "is", "Python", "Monty", "Python.", sep=" ")
print()
print("My", "Name", "is", sep="_", end="*")
print("Monty", "Python", sep="*", end="*\n")
print("Programming***Essentials***in...",end="")
print("Python")


print(colored("    *", "magenta"))
print(colored("  * *  *","magenta"))
print(colored(" *  *   *", "magenta"))
print(colored("*   *    *", "magenta"))
print(colored("****    ***", "magenta"))
print(colored("  *  * *", "magenta"))
print(colored("  *  * *", "magenta"))
print(colored("  ******", "magenta"))
print(.4)
print(3E8)
print(0.000000000000000000000003)