import json


def task(json_file: str) -> float:
    with open(file=json_file, mode='r', encoding='utf-8') as file:
        json_list = json.load(file)
        return round(sum(map(lambda x: x['score'] * x['weight'], json_list)), 3)
