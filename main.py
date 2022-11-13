import time
import os
import socket
import psutil

battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
print("""
███████████████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄███─▄─▄─█▀▀▀▀▀██─▄▄─█─▄▄▄▄███─▄▄▄▄█▄─█─▄█─▄▄▄▄█─▄─▄─█▄─▄▄─█▄─▀█▀─▄█
█▄▄▄▄─██─▀─███─██▀███─██████████─██─█▄▄▄▄─███▄▄▄▄─██▄─▄██▄▄▄▄─███─████─▄█▀██─█▄█─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀""")
print("Welcome to Salt OS, " + l_n)
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("The Current Battery Life Is: ")
print(battery.percent)
print("""
[1] To Open Google
[2] To Open Write
[3] To Open File Opener
[4] To Configure and Open BioS
[5] To Close Salt OS Safely.
""")

select = input("[?]: ")

if select == '1':
    os.startfile('browser.py')
if select == '2':
    os.startfile('write.py')
if select == '3':
    os.startfile('fileview.py')

