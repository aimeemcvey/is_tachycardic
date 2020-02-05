# tachycardia.py
def is_tachycardic():
    word = input("Input word: ")
    # could be upper, lower, mixed case
    # or have leading/trailing spaces or punctuation
    print("{}" .format(word))
    if word == "tachycardic":
        print("True")
        return True


if __name__ == "__main__":
    is_tachycardic()
