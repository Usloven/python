# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
def gen_list(n):
    a = [random.randint(1, 9) for i in range(0,n)]
    return a

newlist = gen_list (20)
print (newlist)
result = [i for i in newlist if newlist.count(i)<2]
print(result)