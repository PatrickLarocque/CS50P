''' Suppose that you're in a country where it's customary to eat breakfast between 7:00 and 8:00, 
lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn't it be nice if you had 
a program that could tell you what to eat when? '''

def main():
    # Get a time for the user.
    time = input("What time is it? ").strip()

    # Handles the user input wherein time is in a 12 hour format. ***Supplementary challenge***
    if time.endswith("a.m") or time.endswith("p.m"):
        twelve_hour_format(time)
    
    # Handles the user input wherein time is in a 24 hour format.
    else:
        time = convert(time)
        if 7 <= time <= 8:  
            print("breakfast time")
        elif 12 <= time <= 13:
            print("lunch time")
        elif 18 <= time <= 19:
            print("dinner time")

# Converts time from a string to its float representation.
def convert(time):
    time = time.split(":")
    minutes = float(time[1]) / 60
    return(float(time[0]) + minutes)

# Handles the user input wherein time is in a 12 hour format. 
def twelve_hour_format(time):
    # Split time into a tupple where the first element represents the hour and assign it to a variable.
    time = time.split(":")
    hours = int(time[0])

    # Split the second element of the tuple further, creating a new tuple where the first element is minutes and the second is a.m or p.m. 
    time = time[1].split()
    minutes = int(time[0])
    suffix = time[1]

    # Conditionals to handle 12 hour time format.
    if hours == 7 or (hours == 8 & minutes == 0) and suffix == "a.m":
        print("breakfast time")
    elif hours == 12 or (hours == 1 and minutes == 0) and suffix == "p.m":
        print("lunch time")
    elif hours == 6 or (hours == 7 and minutes == 0) and suffix == "p.m":
        print("dinner time")
    else:
        return
    
if __name__ == "__main__":
    main()