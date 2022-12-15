import random
Num = int(input())
Table= [int(random.choice([0, 1])) for x in range(Num)]
result = 0
print(Table)
for i in range(Num):
    if Table[i]<1:
        result=result+1
        
print(result)
