# text = "мылsdfа мама рамау"
# text2 = 'ма'

# i = 0
# k=0
# while text.find(text2,k)>0:
#         i = i+1
#         print(k)
#         k=text.find(text2,k)+1
# print (i)



# import random    
# M = int(input())
# k = [M]
# for i in range(M):
#     k.append(random.randint(-10,10))

# data = open('test.txt', 'a' )
# data.writelines(f"{k}")

# print(*(k))

# with open('test1.txt', 'a') as data:
#     data.write('dsfsdf')

# data = open('test1.txt', 'r' )
# for i in data:
#     print(i)


# data.close()



import requests
from bs4 import BeautifulSoup

url = 'https://alestech.ru/factory/512-arktik-vud'
response = requests.get(url)
text1 = response.text
soup = BeautifulSoup(text1, 'lxml')
print (soup)