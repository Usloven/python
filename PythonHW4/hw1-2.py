x = [0,1]
y=[0,1]
z=[0,1]

for i in x:
    for n in y:
        for k in z:
            if -(x[i]*y[n]*z[k])==-x[i]*-y[n]*-z[k]: print ('да')
            else:print ('нет')
            