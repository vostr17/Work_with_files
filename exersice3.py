# Задача 3.
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

if len(list_1) == min([len(list_1), len(list_2), len(list_3)]):
     if len(list_2) < len(list_3):
         save_file('1.txt', list_1)
         save_file('2.txt', list_2)
         save_file('3.txt', list_3)
     else:
         save_file('1.txt', list_1)
         save_file('3.txt', list_3)
         save_file('2.txt', list_2)
elif len(list_2) == min([len(list_1), len(list_2), len(list_3)]):
    if len(list_1) < len(list_3):
        save_file('2.txt', list_2)
        save_file('1.txt', list_1)
        save_file('3.txt', list_3)
    else:
        save_file('2.txt', list_2)
        save_file('3.txt', list_3)
        save_file('1.txt', list_1)
else:
    if len(list_1) < len(list_2):
        save_file('3.txt', list_3)
        save_file('1.txt', list_1)
        save_file('2.txt', list_2)
    else:
        save_file('3.txt', list_3)
        save_file('2.txt', list_2)
        save_file('1.txt', list_1)


