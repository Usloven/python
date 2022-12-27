Candy = 31

from random import randint as rd

first = (rd(0,1))
if first==1:
    print("ходит компьютер")
else: print("ходит человек")
def hod( Candy):
    hod = int(input("введите число"))
    Candy = Candy -hod
    print (f"осталось конфет{Candy}") 
    flag = 1
    return Candy

def hod_comp(Candy):
    hod_comp = Candy%29
    if hod_comp>28:
        hod_comp = 1
    if hod_comp==0:
        hod_comp = 1    
    print(hod_comp)
    Candy = Candy -hod_comp
    print (f"осталось конфет{Candy}") 
    return Candy

while Candy>0:
    if first==1:
        Candy=hod_comp(Candy)
        flag = "comp"
        if Candy>0:
            Candy=hod(Candy)
            flag ="igrok"
        else: 
            break
    else:
        Candy=hod(Candy)
        flag ="igrok"
        if Candy>0:
            Candy=hod_comp(Candy)
            flag ="comp"
        else: 
            break
    
print (f"победил {flag}")
