# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:39:53 2024

@author: nidhi
"""

import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected for the password.")
    
    # Randomly generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, use_uppercase, use_lowercase, use_digits, use_special

def main():
    length, use_uppercase, use_lowercase, use_digits, use_special = get_user_input()
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

