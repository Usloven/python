import codecs
data = codecs.open('input.txt','r', "utf-8")
n_list= data.readlines()
print(n_list[-1])
a = [i[0:-2] for i in n_list if i.count('\n') >0 ]
if 
print(a)