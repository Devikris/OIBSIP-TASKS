import random
import string

def generate_password(min_length, number=True, special=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special:
        characters += special_characters

    pwd = ""
    meet_crit = False
    has_number = False
    has_special = False

    while not meet_crit or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special_characters:
            has_special = True

        meet_crit = True
        if number:
            meet_crit = has_number
        if special:
            meet_crit = meet_crit and has_special

    return pwd


min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want numbers (y/n): ").lower() == 'y'
has_special = input("Do you need special characters (y/n): ").lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)
print("Generated password:", pwd)
