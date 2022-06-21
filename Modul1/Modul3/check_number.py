secret_number = 777
guess_my_number = int(input("Please guess my number: \n"))
while guess_my_number == secret_number:
    secret_number = guess_my_number
    if guess_my_number == secret_number:
        print(
            "\n"
            "+================================+\n"
            "| Welcome to my game, muggle!    |\n"
            "| Enter an integer number        |\n"
            "| and guess what number I've     |\n"
            "| picked for you.                |\n"
            "| So, what is the secret number? |\n"
            "+================================+\n")
        break
    elif guess_my_number != secret_number:
        print("Well done , keep guessing !")
    else:
        break
