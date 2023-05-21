''' Implement a program that prompts users to input a fruit (case-insensitively) and then 
outputs the number of calories in one portion of that fruit, per the FDA's poster for fruits, 
which is also available as text. Capitalization aside, assume that users will input fruits exactly 
as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn't a fruit. '''

# List of dictionaries, each key/value pair being the fruit's name and associated calorie count.
fruits = [
    {"fruit": "apple", "calories": 130},
    {"fruit": "avocado", "calories": 50},
    {"fruit": "banana", "calories": 110},
    {"fruit": "grapefruit", "calories": 60},
    {"fruit": "grqapes", "calories": 90},
    {"fruit": "honeydew melon", "calories": 50},
    {"fruit": "kiwifruit", "calories": 90},
    {"fruit": "lemon", "calories": 15},
    {"fruit": "lime", "calories": 20},
    {"fruit": "nectarine", "calories": 60},
    {"fruit": "orange", "calories": 80},
    {"fruit": "peach", "calories": 60},
    {"fruit": "pear", "calories": 100},
    {"fruit": "pineapple", "calories": 50},
    {"fruit": "plums", "calories": 70},
    {"fruit": "strawberries", "calories": 50},
    {"fruit": "sweet cherries", "calories": 100},
    {"fruit": "tangerine", "calories": 50},
    {"fruit": "watermelon", "calories": 80},
]

# Get user input, strip away white spaces and normalize to lower case.
user_input = input("Item: ").strip().lower()

# Loop through list of fruits, matching the user's input to the fruit key in each dictionary.
for fruit in fruits:
    if fruit["fruit"] == user_input:
        print("Calories: " + str(fruit["calories"]))
