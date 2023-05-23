'''
Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 
9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below.
Then output that same date in YYYY-MM-DD format. If the user's input is not a valid date in either format, 
prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month 
has 28, 29, 30, or 31 days.
'''

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    # Reprompt user until a valid date format is input.
    while True:
        date = input("Date: ").strip().title()
        try:
            # Attempt to split user input at each '/', else reprompt.
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if month > 12 or month < 0 or day > 31 or day < 0:
                continue
            else: 
                break
        except:
            try:
                # Attempt to split user input at each white space. Indexing into the list created by split will fail if no white spaces were found, reprompting the user.
                month_day_year = date.split(" ")
                # Attempt to locate comma afer day, raises ValueError if no comma found.
                month_day_year[1].index(",")
                month = month_day_year[0]
                day = int(month_day_year[1].replace(",", "").strip())
                year = int(month_day_year[2].strip())
                if not month[0].isalpha or month not in months:
                    continue
                elif (day > 31 or day <= 0):
                    continue
                else:
                    # Convert month name to its number value by using its index in months list.
                    for i in range(len(months)):
                        if month == months[i]:
                            month = i + 1
                            break
                    break         
            except:
                continue
    
    # Input was sucessfully validated.
    format_date(month, day, year)

# Format the validated input into the desired format.
def format_date(month, day, year):
        print(f"{year}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()