''' Adieu, adieu, to yieu, yieu, and yieu '''

from inflect import engine

# Accept names from the user until the user terminates using control + d. Pass the list of names for formatting to the adieu method.
def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.insert(len(names), name)
        except (EOFError):
            adieu(names)
            break

# Initializes the inflect engine and formats the list of names. Prints the formatted list to the console. 
def adieu(names):
        inflect = engine()
        formatted_names = inflect.join(names)
        print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()