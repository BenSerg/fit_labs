def find_common_participants(first_group, second_group, sep=','):
    return sorted(set(first_group.split(sep)).intersection(set(second_group.split(sep))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

