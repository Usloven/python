from pupils import show_pupils, add_pupil, del_pupil, fill_tabel_this_week,print_table



def menu():
    print ("""    1.Вывести список учеников
    2.внести нового ученика в базу
    3.внести или изменить данные ученика 
    4.ввести посещения за последнюю неделю
    6.подготовить отчет - табель посещений за месяц
    7.удалить запись об ученике по его uid""")
    act=int(input("Введите номер действия из списка:"))
    if act==1:
        show_pupils()
        input("для выхода в меню нажмите любую кнопку")
        menu()
    elif act==2:
        add_pupil()
        input("для выхода в меню нажмите любую кнопку")
        menu()
    elif act==4:
        fill_tabel_this_week ()
        input("для выхода в меню нажмите любую кнопку")
        menu()
    elif act==7:
        del_pupil()
    elif act==6:
        print_table ()    
    else: 
        menu()

   
   
