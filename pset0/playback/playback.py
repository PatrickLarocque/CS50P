''' Some people have a habit of speaking rather quickly, and it'd be nice to slow them down, a la YouTube's 0.75 playback 
speed, or even by having them pause between words. '''

# Format user's input, replacing all spaces with '...' and assign the result to a variable.
user_input = input("Say something: ").replace(" ", "...")

# Print the resulting variable to the console.
print(user_input)