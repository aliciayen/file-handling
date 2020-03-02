# Alicia Yen

import sys
import csv


def re_order(in_file, out_file):
    with open(in_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        header[0], header[1] = header[1], header[0]

    with open(in_file) as dict_file:
        reader = csv.DictReader(dict_file)

        with open(out_file, mode='wt') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=header)
            writer.writeheader()
            for row in reader:
                writer.writerow(row)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    re_order(in_file, out_file)
