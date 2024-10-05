def caesar_cipher(text, shift, direction):
    if direction == "decode":
        shift *= -1
    result = ""
    for letter in text:
        if letter.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += letter
    return result
 
text = input("Enter the text: ").lower()
shift = int(input("Enter the shift number: "))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
print(f"Here is the {direction}d result: {caesar_cipher(text, shift, direction)}")