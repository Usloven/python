# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

def gen_list(n):
    a = [random.randint(1, 3) for i in range(0,n)]
    return a

newlist=gen_list(10)
print(newlist)
def sum_odd (list):
    result_list = []
    for i in range (0,len(list),2):
        result_list.append(newlist[i])
    sum =0
    
    for i in  result_list:
        sum = sum + i
    return sum



print (sum_odd(newlist))   
