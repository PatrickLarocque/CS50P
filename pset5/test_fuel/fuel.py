import sys

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        # ValueError raised if no '/' to split.
        fraction = fraction.strip().split("/")
        # Gaurd clauses for if numerator/denominator are not integers or if numerator is > than denominator.
        if not float(fraction[0]).is_integer() or not float(fraction[1]).is_integer() or int(fraction[0]) > int(fraction[1]):
            raise ValueError
        # Convert x and y to floats, divide them, round the result and into an int.   
        percentage = int(round((float(fraction[0]) / float(fraction[1]) * 100), 0))
        return percentage
    except (ValueError, ZeroDivisionError):
       raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()