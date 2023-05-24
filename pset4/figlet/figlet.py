from pyfiglet import Figlet
from random import choice
import sys

# Initialize figlet and the list of fonts.
figlet = Figlet()
fonts = figlet.getFonts()

def main():
    # When no arguments are provided, set a random font, then render the user's input to console.
    if len(sys.argv) == 1:
        user_input = input("Input: ").strip()
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(user_input))
    # When exactly 2 arguments are proviced, validate the '-f' or '--font' flag, and a valid font, then render the user's input to console.
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
        user_input = input("Input: ").strip()
        print(figlet.renderText(user_input))
    # The user provided invalid command line arugments.
    else:
        sys.exit("Please provide the -f flag followed by the name of the font. No arugments will produce a random font.")

if __name__ == "__main__":
    main()