alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def letter_loc(word):
    return alphabet.index(word.lower())


def name_pos(word):
    a = ''
    for letter in word:
        a += str(letter_loc(letter))

    print(a)
    return a

print(name_pos("hello"))