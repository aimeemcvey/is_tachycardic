# tachycardia.py


def is_tachycardic(word):
    print("{}" .format(word))
    # could be upper, lower, mixed case
    word = word.lower()
    # or have punctuation
    import string
    table = str.maketrans('', '', string.punctuation)
    word = word.translate(table)
    # or have leading/trailing spaces
    word = word.strip()
    print("{}" .format(word))
    if word == "tachycardic":
        print("True")
        return True
    else:
        print("False")
        return False


if __name__ == "__main__":
    word = input("Input word: ")
    is_tachycardic(word)
