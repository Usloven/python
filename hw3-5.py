# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def Fibonaci (n):
    array = [0,1]
    for i in range(2,n):
        array.append(array[i-1]+array[i-2])
    array.insert(0,1)
    for i in range(1,n-1):
            array.insert(0,array[1]-array[0])
    return array

print(Fibonaci(10))