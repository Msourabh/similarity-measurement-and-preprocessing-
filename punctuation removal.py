import string
def clear_punctuation(s):
    clear_string = ""
    for symbol in s:
        if symbol not in string.punctuation:
            clear_string += symbol
    return clear_string



print(clear_punctuation('"i love u, my dear-friend=======jhkjh"'))

