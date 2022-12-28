phrase="пара-ра-рам рам-пам-папам па-ра-па-да"
def search_a (word):
    return word.count("а")
print(search_a(phrase))
temp=phrase.split()
res=[search_a(i) for i in temp]
t = res[0]
output = ""
for k in res:
    if k==t:
        output="Парам пам-пам"
    else:
        output="Пам парам"
print (output)

