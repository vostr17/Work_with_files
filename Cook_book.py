def cook_book(receipts: list) -> dict:
        """Функция, которая переводит список строк с рецептами в словарь,
        где ключ - название блюда, значение - список словарей с ингредиентами
        и их количеством."""
        cook_book_ = {}  # словарь, который будет возвращён функцией
        cook_ingredients = 0  # количество ингредиентов в блюде
        cook_name = ''  # наименование блюда для ключа в словаре cook_book
        ingredients = []  # перечень ингредиентов и их количества для значений в словаре cook_book
        ingredient = {}  # словарь для каждого ингредиента с наименованием, количеством, шт.
        count = 0  # счётчик строк

        for line in receipts:

            if line[:-1].isdigit():
                cook_ingredients = int(line)

            if line.find('|') == -1 and len(line) > 2:
                cook_name = line[:-1]

            if line.find('|') != -1:
                ingredient['ingredient_name'] = line[:line.find('|') - 1]
                line = line[line.find('|') + 2:]
                ingredient['quantity'] = int(line[:line.find('|') - 1])
                line = line[line.find('|') + 2:]
                ingredient['measure'] = line[:-1]
                ingredients.append(ingredient)
                ingredient = {}

            if len(line) == 1 or count == len(receipts) - 1:
                cook_book_[cook_name] = ingredients
                cook_name = ''
                ingredients = []
            count += 1
        return cook_book_

def get_shop_list_by_dishes(cook_book_list: dict, dishes: list, person_count: str) -> list:
        """Функция, которая выдаёт словарь с названием ингредиентов
        и их количеств для блюда."""
        shop_list_by_dishes = {} # словарь, который будет возвращён функцией
        quantities = {} # словарь с количеством конкретного ингредиента
        ingredients = [] # лист словарей с ингредиентами

        for dish in dishes:
            if dish in cook_book_list:
                ingredients = cook_book_list.get(dish)
            else:
                raise TypeError('Данного блюда нет в кулинарной книге')

            for ingredient in ingredients:
                quantities['measure'] = ingredient['measure']
                quantities['quantity'] = ingredient['quantity'] * person_count

                if ingredient['ingredient_name'] not in shop_list_by_dishes:
                    shop_list_by_dishes[ingredient['ingredient_name']] = quantities
                else:
                    quantities['quantity'] += ingredient['quantity'] * person_count
                    shop_list_by_dishes[ingredient['ingredient_name']] = quantities
                quantities = {}

        return shop_list_by_dishes

# Задача 1. Создание словаря с кулинарной книгой из файла recipes.txt
with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_list = file.readlines()
cook_book_list_ = cook_book(cook_list)
print(cook_book_list_)

# Задача 2. Создание списков ингредиентов с их количеством для приготовления блюд
print(get_shop_list_by_dishes(cook_book_list_,['Омлет', 'Фахитос', 'Запеченный картофель'], 7))
# Попытка создания списка ингредиентов для блюда, которого нет в кулинарной книге
# print(get_shop_list_by_dishes(cook_book_list_,['Солянка', 'Утка по-пекински'], 2))
