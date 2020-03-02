# Alicia Yen

import sys
import csv


def tab_to_comma(in_file, out_file):
    with open(in_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        with open(out_file, mode='wt') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            for line in csv_reader:
                csv_writer.writerow(line)


if __name__ == "__main__":
    in_file = sys.argv[1]
    file_name, ext = in_file.rsplit('.')
    out_file = file_name + "_commas.csv"
    tab_to_comma(in_file, out_file)
