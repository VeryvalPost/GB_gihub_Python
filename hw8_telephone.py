from hw8_db import* 


def main():
    workStatus = True
    while workStatus:
        print()
        menu = input("Введите: \n \
            1 - для создания пользователя \n \
            2 - для поиска \n \
            3 - для сортировки \n \
            4 - отобразить весь список \n \
            5 - изменить параметр \n \
            6 - удалить по ID \n \
            7 - выход \n")
        match menu:
            case '1':
                createNewUser()
            case '2':
                find = input("Введите параметры поиска: \n 1 - ID \n 2 - имя \n 3 - телефон \n 4 - возраст \n")
                param = input ('Введите искомый параметр: ')
                if find == "1":
                    findUserBy(param,param_num=0)
                if find == "2":
                    findUserBy(param,param_num=1)    
                if find == "3":
                    findUserBy(param,param_num=2)    
                if find == "4":
                    findUserBy(param,param_num=3)    
            case '3':
                find = input("Введите параметры сортировки: \n 1 - имя \n 2 - телефон \n 3 - возраст \n")
                if find == "1":
                    sorting(param_num=1)
                if find == "2":
                    sorting(param_num=2)    
                if find == "3":
                    sorting(param_num=3)    

            case '4':
                listAll()
            case '5':
                id = int(input("Введите ID изменения:"))
                param = int(input("Введите параметры изменения: \n 1 - имя \n 2 - телефон \n 3 - возраст \n"))
                value = input("Введите новое значение: \n")
                change(id, param,value)
            case '6':
                id = input("Введите ID для удаления:")              
            case '7':
                workStatus = False
                
main()