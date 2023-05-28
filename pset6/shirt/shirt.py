from sys import argv, exit
from PIL import Image
import os

def main():
    is_valid_command_line_arguments(argv)
    before = argv[1]
    overlay_images(before)


# Validate that command-line has 2 arugement, and those arugment have valid file exstensions and those both extensions match.
def is_valid_command_line_arguments(argv):
    if len(argv) < 3:
        exit("Too few command-line arguments.")
    elif len(argv) > 3:
        exit("Too many command-line arguments.")
    elif not argv[1].endswith(".jpg") and not argv[1].endswith(".jpeg") and not argv[1].endswith(".png"):
        exit("Invalid input.")
    else:
        first_arg = os.path.splitext(argv[1])
        first_arg_extension = first_arg[1]
        if not argv[2].endswith(first_arg_extension):
            exit("Input and output have different file extensions.")
            
def overlay_images(before):
    original = Image.open(before)
    shirt = Image.open("shirt.png")
    resized_shirt = shirt.resize(original.size)
    original.paste(resized_shirt, resized_shirt)
    original.save(argv[2])
    
    
if __name__ == "__main__":
    main()