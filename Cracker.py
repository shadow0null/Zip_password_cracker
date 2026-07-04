import time 
from colorama import Fore ,Back ,Style ,init 
init (autoreset =True )
def startMessage ():
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")
    OOOO0OO000OO0OOOO ="love"
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :
        print (Fore .RED +'[X] Wrong Code')
        print (Fore .BLUE +''' 
   1. Go to Insta and massage 
   2. Insta ID: Shadow0null
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')#line:18
        startMessage ()
    else :#line:20
        print (Fore .GREEN +"Successfully Unlocked Tool!")
        pass 
if __name__ =="__main__":
    startMessage ()

from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint


try:
    import socks
except ModuleNotFoundError:
    os.system("pip install spcks")



clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"]

# imports
import zipfile
import os
from colored import fg, bg, attr

green = fg("green")
red = fg("red")

zipName = input("[*] Zip File: ")
pwdsFile = input("[*] Password File: ")

if os.path.exists(zipName):
    if os.path.exists(pwdsFile):
        with open(pwdsFile,'rb') as text:
            for entry in text.readlines():
                password = entry.strip()
                with zipfile.ZipFile(zipName,'r') as zf:
                    try:
                        zf.extractall(pwd=password)

                        print( green + "\n[+] Password Found!\n" + attr("reset"))

                        data = zf.namelist()[0]
                        print("Data: " + str(data))

                        data_size = zf.getinfo(data).file_size
                        print("Data Size: " + str(data_size))

                        print("Password: " + password.decode("utf-8"))

                        break
                    except:
                        print(red + "[-] Password Not Found! - " + password.decode("utf-8"))
                    pass
    else:
        print(red + "[-] Password File Not Found!")
else:
    print(red + "[-] Zip File Not Found!")


input()
