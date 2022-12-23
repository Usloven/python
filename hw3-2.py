# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import math
def gen_list(n):
    a = [random.randint(1, 3) for i in range(0,n)]
    return a

newList = gen_list(6)
print (newList)


def sum_first_last(list):
    result = []
    k=0
    for i in range(math.ceil((len(list)/2))):
        result.append(list[k]*(list[-k-1]))
        print(result)
        k=k+1
    return result
print(sum_first_last(newList))