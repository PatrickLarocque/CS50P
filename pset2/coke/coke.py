''' Implement a program that prompts the user to insert a coin, one at a time, each time 
informing the user of the amount due. Once the user has inputted at least 50 cents, output 
how many cents in change the user is owed. Assume that the user will only input integers, and 
ignore any integer that isn't an accepted denomination. '''

def main():
    coke_machine()

# A coke can costs 50 cents. The machine accepts accepts quarters, dimes or nickels from thee user and pays back any change over 50 cents. 
def coke_machine():
    amount_due = 50
    accepted_denominations = [25, 10, 5]
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in accepted_denominations:
            amount_due -= coin
        if amount_due <= 0:
            print(f"Change Owed: {amount_due * -1}")


if __name__ == "__main__":
    main()