dict1 = {'a':3, 'b':5, 'c':100, 'e':10, 'd':16}
dict2 = {'a':5, 'b':4, 'c':100, 'd':6, 'e':-0}
dict3 = {'b':1, 'a':0, 'c':100, 'd':7, 'e':0, 'g':9, 'z':11}

dicts = [dict1, dict2, dict3]

# 1. Собираем все ключи
all_keys = set().union(dict1, dict2, dict3)

result = {}

# 2. Для каждого ключа ищем все значения
for key in all_keys:
    values = []  # (value, dict_number)

    num = 1
    for d in dicts:
        if key in d:
            values.append((d[key], num))
        num += 1

    # 3. Если значение лишь одно — пишем без суффикса
    if len(values) == 1:
        result[key] = values[0][0]

    else:
        # 4. Ищем максимальное value
        max_value = values[0][0]
        max_num = values[0][1]

        for value, number in values:
            if value > max_value:
                max_value = value
                max_num = number

        # добавляем суффикс _номер словаря
        result[f"{key}_{max_num}"] = max_value

print(result)