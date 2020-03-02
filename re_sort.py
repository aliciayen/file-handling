# Alicia Yen

import sys
import csv


def re_sort(in_file, out_file):
    with open(in_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

    with open(in_file) as dict_file:
        reader = csv.DictReader(dict_file)
        sorted_csv = sorted(reader, key=lambda row: row[header[1]])

        with open(out_file, mode='wt') as new_file:
            writer = csv.DictWriter(new_file, reader.fieldnames)
            writer.writeheader()
            for row in sorted_csv:
                writer.writerow(row)


if __name__ == "__main__":
    in_file = sys.argv[1]
    file_name, ext = in_file.rsplit('.')
    out_file = file_name + "_sort.csv"
    re_sort(in_file, out_file)
