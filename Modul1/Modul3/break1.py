  GNU nano 6.3                                                                              break1.py *
# import the library that is about to be used
import getpass

# defining the variable
exit_word = "chupacabra"

# creating a while loop

while True:
    user_request = getpass.getpass("Type a word: ")
    if user_request != exit_word:
        continue
    elif user_request == exit_word:
        print("You have successfully exit the loop!")
        break

# EOF the program



