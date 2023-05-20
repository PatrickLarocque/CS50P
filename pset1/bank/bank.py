''' 
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn't 
greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn't a “hello,” and 
so he asks for $100. The bank's manager proposes a compromise: “You got a greeting that starts with an 'h,' 
how does $20 sound?” Kramer accepts.
'''

# Store the user's greeting, stripped of white spaces and normalized to lower case.
user_input = input("Greeting: ").strip().lower()

# Prints the appropritate sum of money to the console, based on the user's greeting.
if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h") and not user_input.startswith("hello"):
    print("$20")
else:
    print("$100")