'''
Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file 
in Pinocchio's format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI 
at pypi.org/project/tabulate. Format the table using the library's grid format. If the user does not 
specify exactly one command-line argument, or if the specified file's name does not end in .csv, or 
if the specified file does not exist, the program should instead exit via sys.exit.
'''
from sys import exit, argv
from tabulate import tabulate
from csv import reader, DictReader

def main():
    is_valid_command_line_arguments(argv)
    menu = argv[1]
    keys = get_menu_keys(menu)
    menu_items = get_menu_items(menu, keys)
    # Formats the list of dicts tabularly.
    print(tabulate(menu_items, headers="keys", tablefmt="grid"))

# Validate that command-line has 1 arugement, and that arugment has a valid '.csv' file exstension.
def is_valid_command_line_arguments(argv):
    if len(argv) < 2:
        exit("Too few command-line arguments.")
    elif len(argv) > 2:
        exit("Too many command-line arguments.")
    elif not argv[1].endswith(".csv"):
        exit("Not a valid CSV file.")
    
# Get the header names in the first row of a csv file to use as dict keys.
def get_menu_keys(menu):
    with open(menu) as file:
        for line in file:
            keys = line.rstrip().split(",")
            return keys

# Returns the menu formatted as a list of dicts, where each item corresponds to its key according to the csv.
def get_menu_items(menu, keys):
        menu_items = []
        with open(menu) as file:
            reader = DictReader(file)
            for row in reader:
                menu_items.append({
                    keys[0]: row[keys[0]], 
                    keys[1]: row[keys[1]], 
                    keys[2]: row[keys[2]]})
        return menu_items


if __name__ == "__main__":
    main()