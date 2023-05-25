''' Implement a program that prompts the user for a str of text and then outputs that same 
text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. '''

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user_input = input("Input: ").strip()

# Loop through user's string, removing vowels when encoutered.
for char in user_input:
    if char in vowels:
        user_input = user_input.replace(char, "")

print(user_input)