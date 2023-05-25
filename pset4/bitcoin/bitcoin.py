''' 
Implement a program that:

1. Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. 
2. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
3. Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which 
returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
'''
import requests
import sys

# Read the arugment vector. Exit if no arugments provided or if first arugment cannot be coverted to a float.
try:
    number_of_bitcoin = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
# Erroneous status code.
except requests.RequestException:
    print("API request failed.")
except (ValueError):
    sys.exit("Command-line arugment is not a valid number.")
except (IndexError):
    sys.exit("Missing command-line argument.")
# Valid command-line arugments and sucessful status code. Print the cost of the amount of bitcoin specificed at the current rate.
else:     
    amount = response["bpi"]["USD"]["rate_float"] * number_of_bitcoin
    print(f"${amount:,.4f}") 