p1=[int(input()),int(input())]
result = 0
if p1[1]!=0 and p1[0]!=0:
    if p1[1]>0 and p1[0]>0:
        result = 1
    elif p1[0]>0 and p1[1]<0:
        result = 4
    elif p1[0]<0 and p1[1]<0:
        result = 3
    else: result = 2
else: result = 0
print (result)