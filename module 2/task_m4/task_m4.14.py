import sys


def parse_args():
    result = ""
    for arg in sys.argv[1::]:
        result += str(arg) + " "

    return result[:-1]