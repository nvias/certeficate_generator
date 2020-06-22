import csv
import os
from pathlib import Path

from certificate_generator import certificat


def load_names(file):
    with open(file, mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        list2 = [row.split()[0] for row in csv_file]
        print(list2)
        return list2


if __name__ == "__main__":
    list = load_names(r'C:\Users\David\Documents\list.csv')

    if not os.path.exists("\\output"):
        os.makedirs("\\output")

    for x in list:
        img = certificat(x)
        path = Path("\\output\\" + "certificat_" + x + ".png")
        img.save(path.as_posix())  # for testing purposes
