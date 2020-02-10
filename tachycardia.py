# tachycardia.py


def is_tachycardic(word):
    # could be upper, lower, mixed case
    word = word.lower()
    # or have punctuation
    import string
    table = str.maketrans('', '', string.punctuation)
    word = word.translate(table)
    # or have leading/trailing spaces
    word = word.strip()
    if word == "tachycardic":
        return True
    else:
        # check if spelling error
        x = 0
        for i in word:
            if i in "tachycardic":
                x += 1
        if x >= 9:
            return True
        else:
            return False


# if __name__ == "__main__":
    # word = input("Input word: ")
    # is_tachycardic(word)
