# Задача 3.
from operator import itemgetter

with open('exersice3/1.txt', 'r', encoding='utf-8') as file:
    list_1 = file.readlines()

with open('exersice3/2.txt', 'r', encoding='utf-8') as file:
    list_2 = file.readlines()

with open('exersice3/3.txt', 'r', encoding='utf-8') as file:
    list_3 = file.readlines()

def save_file(file_name: str, content: list):
    """Функция записи информации в файл в соответствии с заданием 3."""
    with open('exersice3/result.txt', 'a', encoding='utf-8') as file:
        file.write(file_name + '\n')
        file.write(str(len(content)) + '\n')
        file.writelines(content)
        file.write('\n')
list_files = [{'file_name': '1.txt', 'len': len(list_1), 'info': list_1}, {'file_name': '2.txt', 'len': len(list_2), 'info': list_2}, {'file_name': '3.txt', 'len': len(list_3), 'info': list_3}] # список словарей, содержащих имя файла и количество строк в нём
list_files = sorted(list_files, key=itemgetter('len'))

for i in list_files:
    save_file(i['file_name'], i['info'])

print("Файл 'result.txt' успешно записан." )

