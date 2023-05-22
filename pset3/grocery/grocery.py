''' Implement a program that prompts the user for items, one per line, until the user 
inputs control-d (which is a common way of ending one's input to a program). Then output 
the user's grocery list in all uppercase, sorted alphabetically by item, prefixing each 
line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user's input case-insensitively. '''

def main():
    grocery_list()

def grocery_list():
    grocery_list = {}

    # Add items to the list until the user inputs control + d.
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        # If a key was already in the list, increment its vaLue by 1, else add the item to the with a value of 1.
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list.update({item : 1})

    # Loop through grocery list sorted alphabettically, printing first the value followed by the key.
    for item in sorted(grocery_list.keys()):
        print(grocery_list[item], item)

main()