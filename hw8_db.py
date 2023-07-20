import os.path

id = 0

def countId():
    
    check_file = os.path.exists('db.txt')
    if check_file:
        with open('db.txt', 'r', encoding='UTF-8') as file:
            strCount = file.readlines()
            count = 0
            for i in strCount:
                count +=1 
        return count
    else:
        with open('db.txt', 'a' ):
            pass
        return 0

def createNewUser():
    global id
    id = str(countId() + 1)
    name = input ('Введите имя пользователя: ')
    tel = input ('Введите телефон: ')
    age = input ('Введите возраст: ')
    
    with open('db.txt', 'a' , encoding='UTF-8') as file:
            dbCreate = file.write(id+';'+name+';'+tel+';'+age+'\n')
    with open('db.txt', 'r', encoding='UTF-8') as file:
        strCount = file.readlines()
        print(strCount) 
    
def findUserBy(param,param_num):
    with open('db.txt', 'r', encoding='UTF-8') as file:
        strCount = file.readlines()
        for row in strCount:
            if param in row.split(';')[param_num]:
                print(row)
                
def listAll():
    with open('db.txt', 'r', encoding='UTF-8') as file:
        strCount = file.readlines()
        print(" ID      NAME       TEL        AGE ")
        for row in strCount:
            listRecord = row.split(';')
            for recording in listRecord:
                print(recording, end=" ")
            print()   
            
            
def sorting(param_num):
    with open('db.txt', 'r', encoding='UTF-8') as file:
        strCount = file.readlines()
        if param_num == 1:          
            strCount.sort(key=lambda x:x.split(';')[param_num])
        else:
            strCount.sort(key=lambda x:int(x.split(';')[param_num]))   
            
        for row in strCount:
            listRecord = row.split(';')
            for recording in listRecord:
                print(recording, end=" ")
            print()   


def change(id,param, value):
    with open('db.txt', 'r', encoding='UTF-8') as file:
        strCount = file.readlines()
        writeString=[]
        for row in strCount:
            if id == int(row.split(';')[0]):
                a = row.split(';')
                if param == 1:
                    writeString.append(str(id)+';'+value+';'+a[2]+';'+a[3]) 
                if param == 2:
                    writeString.append(str(id)+';'+a[1]+';'+value+';'+a[3]) 
                if param == 3:
                    writeString.append(str(id)+';'+a[1]+';'+a[2]+';'+value)
            else:
                writeString.append(row)
    rewriteFile(writeString)            
              
         
def deleteById(id):
    with open('db.txt', 'r', encoding='UTF-8') as file:
        strCount = file.readlines()
        writeString=[]
        for row in strCount:
            if id != int(row.split(';')[0]):
                writeString.append(row)
    rewriteFile(writeString)      


def rewriteFile(writeString):
    with open('db.txt', 'w', encoding='UTF-8') as file:
        file.seek(0,0)
        for item in writeString:
            file.write(item)       