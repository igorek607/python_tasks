import random


# 1. создаём список словарей

dicts = []
dicts_qty = 3
string = "abc"

for _ in range(dicts_qty):
    dictionary = {}
    keys_qty = random.randint(0, len(string))
    keys = random.sample(string, keys_qty)
    for key in keys:
        dictionary[key] = random.randint(0, 1000)
    dicts.append(dictionary)

# 2. собираем максимум + откуда он

temp_dict = {}
for i, d in enumerate(dicts, start=1):
    for k, v in d.items():
        if k not in temp_dict:
            temp_dict[k] = (v, i)
        else:
            if v > temp_dict[k][0]:
                temp_dict[k] = (v, i)

# 3. считаем сколько раз встречается ключ

occ = {}
for d in dicts:
    for k, _ in d.items():
        occ[k] = occ.get(k, 0) + 1

# 4. финальный результат
result = {}

for key, (value, idx) in temp_dict.items():
    if occ[key] == 1:
        result[key] = value
    else:
        result[f"{key}_{idx}"] = value

print(result)

