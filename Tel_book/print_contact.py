# модуль печати из файла, в зависимости от выбора формата

def contact():

    n = int(input('Из какого файла вывести данные (1 или 2): '))

    if n == 1: fileName = "tel_1.txt"
    elif n == 2: fileName = "tel_2.txt"
    else: print("выбор неверен")

    with open(fileName, 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line, end = '')