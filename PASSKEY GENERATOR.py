# Just the simplest script I could think of to create a simple random password.
# Just run it anywhere.

import random

str_length = random.randint(8, 16)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

algorism = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

input_MAC = []

while len(input_MAC) != str_length:
    picker = random.randint(1, 2)
    alphabet_chooser = random.randint(0, 25)
    algorism_chooser = random.randint(0, 9)

    if picker == 1:
        input_MAC.append(alphabet[alphabet_chooser])
    else:
        input_MAC.append(algorism[algorism_chooser])


output_MAC = "".join(input_MAC)
print(output_MAC)

# Plans to def it in the future and further improve.
