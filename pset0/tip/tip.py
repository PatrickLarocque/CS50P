''' And now for my Wizard tip calculator. — Morty Seinfeld '''

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Converts user's dollar amount string to its float value.
def dollars_to_float(dollars):
    return float(dollars.strip("$ "))

# Converts user's percentage string to its float representation.
def percent_to_float(percent):
    return float(percent.strip("% "))/100

main()