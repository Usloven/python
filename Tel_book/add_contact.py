# Ввод данных в телефонный справочник

def method1(lastName, firstName, tel, comm):
    
    with open('tel_1.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n{}\n{}\n{}\n'
                    .format(lastName, firstName, tel, comm))    

def method2(lastName, firstName, tel, comm):
    with open('tel_2.txt', 'a', encoding='utf-8') as file:
        file.write('{},{},{},{}\n'
                    .format(lastName, firstName, tel, comm))  
def add():

    n = int(input('В какой формат ввести данные (1 или 2): '))

    if 1 <= n <= 2:
        lastName = input('Введите Фамилию: ')
        firstName = input('Введите Имя: ')
        tel = input('Введите Телефон: ')
        comm = input('Введите Описание: ')

        if n == 1:
            method1(lastName, firstName, tel, comm)

        elif n == 2:
            method2(lastName, firstName, tel, comm)

    else: print("выбор неверен")