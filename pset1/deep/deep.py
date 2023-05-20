''' 
“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker’s Guide to the Galaxy, Douglas Adams
'''

# Ask the user for input, stip white spaces and normalize to lower case.
user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

# Match user's input to print yes under the specified conditions, else print no to the console.
match user_input:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")