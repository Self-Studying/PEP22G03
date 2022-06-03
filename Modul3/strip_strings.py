import re

user_word = input("Please type a word at your will:")
letters_to_remove = "aeiou"

pattern = "[" + letters_to_remove + "]"
new_string = re.sub(pattern, "", user_word)

print(new_string)
