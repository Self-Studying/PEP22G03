def mypassword():
    correct_password = 9
    while True:
        password = input("Scrie parola:")
        if password == 'q':
            break
        correct_password = correct_password ** int(correct_password)
        print("Acesta este numarul corct")



mypassword()