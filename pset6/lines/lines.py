''' Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, 
and outputs the number of lines of code in that file, excluding comments and blank lines. If the user 
does not specify exactly one command-line argument, or if the specified file's name does not end in .py, 
or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring 
should not be considered a comment.) Assume that any line that only contains whitespace is blank. '''

from sys import argv, exit

def main():
    if is_valid_command_line_argument(argv):
        lines = get_lines(argv[1])
        print(count_lines(lines))

# Validate that command-line has 1 arugement, and that arugment has a valid Python file exstension.
def is_valid_command_line_argument(argv):
    if len(argv) < 2:
        exit("Too few command-line arguments.")
    elif len(argv) > 2:
        exit("Too many command-line arguments.")
    elif not argv[1].endswith(".py"):
        exit("Not a Python file.")
    return True

# Open the file, store each line as an element in a list.
def get_lines(python_file):
    lines = []
    try:
        with open(python_file) as file:
            lines = file.readlines()
    except FileNotFoundError:
        exit("File does not exist.")
    return lines


# Count the lines of code, not including comments. Docstrings are included.
def count_lines(lines):
    line_count = 0
    for line in lines:
        line = line.strip()
        if len(line) > 0 and not line.startswith("#"):
            line_count += 1
    return line_count


if __name__ == "__main__":
    main()