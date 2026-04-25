# This is a simple password generator that allows users to create a password with a specified length and character types (letters, digits, symbols).
# Random password generator 
# Author : Asad Sajjad




import random    # Helps pick random characters
import string    # Gives ready made latters, digits and symbols.

print("Welcome to the password generator.")
print("I can generate password with different length and random characters.\n")


# user input for the length of the password 
password_length = int(input("Enter the length of the password: "))

use_letters = input("Do you want to include letters? (y/n): ").lower() == 'y'
use_digits = input("Do you want to include digits? (y/n): ").lower() == 'y'
use_symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y' 

characters = ""

# Build the character set based on user preferences
if use_letters:
    characters += string.ascii_letters
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation
print("Generating password...")
if not characters:
    print("You must select at least one character type (letters, digits, or symbols).")
    exit()


# Generate the password 
password = ""
for i in range(password_length):
    password += random.choice(characters) 

print("\nYour generated password is: ", password)
print("Thank you for using the password generator.")
