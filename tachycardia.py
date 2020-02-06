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
        print("True")
        return True
    else:
        spellcheck(word)
        #print("False")
        #return False


def spellcheck(word):
    target_word = []
    my_word = []
    for char in "tachycardic":
        target_word.append(char)
    for char in word:
        my_word.append(char)
    print(target_word)
    print(my_word)
    # if 9/11 chars match, return True
    x, y = 0, 0
    for i in word:
        if "tachycardic".find(i) >= 0 and y == word.find(i):
            x += 1
            print(i, x)
        y += 1
    if x >= 9:
        print("True")
        return True
    else:
        print("False")
        return False


if __name__ == "__main__":
    word = input("Input word: ")
    is_tachycardic(word)
