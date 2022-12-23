import random
def gen_dualdef(k):
    data =  open(f'test{k}.txt','w')
    sign = ["+","-"]
    example = ""
    for i in range(-k,1):
        i=-i
        example = example +str(random.choice("+-"))+ str(random.randint(1, 9))+f"x**{i}"
       


    data.writelines(example)
    data.close()

gen_dualdef(3)
gen_dualdef(4)

def sum_polynom(text1,text2):
    data=open(text1,'r')
    data1=open(text2,'r')
    data3 = open('test.txt','w')
    data3.writelines(data.readline()+ data1.readline())

sum_polynom("test3.txt", "test4.txt")