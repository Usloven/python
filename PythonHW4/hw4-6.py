import codecs
data = codecs.open('input1.txt','r','utf-8')
n_list= data.readlines()
d = dict()
for i in n_list:
    x=i.split()
    if x[0] not in d.keys():
       d[x[0]] = {x[1]}
    else:
        d[x[0]].add(x[1])
    if x[1] not in d.keys():
        d[x[1]]={x[0]}
    else:
        d[x[1]].add(x[0])
print ('ДРУЗЬЯ 1 УРОВЕНЬ')
print(d)
res = dict()
for x in d:
    for y in d[x]:
        if x not in res.keys():
            res[x]={k for k in d[y]}
        else:
            res[x].union({k for k in d[y]})
print ('ДРУЗЬЯ 2 УРОВЕНЬ')
print(res)
for i in res: 
    if i in res[i]:
      res[i].discard(i)  

print(res)
data.close()