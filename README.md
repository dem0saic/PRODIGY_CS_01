# PRODIGY_CS_01
A Python program that can encrypt and decrypt text using Caesar Cipher Algorithm. 
It allows users to input a message and a shift value to perform Encryption and Decryption

## Caesar Cipher

# Overview
The **Caesar Cipher** is a simple encryption technique that shifts each letter in a message by a fixed number of positions in the alphabet. This program allows users to encrypt and decrypt messages using the Caesar cipher method.

# Features
- Encrypts and decrypts messages using the Caesar cipher.
- User-defined shift value for customizable encryption.
- Handles both uppercase and lowercase letters.
- Maintains non-alphabetic characters unchanged.

# Requirements
- Python 3.x

# Installation
1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

# Usage
To run the Caesar Cipher program, execute the following command in your terminal or command prompt:
```bash
python caesar_cipher.py
```
# Instructions
Enter the text you want to encrypt or decrypt when prompted.
Specify the shift number (an integer).
Type encode to encrypt the message or decode to decrypt it.

# Example Command
Enter the text: hello
Enter the shift number: 3
Type 'encode' to encrypt, type 'decode' to decrypt: encode
Here is the encoded result: khoor

# Code Explanation
The program consists of the following key components:

Title Display: The title "Caesar Cipher" is printed in a stylized ASCII format using the pyfiglet library.
Creator Information: Displays the creator's name and social media handles.
Welcome Message: A brief introduction to the program's functionality.
caesar_cipher(text, shift, direction): This function performs the encryption or decryption based on the specified shift and direction.
User Input: Collects input from the user for the text, shift value, and direction of operation.

# Creator
Created by: Dem0saic
GitHub: dem0saic
LinkedIn: owusuvincent

# License
This project is licensed under the MIT License - see the LICENSE file for details.
