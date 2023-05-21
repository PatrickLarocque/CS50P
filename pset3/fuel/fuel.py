''' 
Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each 
of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, 
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate 
that the tank is essentially empty. And if 99% or more remains, output F instead to indicate 
that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user 
again. Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

# Prompt user for input until a valid fraction is provided.
while True:
    try:
        fraction = input("Fraction: ").strip().split("/")

        # Gaurd clauses for if numerator/denominator are not integers or if numerator is > than denominator.
        if not float(fraction[0]).is_integer() or not float(fraction[1]).is_integer() or int(fraction[0]) > int(fraction[1]):
            raise ValueError

        # ValueError or ZeroDivisionError raised if either X or Y cannot be converted to a float or if Y is 0.
        percent_full = float(fraction[0]) / float(fraction[1])

    except (ValueError, ZeroDivisionError):
        print("Please provide a valid fraction.")
    else:
        if percent_full <= 0.01:
            print("E")
        elif percent_full >= 0.99:
            print("F")
        else:
            print(f"{int(round(percent_full * 100, 0))}%")
        break