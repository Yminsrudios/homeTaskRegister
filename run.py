nameUser = ""
pasworldUser = ""
register = False
menyPos = ""

print('hello new user, what is your name?')
nameUser = input()
print('hello', nameUser)
print('So what is your password?')
pasworldUser = input()
register = True
print('ok')

# Сохранение данных в файл infoUser.txt
with open("infoUser.txt", "w") as f:
    f.write(f"Name: {nameUser}\n")
    f.write(f"Password: {pasworldUser}\n")
print("Данные сохранены в файле infoUser.txt")

def mainMeny():
    global menyPos
    print('Welcom to main menu')
    print('1_profil')
    print('2_exit')
    print('3_sign up')
    menyPos = input()

def profil():
    print('this is your profile')
    print(nameUser)


def exit_program():
    print('you exit ?')


def sing():
    print('you sign up for a lost profile')
    print('soon')


if register == True:
    mainMeny()

    if menyPos == "1":
       profil()
    elif menyPos == "2":
       exit_program()
    elif menyPos == "3":
        sing()
    else:
        print('Некоректный ввод')