
data =  open('test2.txt','r')


# Num = list(map(lambda x:x%2==0,list(data.readline())))
newlist= (list(map(int,data.readline().split() )))
newlist = [i for i in newlist if i%2==0 ]
