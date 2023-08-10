import pathlib
import sys


def print_file_name(file_name, full_name=False, margin=0, margin_item=''):
    margin = margin * margin_item
    if full_name:
        print(margin + str(file_name.absolute()))
    else:
        print(margin + str(file_name.name))


def main():
    file_name = pathlib.Path(sys.argv[0])
    print_file_name(
        margin_item='*',
        #full_name=True,
        margin=30,
        file_name=file_name
    )


if __name__ == "__main__":
    main()
