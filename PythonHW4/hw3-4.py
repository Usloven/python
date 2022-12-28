# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def dualsys (n):
    res=[]
    while  int(n/2)!=0:
        res.append(n%2)
        n=int(n/2)
    res.append(n)    
    res2 = (res[::-1])
    res3 = [str(i) for i in res2]
    result = ''.join(res3)
    return result
print(dualsys (3))

