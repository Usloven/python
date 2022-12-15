
Num = int(input())
result = None
for i in range(2,Num+1):
    if Num%i==0:
        result=i
        break
print (result)
