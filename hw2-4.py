import random    
Num = int(input())
k = [random.randint(100,200)]
for i in range(Num):
    k.append(k[i]-2*random.randint(0,1))
print((k))

age=int(input())
index = 0
while age<k[index]:
    index=index+1
 
    
print (index+1)
