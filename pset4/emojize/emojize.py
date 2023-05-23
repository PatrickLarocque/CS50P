''' implement a program that prompts the user for a str in English and then outputs 
the “emojized” version of that str, converting any codes (or aliases) therein to their 
corresponding emoji. '''

import emoji

user_input = input("Input: ").strip()
print(emoji.emojize(f"Output: {user_input}"))