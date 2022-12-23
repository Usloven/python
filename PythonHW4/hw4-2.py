# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Simpl_mult (n):
    result =[]
    for i in range(1,10):
        if n%i==0:
            result.append(i)
    return result

k=Simpl_mult (13)
print(k)