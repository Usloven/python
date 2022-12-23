# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

def gen_list(n):
    a = [float(format(random.random()*random.randint(1,9), '.2f')) for i in range(0,n)]
    return a

def fl_num(i):
    return i%1

newlist=gen_list(10)
print(newlist)
def maxminfloat (list):
    
    maxfl = 0
    minfl =fl_num(list[0])
    for i in range (0,len(list)):
        if fl_num(list[i])>maxfl:
            maxfl=fl_num(list[i])
        elif fl_num(list[i])<minfl:
            minfl= fl_num(list[i])
    print (maxfl)
    print (minfl)
    return maxfl-minfl



print (maxminfloat(newlist))   
