def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!,2023")


def happy_new_year2023(wishes=False):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year,2023!")


def strange_function(n):
    if n % 2 > 0:
        return


def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))

strange_function(n=16)
happy_new_year()