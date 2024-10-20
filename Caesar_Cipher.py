from pyfiglet import figlet_format
from termcolor import colored

# Print the title of the program
title = "Caesar Cipher"
title_ascii = figlet_format(title, font="slant", justify="center")
title_colored = colored(title_ascii, color="cyan")
print(title_colored)


def caesar_cipher(text, shift, direction):
    # If the direction is "decode", reverse the shift
    if direction == "decode":
        shift *= -1
    result = ""
    # Iterate through each letter in the text
    for letter in text:
        # Check if the letter is an alphabet character
        if letter.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            # Find the position of the letter in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position with the shift
            new_position = (position + shift) % 26
            # Append the shifted letter to the result
            result += alphabet[new_position]
        else:
            # If the character is not an alphabet, add it as is
            result += letter
    return result

# Get the text input from the user and convert it to lowercase
text = input("Enter the text: ").lower()
# Get the shift number input from the user and convert it to an integer
shift = int(input("Enter the shift number: "))
# Get the direction input from the user (encode or decode)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
# Print the result of the Caesar cipher operation
print(f"Here is the {direction}d result: {caesar_cipher(text, shift, direction)}")