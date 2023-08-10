from random import randint


def get_random_password():
    string = ""
    for i in range(8):
        random_num = randint(40, 126)
        string += str(chr(random_num))

    return string


get_random_password()