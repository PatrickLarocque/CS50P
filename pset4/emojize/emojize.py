''' implement a program that prompts the user for a str in English and then outputs 
the “emojized” version of that str, converting any codes (or aliases) therein to their 
corresponding emoji. '''

from emoji import emojize

user_input = input("Input: ").strip()
print(emojize(f"Output: {user_input}"))