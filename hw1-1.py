a= int(input())
b= int(input())
c= int(input())
d= int(input())
f= int(input())
max =a
array= [a,b,c,d,f]
k= 0
i=0
for k in array:
    if array[i]>max:
        max = array[i]
        i=i+1
    else: i=i+1
print (max)
# # while (k < len(array)-1):
# #     if array(k)>array(k+1):
# #         max = array[k]
# #         k=k+1
# #     else: k=k+1
# # print(max)