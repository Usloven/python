# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
#  (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.


# За формулу расчета пи взят ряд лейбница (но он начинает показвать приближение к пи только после 4000 прогонов)
def f_pi(n):
    k = 1
    temp = 0
    for i in range(1,n,2):
        temp =  temp+k*(1/i)
        k=k*-1
    return temp*4
pi=f_pi(40000000)
num = int(input())
print(round(pi, num))

# print(pi)
# def signpi(n, pi):
#     return int((pi%3)*10**n)

# print (signpi(7, pi))

# def f_pi2(n):
#     temp = 0
#     for i in range(1,n):
#         temp =  temp+(1/(i**2))
#     return ((6*temp)**0.5)
# print (f_pi2(1000))


