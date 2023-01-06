import json
import datetime
import pandas as pd



def del_pupil():
    with open('.\HW8\pupil.json', 'r') as f:
        pup_data = json.load(f)
    uid=input('введите номер ученика')
    del pup_data[uid]
    with open('.\HW8\pupil.json', 'w') as f:
        json.dump(pup_data, f)
    input("Enter для возврата в меню")
    
def add_first_pupil():
    json_data = {}
    uid=1
   
    json_data[(uid)] = {}
    json_data[(uid)]['name'] = input("Имя:")
    json_data[(uid)]['sername'] = input("Фамилия:")
    json_data[(uid)]['f_name'] = input("Отчество:")
    json_data[(uid)]['bday'] = input("Дата рождения:")
    json_data[(uid)]['pup_class'] = input("Класс:")
    json_data[(uid)]['parent_name'] = input("ФИО:")
    json_data[(uid)]['parent_phone'] = input("телефон") 
    json_data[(uid)]['status'] = input("статус") 


    
    with open('.\HW8\pupil.json', 'w') as f:
        json.dump(json_data, f)
    input("Enter для возврата в меню")

def show_pupils():
    try:
        with open('.\HW8\pupil.json', 'r') as f:
            json_data = json.load(f)
            print(json_data)
    except:
        print ("в базе еще нет ни одной записи. Добавить ученика? да - нажмите 1, нет - нажмите любую любую другую клавишу")
        if int(input())==1:
            add_first_pupil()
        else:
            show_pupils()
            


def add_pupil():
    

    with open('.\HW8\pupil.json', 'r') as f:
        json_data = json.load(f)
    uid=len(json_data)+1
   
    json_data[uid] = {}
    json_data[(uid)]['name'] = input("Имя:")
    json_data[(uid)]['sername'] = input("Фамилия:")
    json_data[(uid)]['f_name'] = input("Отчество:")
    json_data[(uid)]['bday'] = input("Дата рождения:")
    json_data[(uid)]['pup_class'] = input("Класс:")
    json_data[(uid)]['parent_name'] = input("ФИО:")
    json_data[(uid)]['parent_phone'] = input("телефон") 
    json_data[(uid)]['status'] = input("статус") 


    
    with open('.\HW8\pupil.json', 'w') as f:
        json.dump(json_data, f)
    input("Enter для возврата в меню")
  





def fill_tabel_this_week ():
    date_now = datetime.datetime.now()

    a = date_now.timetuple()
    date_fill = date_now
    if a ==0:
        date_fill = date_now
    else: 
        delta = datetime.timedelta(days=int(a[6]))
        date_fill = date_now-delta
    print(date_fill)
    pupils_list=[]

    with open('.\HW8\pupil.json', 'r') as f:
        pupils_list = json.load(f)
    
    try:
        with open('.\HW8\log.json', 'r') as k:
            log_list = json.load(k)
            uid = max(log_list.keys())+1
    except:
        uid = 1

        
    log_file = {}
    for i in pupils_list.keys():
        log_file[uid]={}
        log_file[uid]['date'] = str(date_fill.date())
        log_file[uid]['id pupil']=i
        uid = uid+1

    with open('.\HW8\log.json', 'w') as f:
        json.dump(log_file, f)



      

def print_table ():

    try:
        with open('.\HW8\pupil.json', 'r') as f:
            pupil_data = json.load(f)
    except:print("нет данные в списке учеников")
    pupil_list = []
    

    for i in pupil_data.keys():
        pupil_list.append(pupil_data[i]['name'])
    import_data={'№ п/п':pupil_list} #импортируем имена учеников в столбец п\п
    for i in range(1,32):
        import_data[i]=day_list(i) #создаем календарь посещений
    print (import_data)
    df= pd.DataFrame(import_data)
    df.to_excel('./new1.xlsx', index=False)


def day_list(k):
    with open('.\HW8\log.json', 'r') as f:
        log_list = json.load(f)
    
    temp = []
    for i in log_list:
        
        if k == int((log_list[i]["date"])[-2:]):
            temp.append(1)
        else:
            temp.append(0)      
    return temp


