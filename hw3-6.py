# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
#  (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

import random
def gen_list(n):
    a = [random.randint(1, 9) for i in range(0,n)]
    return a

array = gen_list(6)
print(array)
def change_pl(n,list):
    if n>0:
        for i in range(n):
            list.insert(0,list.pop())
    else:
        for i in range(-n):
            temp =list.pop(0)
            list.append(temp)
    return list
change_pl(-2,array)
print(array)
