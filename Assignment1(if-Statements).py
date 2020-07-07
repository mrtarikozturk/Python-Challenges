passwords = {"tarik" : '1234', "faruk" : '6789', "ahmet" : '3456', "mehmet" : '98765', "tahir" : '54323'}

name = input('Please, enter your name')

if name in passwords.keys():
    print(f'Hello, {name}! The password is : {passwords[name]}')
else:
    print(f'Hello, {name}! See you later.')