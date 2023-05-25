def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Checks to verify that the vanity plate formatting is valid in Massachusetts.
def is_valid(plate):
    # Guard clauses that can be checked immediately.
    if len(plate) < 2 or len(plate) > 6 or plate[0].isnumeric() or plate[1].isnumeric() or not plate.isalnum():
        return False
    
    # Whenever a character is numeric and not 0, all subsequent characters must be numeric.
    for char in plate[2:len(plate)]:
        if char.isnumeric():
            if plate[plate.index(char):len(plate)].isnumeric() and int(char) != 0:
                return True
            else:
                return False
            
    # Formatting is validated. All characters in plate are letters.
    return True


if __name__ == "__main__":
    main()