# tachycardia.py
def is_tachycardic():
    string = input("Input word: ")
    print("{}" .format(string))
    # could be upper, lower, mixed case
    string = string.lower()
    # or have leading/trailing spaces or punctuation
    print("{}" .format(string))
    if string == "tachycardic":
        print("True")
        return True


if __name__ == "__main__":
    is_tachycardic()
