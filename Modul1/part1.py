import cmd
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
print("Programming***Essentials***in...", end="")
print("Python")

print(colored("    *", "magenta"))
print(colored("  * *  *", "magenta"))
print(colored(" *  *   *", "magenta"))
print(colored("*   *    *", "magenta"))
print(colored("****    ***", "magenta"))
print(colored("  *  * *", "magenta"))
print(colored("  *  * *", "magenta"))
print(colored("  ******", "magenta"))
print(.4)
print(3E8)
print(0.000000000000000000000003)

print('I\'m Month python!')
print("I'm Monthy python!")
print(True > False)
print(True < False)
print('i\'m', '""learning\""', '""python\""\n')
print(2 + 2)
print(int("2" + "2") * int("3"))
print(2 * 3)
print(2 * 3)
print(.2 * .3)
print(.2 * 3)
print(2. * 3)

print()

print(8 / 2)
print(8 / 2.)
print(8. / 2)
print(8. / 2.)
print(.8 / 2)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(-6 // 4)
print(6. // -4)
print(14 % 4)
print(14 // 4)
print(14 / 4)
print(12 % 4.5)
print(-4 - 4)
print(-4. + 8)
print(+2 - 2)
print(-1.1)
print(9 % 6 % 2)
print(2 % 6 % 9)

print(4 ** 4 ** 4)
print(4e4)


import os, sys

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
log = 'python'
print(os.system(log))
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)