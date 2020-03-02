# Alicia Yen

import csv


def main():
    in_file = "countryInfo.csv"
    out_file = "country_simple_info.csv"
    header = ['country', 'capital', 'population']

    with open(in_file) as csv_file:
        reader = csv.DictReader(csv_file, delimiter='\t')
        simple_info = [
            {
                'country': row['name'],
                'capital': row['capital'],
                'population': row['population']
            }
            for row in reader
        ]
        sorted_simple = sorted(
            simple_info,
            key=lambda row: int(row['population']),
            reverse=True)

        with open(out_file, mode='wt') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=header, delimiter=',')
            writer.writeheader()
            for row in sorted_simple:
                writer.writerow(row)


if __name__ == "__main__":
    main()
