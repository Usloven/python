num = int(input())
result=0
if num > 0:
    for i in range(num+1):
       result=result+i

else:
    for i in range(num,0):
           result=result+i
print(result)