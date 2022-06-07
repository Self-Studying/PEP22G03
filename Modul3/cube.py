i = 2
while i > 2:
    print("*")
    i -= 2
print(i)

for i in range(-1, 1):
    print("#")

my_list = [3, 1, -1]
my_list[-1] = my_list[-2]
print(my_list)

my_list = "Python is Great!"
print(my_list[1:6:2])

"""-> start slice; end slice; pas slice[literele,caracterele care se vor omite]"""
print(len(my_list))
print(id(str))
print(my_list[:18])
print('King of Sun is :', my_list[11::2])