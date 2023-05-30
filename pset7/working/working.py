import re


def main():
    print(convert(input("Hours: ")))


def convert(time):
    # Match a string having a valid twelve hour time format, guard clause raises a ValueError if no match was found.
    time = re.search(r"^([1]?[0-9])[:]?([0-5][0-9])? (AM|PM) to ([1]?[0-9])[:]?([0-5][0-9])? (AM|PM)$", time, re.IGNORECASE)
    if not time:
        raise ValueError
    # If the starting hour or ending hour values are greater than 12 or 0, guard clause raises a ValueError.
    if int(time.group(1)) > 12 or int(time.group(4)) > 12 or int(time.group(1)) == 0 or int(time.group(4)) == 0:
        raise ValueError
    
    # Segment each match group of the regular expression.
    start_hour = int(time.group(1))
    start_minute = time.group(2)
    start_am_or_pm = time.group(3)
    end_hour = int(time.group(4))
    end_minute = time.group(5)
    end_am_or_pm = time.group(6)

    # Edge cases
    if start_hour == 12 and start_am_or_pm == "AM":
        start_hour = 0
    if end_hour == 12 and end_am_or_pm == "AM":
        end_hour = 0
    if start_am_or_pm == "PM" and not start_hour == 12:
        start_hour = start_hour + 12
    if end_am_or_pm == "PM" and not end_hour == 12:
        end_hour = end_hour + 12
    if start_minute == None:
        start_minute = 0
    if end_minute == None:
        end_minute = 0

    # Returns a string with the times now in 24 hour format.
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    

if __name__ == "__main__":
    main()