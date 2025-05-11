import os
import csv


def read_file(filename: str):
    if not os.path.exists(filename):
        return "Papka yo'q"

    try:
        with open(file=filename, mode='r', encoding="UTF-8", newline="") as file:
            read = list(csv.reader(file))
            return [] if len(read) == 0 else read
    except BaseException as e:
        return e


def write_to_file(filename: str, data: list, mode: str = 'w'):
    with open(file=filename, mode=mode, encoding="UTf-8", newline="") as file:
        wrt = csv.writer(file)
        if mode == 'w':
            wrt.writerows(data)
        else:
            wrt.writerow(data)
    return


def generate_id(filename: str):
    read = read_file(filename=filename)
    if len(read) == 0:
        return 1
    else:
        return int(read[-1][0]) + 1