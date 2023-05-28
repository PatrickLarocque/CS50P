''' Implement a program that:

Expects the user to provide two command-line arguments:

    1. the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    2. the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    3. Converts that input to that output, splitting each name into a first name and last name. Assume that each student 
    will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via 
sys.exit with an error message. '''

from csv import DictReader, DictWriter
from sys import argv, exit

def main():
    before = argv[1]
    after = argv[2]
    pre_split = read_csv(before)
    post_split = split_first_last_name(pre_split)
    write_csv(after, post_split)
    
# Validate that command-line has 2 arugement, and those arugment have valid '.csv' file exstensions.
def is_valid_command_line_arguments(argv):
    if len(argv) < 3:
        exit("Too few command-line arguments.")
    elif len(argv) > 3:
        exit("Too many command-line arguments.")
    elif not argv[1].endswith(".csv") or not argv[2].endswith(".csv"):
        exit("Not a valid CSV file.")

# Reads a csv file and composes a list of dicts containing each key value pair read, returns that list of dicts.
def read_csv(before):
        pre_split = []
        try:
            with open(before) as file:
                reader = DictReader(file)
                for row in reader:
                    pre_split.append({"name": row["name"], "house": row["house"]})
        except FileNotFoundError:
            exit(f"Could not read {before}")
        return pre_split
    
# Splits the name key of the pre_split list of dicts into to two keys, first and last, then recomposes a new list of dicts called post_split, now with 3 keys.
def split_first_last_name(pre_split):
    post_split = []
    for row in pre_split:
        names = row["name"].replace(" ", "").split(",")
        post_split.append({"first": names[1], "last":names[0], "house": row["house"]})
    return post_split

# Writes the new post_split list of dicts to a new csv file, now with name split into first and last.
def write_csv(after, post_split):
    keys = post_split[0].keys()
    try:
        with open(after, "w") as file:
            writer = DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(post_split)
    except FileNotFoundError:
        exit(f"Could not read {after}")


if __name__ == "__main__":
    main()