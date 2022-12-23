# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
def gen_dualdef(k):
    data =  open(f'test{k}.txt','w')
    sign = ["+","-"]
    example = ""
    for i in range(-k,1):
        i=-i
        example = example +str(random.choice("+-"))+ str(random.randint(1, 9))+f"x**{i}"
        print(example)


    data.writelines(example+"=0")
    data.close()

gen_dualdef(3)