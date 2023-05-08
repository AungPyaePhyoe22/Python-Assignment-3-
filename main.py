
db={}

global email_exit
email_exit=-1

def Check_Ascii(data):
    Special = 32
    Special_character = [' ','!','"','#','$','%','&','(',')','*','+',',','=','-','/']
    Number = ['0','1','2','3','4','5','6','7','8','9']
    Captial = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    Small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    Special_character1 = [':',';','<','=','>','?','@']
    Special_character2 = ['[',']','^','_']
    Special_character3 = ['{','|','}','~']
    Special_character.insert(7,"'")
    Special_character2.append('`')
    Special_character2.insert(1,'\\')
#    print(Special_character)
#    print(Special_character2)
#    print(Special_character3)
# append lokk fo 2 khu kyn
    A_Number = []
    A_Special_character = []
    A_Special_character1 = []
    A_Captial_Character = []
    A_Special_character2 = []
    A_Small_Character = []
    A_Special_character3 = []

    for i in range(0,16):
         A_Special_character.append(Special)
         if Special_character[i] == data:
             data = A_Special_character[i]
         Special +=1

#    print(A_Special_character)
    for i in range(0,10):
         A_Number.append(Special)
         if Number[i] == data:
             data = A_Number[i]
         Special +=1
#    print(A_Number)
    for i in range(0,7):
         A_Special_character1.append(Special)
         if Special_character1[i] == data:
             data = A_Special_character1[i]
         Special +=1
#    print(A_Special_character1)
    for i in range(0,26):
         A_Captial_Character.append(Special)
         if Captial[i] == data:
             data = A_Captial_Character[i]
         Special += 1
#    print(A_Captial_Character)
    for i in range(0, 6):
        A_Special_character2.append(Special)
        if Special_character2[i] == data:
            data = A_Special_character2[i]
        Special += 1
#    print(A_Special_character2)
    for i in range(0, 26):
        A_Small_Character.append(Special)
        if Small[i] == data:
            data = A_Small_Character[i]
        Special += 1
#    print(A_Small_Character)
    for i in range(0, 4):
        A_Special_character3.append(Special)
        if Special_character3[i] == data:
            data = A_Special_character3[i]
        Special += 1
#    print(A_Special_character3)

    return data


def main_sector():
    main_option =input("Press 1 to Register:\nPress 2 to Login\nPress 3 Exit:")
#    print(Check_Ascii(main_option))
    if ((Check_Ascii(main_option)>48) and (Check_Ascii(main_option)<57)):
        if Check_Ascii(main_option)== 49:
           registration()
        elif Check_Ascii(main_option)== 50:
            login()
        elif Check_Ascii(main_option)== 51:
            recording_all_data()
            exit(1)
        else:
           print("Invalid Option")
           main_sector()
    else:
        print("Invalid!\nPlease enter only numbers")
        main_sector()

def main_sector1():
    main_option =input("Press 1 to Register:\nPress 2 to Login\nPress 3 Exit:")
#    print(Check_Ascii(main_option))
    if ((main_option>=str(0)) and (main_option)<=str(9)):
        if main_option== str(1):
           registration()
        elif main_option== str(2):
            login()
        elif main_option== str(3):
            recording_all_data()
            exit(1)
        else:
           print("Invalid Option")
           main_sector1()
    else:
        print("Invalid!\nPlease enter only numbers")
        main_sector1()
def registration():

    user_email = input("Enter your email:")
    email_get = Email_exit(user_email)

    if email_get!=None:
        print("Email already exit:")
        registration()
    else:
        user_name = input("Enter your username:")
        user_password = input("Enter your password:")
        user_phone = int(input("Enter your phone:"))
        user_age = int(input("Enter your age:"))

        id = len(db)

        to_insert = {id: {"email": user_email,"u_name":user_name, "password": user_password,"phone":user_phone,"age":user_age}}
        db.update(to_insert)
        print("Registred!")


def login():
    user_found=-1;
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")


    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"]==l_user_password:

            user_found=i
    if user_found!=-1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("Not Found ")

def user_profile(user_found):
    print("Welcome:",db[user_found]["u_name"])

    option =input("Press 1 to exit\nPress 2 to update data\nPress 3 to go back")
    if option == str(1):
        recording_all_data()
    elif option == str(2):
        update_data(user_found)
    elif option == str(3):
        main_sector1()
    else:
        print("Invalid!")
        user_profile(user_found)

def update_data(index):
    print("This is update data sector!")
    option = input("Press A to update email\nPress B to update name\nPress C to update password\nPress D to update phone\nPress E to update age")
    if option == str('A'):

        up_email = input("Enter you new email")
        email_get = Email_exit(up_email)

        if email_get != None:
            print("Email already exit:")
            update_data(index)
        else:
            db[index]["email"] = up_email
            print("Updated!")

    elif option == str('B'):

        up_name = input("Enter your new name")
        db[index]["u_name"] = up_name
        print("Updated!")

    elif option == str('C'):

        up_pass = input("Enter your new password")
        db[index]["password"] = up_pass
        print("Updated!")

    elif option == str('D'):

        up_ph = input("Enter your new phone")
        db[index]["phone"] = up_ph
        print("Updated!")

    elif option == str('E'):

        up_age = input("Enter your new age")
        db[index]["age"] = up_age + '\n'
        print("Updated!")

    else:
        print("INvalid")
        update_data(index)

def Email_exit(email):

    lenght = len(db)
    for i in range(lenght):
        if db[i]["email"] == email:

            return i

def recording_all_data():
    with open("ass.txt", 'w') as dbfile:
        for i in range(len(db)):
            email = db[i]["email"]
            user_name = db[i]["u_name"]
            password = db[i]["password"]
            phone = db[i]["phone"]
            age = db[i]["age"]
            total_user_data = email + ' ' + user_name + ' ' + password + ' ' + str(phone) + ' ' + str(age)

            dbfile.write(total_user_data)


def loading_all_data():
    with open("ass.txt",'r') as dbfile:
        datas=dbfile.readlines()
        for one in datas:
            oneData = one.split(" ")

            id = len(db)
            data_form = {id:{"email":oneData[0],"u_name":oneData[1],"password":oneData[2],
                             "phone":oneData[3],"age":oneData[4]
                             }}
            db.update(data_form)

if __name__ == '__main__':
    loading_all_data()
    print(db)
    while True:
       main_sector1()
#     print(Check_Ascii(')'))