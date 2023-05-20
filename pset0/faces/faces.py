''' Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( 
was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically! '''

# Ask the user for input, and call the convert method to print emojis to the console.
def main():
    user_input = convert(input("Say something: "))
    print(user_input)

# Takes in a string and returns it with all instances of ":)" and ":(" replaced with corresponding emojis.
def convert(user_input):
    return user_input.replace(":)", "🙂").replace(":(", "🙁")

main()