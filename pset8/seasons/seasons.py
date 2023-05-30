''' In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then 
prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song 
from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that 
the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even 
if the user runs the program at noon, assume that it's actually midnight, on the same date. Use datetime.date.today to get today's date. '''

from datetime import date, datetime
from sys import exit
import inflect
import operator


def main():
    try:
        print(minutes_between(input("Date of Birth: ")))
    except ValueError:
        exit("Invalid date.")

# Gets the delta between today's date and the user's date of birth, converta the delta to minutes then uses inflect to turn the value in minutes to words.
def minutes_between(birth_date):
    # ValueError raised if dob cannot be converted to a datetime object. 
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = date.today()
    delta = str(operator.__sub__(today, birth_date))
    delta = delta.split(" ")
    days = int(delta[0])
    minutes = days * 24 * 60
    engine = inflect.engine()
    words = engine.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()