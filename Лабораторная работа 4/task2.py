import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(file=INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file, \
            open(file=OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        data = list(csv.DictReader(csv_file, delimiter=',', lineterminator='\n'))
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

