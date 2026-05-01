import random

list = []

for _ in range(100):
    a = random.randint(0, 1000)
    list.append(a)

new_list = list[:]

sorted_list = []

while new_list:
    m = min(new_list)
    i = new_list.index(m)
    a = new_list.pop(i)
    sorted_list.append(a)

chet = []
nechet = []

for x in sorted_list:
    if x % 2 == 0:
        chet.append(x)
    else:
        nechet.append(x)

avg_chet = sum(chet) / len(chet)
avg_nechet = sum(nechet) / len(nechet)

print("Среднее четных = ", avg_chet)
print("Среднее нечетных = ", avg_nechet)
