''' Using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address 
via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address. You may not use re. 
And do not validate whether the email address's domain name actually exists. '''

import validators


def main():
    print(validate(input("What's your email address? ")))
    
    
 # Using validators' email function to validate that the input complies with the format of an email address.   
def validate(email):
    if validators.email(email):
        return "Valid"
    return "Invalid"

    
if __name__ == "__main__":
    main()