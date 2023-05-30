''' Implement a function called validate that expects an IPv4 address as input as a str 
and then returns True or False, respectively, if that input is a valid IPv4 address or not.
You may not import any other libraries. You're welcome, but not required, to use re and/or sys.
Either before or after you implement validate in numb3rs.py, additionally implement, in a file 
called test_numb3rs.py, two or more functions that collectively test your implementation of validate 
thoroughly, each of whose names should begin with test_ so that you can execute your tests with pytest. '''

import re
from sys import exit

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        segments = ip.split(".")
        if len(segments) < 4 or len(segments) > 4:
            return False
    except ValueError:
       exit("Invalid IP address.")
    else:
        # Match groups for each segment: 0 - 199 or 200 - 249 or 250 - 255
        for segment in segments:
            if not re.search(r"^([1]?[1-9]?[0-9]|2[0-4][0-9]|25[0-5])$", segment):
                return False
        return True

    # It is possible to match the hold string by repeating the above regular 4 times expression with literal a '.' between each match group.
    # if re.search(r"^([1]?[1-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([1]?[1-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([1]?[1-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([1]?[1-9]?[0-9]|2[0-4][0-9]|25[0-5])$", ip):
    #     return True
    # return False

if __name__ == "__main__":
    main()