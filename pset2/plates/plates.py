''' 
In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with your 
choice of letters and numbers instead of random ones. Among the requirements, though, are:

    "All vanity plates must start with at least two letters."
    "… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."
    "Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an 
    acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'."
    "No periods, spaces, or punctuation marks are allowed."
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Checks to verify that the vanity plate formatting is valid in Massachusetts.
def is_valid(plate):
    # Guard clauses that can checked immediately.
    if len(plate) < 2 or len(plate) > 6 or plate[0:1].isnumeric() or not plate.isalnum():
        return False
    
    # Whenever a character is numeric and not 0, all subsequent characters must be numeric.
    for char in plate:
        if char.isnumeric():
            if plate[plate.index(char):len(plate)].isnumeric() and int(char) != 0:
                return True
            else:
                return False
            
    # Formatting is validated. All characters in plate are letters.
    return True

main()