import sys
PATH = sys.argv[1]

files = [PATH+'\Cash1.txt',PATH+'\Cash2.txt',PATH+'\Cash3.txt',PATH+'\Cash4.txt',PATH+'\Cash5.txt'] # пути к файлам
print(files)
print(files[0])
till = 0
tills = []
for path in files:# беру путь файла
    with open(path) as file: # Открываю файл
        tills.append([]) # добавляю пустой массив для дальнейшего его заполнения
        for line in file:#
            tills[till].append(float(line))# каждую строку файла преобразую в флоат и добавляю в массив с индексом till в массиве tills
        till += 1 # увилечиваю индекс кассы на единицу
all_item = []# массив для сложенных значений
for item in range(len(tills[0])):#  определил длину вложенного массива
    all_item.append(tills[0][item] + tills[1][item] + tills[2][item] + tills[3][item] + tills[4][item]) # добавление суммы позиций с индексом item
print(all_item.index(max(all_item)) + 1 )# распечатал позицию максимального элемента
