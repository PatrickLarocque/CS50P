''' Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix 
that starts with a period (.) at the end of their name. '''

# Get input from the user, store their response in a variable, normalize to lower case, strip white spaces.
user_input = input("File name: ").strip().lower()

# Checks whether user's file name is suffixed by a valid extension and prints corresponding media type to console.
if user_input.endswith(".gif"):
    print("image/gif")
elif user_input.endswith(".jpg") or user_input.endswith(".jpeg"):
    print("image/jpeg")
elif user_input.endswith(".png"):
    print("image/png")
elif user_input.endswith(".pdf"):
    print("application/pdf")
elif user_input.endswith(".txt"):
    print("text/plain")
elif user_input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")