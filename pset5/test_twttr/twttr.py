def main():
    word = input("Input: ").strip()
    vowelless_word = shorten(word)
    print(vowelless_word)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in word:
        if char in vowels:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()