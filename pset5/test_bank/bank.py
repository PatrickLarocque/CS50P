def main():
    # Store the user's greeting, stripped of white spaces and normalized to lower case.
    greeting = input("Greeting: ").strip()
    reward = value(greeting)
    print(f"${reward}")

# Normalize greeting to lower case. Return the appropriate value depending on greeting.
def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()