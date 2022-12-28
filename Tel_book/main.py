
import add_contact
import print_contact

n = int(input('Выберите действие:\n\
    1: Вывод контактов\n\
    2: Добавить контакт\n\
    '))

if   n == 1:
    print_contact.contact()
elif n == 2:
    add_contact.add()
else: print("выбор неверен")