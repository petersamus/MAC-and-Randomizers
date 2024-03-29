# Just the simplest script I could think of to create a simple random password.
# Just run it anywhere.

import random


def random_password():

    str_length = random.randint(8, 20)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    algorism = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    symbols = ["!", "@", "#", "$", "%", "&", "¥", "£", "€"]

    input_MAC = []

    while len(input_MAC) != str_length:
        picker = random.randint(1, 4)
        alphabet_chooser = random.randint(0, 25)
        algorism_chooser = random.randint(0, 9)
        symbols_chooser = random.randint(0, 8)

        if picker == 1:
            input_MAC.append(alphabet[alphabet_chooser])
        elif picker == 2:
            input_MAC.append(alphabet[alphabet_chooser].upper())
        elif picker == 3:
            input_MAC.append(symbols[symbols_chooser])
        else:
            input_MAC.append(algorism[algorism_chooser])

    return "".join(input_MAC)


output_MAC = random_password()

print(output_MAC)
