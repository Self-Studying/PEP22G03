from termcolor import colored


def ismypwd():
    good_password = False
    while not good_password:
        my_input = input("Introduceti o parola: ")
        for number in range(0, 10):
            if str(number) in my_input:
                break
            print("Parola nu contine o cifra.")
            continue
        if len(my_input) < 8:
            print("Parola are lungimea corespunzatoare! ")
            continue
        for letter in "!@%":
            if letter in my_input:
                break
        else:
            print("Parola nu are caracter special.")
            continue
        if my_input[0] == my_input[0].upper:
            good_password = True
        else:
            continue
        print("Parola contine un caractyer special")


ismypwd()
