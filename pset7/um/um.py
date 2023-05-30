# It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more noticeable it tends to be!

import re

def main():
    print(count(input("Text: ")))

# Returns the number of matches found using um or Um as a word boundary.
def count(phrase):
    return len(re.findall(r"\b(um|Um)\b", phrase))
    


if __name__ == "__main__":
    main()