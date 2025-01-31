from pprint import pprint


# Открытие файла и чтение строки
f = open("путь_до_файла.txt")
string = f.readline().replace("\n", "")


# Составление частотного анализа
simbols = {}
for s in string:
    if s in simbols:
        simbols[s] += 1
    else:
        simbols[s] = 1


# Создание формы для таблицы пар. Первый столбец заполнен
arr = [list(sorted(simbols.items(), key=lambda x: x[1], reverse=False))]
for _ in range(len(simbols.keys()) - 1):
    arr.append([])


# Заполнение остальных столбцов таблицы. Хуй знает как это тут работат я уже забыл
for i in range(1, len(arr)):
    j = 0

    flag = False
    while True:
        if j >= len(arr[i - 1]):
            break

        if i == len(arr[i]) + 1:
            arr[i].append(
                (
                    f"{arr[i-1][i-1][0]}{arr[i-1][i][0]}",
                    arr[i - 1][i][1] + arr[i - 1][i - 1][1],
                )
            )
            j += 1
        elif i > len(arr[i - 1]) and not flag:
            arr[i].append(
                (
                    f"{arr[i-1][j if j < len(arr[i-1]) else -1][0]}{arr[i-1][j+1 if j+1 < len(arr[i-1]) else -1][0]}",
                    arr[i - 1][j if j < len(arr[i - 1]) else -1][1]
                    + arr[i - 1][j + 1 if j + 1 < len(arr[i - 1]) else -1][1],
                )
            )
            j += 1
            flag = True
        else:
            arr[i].append(arr[i - 1][j])

        j += 1


# Таблица пар
pprint(arr)
print("_" * 100)


bin_arr = [[] for _ in range(len(simbols.keys()))]
bin_arr[-1].append(("Корень",))
for i in range(len(arr) - 1):
    for j in range(len(arr[i])):
        bin_arr[i].append((arr[i][j][0], j % 2))


# Бинарная таблица
pprint(bin_arr)
print("_" * 100)


bin_simbols = {i: "" for i in simbols.keys()}
for i in range(len(arr) - 1):
    for j in range(len(arr[i])):
        for simbol in list(bin_simbols.keys()):
            if simbol in arr[i][j][0]:
                bin_simbols[simbol] = bin_simbols[simbol] + str(bin_arr[i][j][1])


# Объявление кодов каждому символу
pprint(bin_simbols)
print("_" * 100)
