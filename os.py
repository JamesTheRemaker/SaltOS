import time
import os

print("""


███████████████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄███─▄─▄─█▀▀▀▀▀██─▄▄─█─▄▄▄▄███─▄▄▄▄█▄─█─▄█─▄▄▄▄█─▄─▄─█▄─▄▄─█▄─▀█▀─▄█
█▄▄▄▄─██─▀─███─██▀███─██████████─██─█▄▄▄▄─███▄▄▄▄─██▄─▄██▄▄▄▄─███─████─▄█▀██─█▄█─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀""")
print("""
[1] Continue With Setup
[2] Ive Already Done Setup
""")
setup = input("[?]: ")
if setup == "1":
    name = input(str("Please Enter Your Username To Be Displayed: "))
    pas = input(str("Please enter your password to login: "))
    lines = [name]
    with open('user/username.txt', 'w') as f:
        f.writelines(lines)
    
    lines2 = [pas]
    with open('user/password.txt', 'w') as f:
        f.writelines(lines2)
    print("Setup Complete.")
    input("Press Enter To Close Window: ")

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Please Enter The Password To " + l_n + ": "))
    if login == l_p:
        os.startfile('main.py')
    else:
        print("Wrong Password!")