pole = [["*","*","*"],["*","*","*"],["*","*","*"]]

def print_matrix(list):
    for a in list:
        print(" ".join(a))
win = ""
result = {"temp_x_row":[],"temp_x_line" :[],"temp_O_row":[], "temp_O_line":[]}
history = {}

print_matrix(pole)
def kr_hod():
    krestik_hod=list(map(int, input("Крестик:введите номер строки и номер столбца:например 0 2\n").split(" ")))
    (pole[krestik_hod[0]])[krestik_hod[1]]="X"
    print_matrix(pole)
    result["temp_x_row"].append(krestik_hod[0])
    result["temp_x_line"].append(krestik_hod[1])

def nol_hod():
    nolik_hod = list(map(int, input("Нолик:введите номер строки и номер столбца:например 0 2\n").split(" ")))
    (pole[nolik_hod[0]])[nolik_hod[1]]="O"
    print_matrix(pole)
    result["temp_O_row"].append(nolik_hod[0])
    result["temp_O_line"].append(nolik_hod[1])

def Check_win():
    temp=(list(result.values()))
    for i in temp:
        for k in i:
            if i.count(k)==3:
                return "x"
    if  len(set(temp[0])) ==3 and len(set(temp[1])) ==3:
        return 'x'
    elif  len(set(temp[2])) ==3 and len(set(temp[3]))==3:
        return '0'

    else: return ""
    

for i in range(1,8):
    while win == "":
        if win =="":
            kr_hod()
            win=Check_win()
        if win =="":
            nol_hod()
            win=Check_win()
        else: break
print (f"выиграла команда {win}")