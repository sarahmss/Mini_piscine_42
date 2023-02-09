#!/usr/bin/env python3

from path import Path

def my_program():
    try:
        Path.makedirs("folder")
        Path.touch('folder/file')
        file = Path('folder/file')
        file.write_lines(['something'])
        print(file.read_text())
    except FileExistsError as exception:
        print(exception)


if __name__ == '__main__':
    my_program()