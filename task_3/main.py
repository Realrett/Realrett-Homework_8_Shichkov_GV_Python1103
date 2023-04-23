
# 3. Задание на закрепление знаний по модулю yaml.
#  Написать скрипт, автоматизирующий сохранение данных
#  в файле YAML-формата.
# Для этого:

# Подготовить данные для записи в виде словаря, в котором
# первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа —
# это целое число с юникод-символом, отсутствующим в кодировке
# ASCII(например, €);

# Реализовать сохранение данных в файл формата YAML — например,
# в файл file.yaml. При этом обеспечить стилизацию файла с помощью
# параметра default_flow_style, а также установить возможность работы
# с юникодом: allow_unicode = True;

# Реализовать считывание данных из созданного файла и проверить,
# совпадают ли они с исходными.

import yaml

data = {"list": [1, 2, 3],
        "integer": 42,
        "dict": {1: "Σ", 2: "Ψ", 3: "Ω"}
        }

with open("my_yaml.yaml", "w", encoding="utf-8") as file_stream:
    yaml.dump(data, file_stream, sort_keys=False, allow_unicode=True,
              default_flow_style=True)

with open("my_yaml.yaml", encoding="utf-8") as file_stream:
    print(file_stream.read())

