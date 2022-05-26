
from pywebio.input import  input , TEXT , PASSWORD
from pywebio.output import put_text

def user_control():
    username = input ("kulanıcı adı :" , type = TEXT)
    password = input("sifre giriniz", type=PASSWORD)

    if username =="user" and password =="1234":
        put_text("hoşgeldiniz" + username)
    else:
        put_text("hatalı sifre")


if __name__ == '__main__':
    user_control()