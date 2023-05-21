''' Implement a program that prompts the user for a str of text and then outputs that same 
text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. '''

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user_input = input("Input:" ).strip()

# Loop through user's string, removing vowels when encoutered.
for i in user_input:
    if i in vowels:
        user_input = user_input.replace(i, "")

print(user_input)