import argparse
import os
import sys
import time
from multiprocessing import Process
from pathlib import Path

from certificate_generator import certificat


def load_names(file):
    with open(file, mode='r', encoding='utf-16') as csv_file:
        # need fix
        list2 = [row.split()[0] for row in csv_file]
        print(list2)
        return list2


def create_img(name):
    img = certificat(name)
    path = Path("output\\" + name + ".png")
    img.save(path.as_posix())  # for testing purposes


def load_credentials(file):
    try:
        with open(file) as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
    except Exception:
        print('failed to read file ')
        sys.exit(1)
    return lines


def wait():
    blah = "\|/-\|/-"
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    args = parser.parse_args()

    list = load_credentials(args.file)

    if not os.path.exists("output"):
        os.makedirs("output")

    processes = []

    for x in list:
        p = Process(target=create_img, args=(x,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Done")
