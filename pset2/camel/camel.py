''' Implement a program that prompts the user for the name of a variable in camel case and outputs the 
corresponding name in snake case. Assume that the user's input will indeed be in camel case. '''

user_input = input("camelCase: ").strip()

# Loop through user's string, if any characters are uppercased, replace with an underscore followed by the same lowercased letter.
for i in user_input:
    if i.isupper():
        user_input = user_input.replace(i, f"_{i.lower()}")
 
print(f"snake_case: {user_input}")