import os
import sys
import time
from colorama import Fore, Style

RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
END = '\033[0m'


def slowness(s):
  try:
    for w in s + '\n' :
      sys.stdout.write(w)
      sys.stdout.flush()
      time.sleep(5. / 100)
    print('\n')
#       time.sleep(1)
  except KeyboardInterrupt:
    time.sleep(1)
    slowness('Exiting =)')
    print('\n')
    sys.exit(0)

print("\n\033[1;37mGENERANDO DIRECTORIOS...\033[0;m\n")
os.system("mkdir Facebook && mkdir Instagram && mkdir Twitter && mkdir Gmail && mkdir Spotify && mkdir WordPress && mkdir Android-Login && mkdir Snapchat && mkdir Paypal && mkdir TikTok")
time.sleep(1)
os.system("clear")

def banner():

    print("\n")
    print(RED + Style.NORMAL+ "      ██████╗ ██████╗ ██╗   ██╗████████╗███████╗     ")
    print(RED + Style.NORMAL+"      ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝     ")
    print(RED + Style.NORMAL+"      ██████╔╝██████╔╝██║   ██║   ██║   █████╗       ")
    print(GREEN + Style.NORMAL+"      ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝       ")
    print(GREEN + Style.NORMAL+"      ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗     ")
    print(GREEN + Style.NORMAL+"      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝     ")
    print("")
    print(WHITE + Style.NORMAL+"""     \033[1;37m«\033[0;mEl poder del usuario radica en su ANONIMATO\033[1;37m»\033[0;m
    	              \033[0;31m【\033[0;m\033[1;37mR3LI4NT\033[0;m\033[0;31m】\033[0;m
    	""")
    print(BLUE +Style.NORMAL +"       ███████╗ ██████╗ ██████╗  ██████╗███████╗     ")
    print(BLUE +Style.NORMAL +"       ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝     ")
    print(BLUE + Style.NORMAL +"       █████╗  ██║   ██║██████╔╝██║     █████╗       ")
    print(WHITE + Style.NORMAL +"       ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝       ")
    print(WHITE + Style.NORMAL +"       ██║     ╚██████╔╝██║  ██║╚██████╗███████╗     ")
    print(WHITE + Style.NORMAL +"       ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝  \033[1;37mv1.5\033[0;m")

banner()
                                          
def menu():
    while True:
        
        print("\n")
        print("[\033[0;32m01\033[0;m] \033[1;34mFacebook\033[0;m")
        print("[\033[0;32m02\033[0;m] \033[1;35mInstagram\033[0;m")
        print("[\033[0;32m03\033[0;m] \033[1;36mTwitter\033[0;m")
        print("[\033[0;32m04\033[0;m] \033[1;33mGmail\033[0;m")
        print("[\033[0;32m05\033[0;m] \033[1;32mSpotify\033[0;m")
        print("[\033[0;32m06\033[0;m] \033[1;37mWordPress\033[0;m")
        print("[\033[0;32m07\033[0;m] \033[1;31mAndroid Login\033[0;m")
        print("[\033[0;32m08\033[0;m] \033[1;33mSnapchat\033[0;m")
        print("[\033[0;32m09\033[0;m] \033[1;36mPaypal\033[0;m")
        print("[\033[0;32m10\033[0;m] \033[1;37mTikTok\033[0;m")
        print("[\033[0;32m00\033[0;m] \033[0;31mExit\033[0;m")

        opcion = input("\n==> ")
        while opcion == "01":
            os.system("clear")
            banner()
            print("\n")
            print("[\033[1;4;34mFACEBOOK\033[0;m \033[0;4;31mATTACK TOOlS\033[0;m]")
            print("[\033[0;31m01\033[0;m] BluForce-FB")
            print("[\033[0;31m02\033[0;m] FaceBoom")
            print("[\033[0;31m03\033[0;m] Facebash")
            print("[\033[0;31m04\033[0;m] SocialBox")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            fb = input("\n==> ")
            if fb == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Facebook && git clone https://github.com/AngelSecurityTeam/BluForce-FB")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;34mEj\033[0m : cd Facebook")
                exit(0)

            elif fb == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Facebook && git clone https://github.com/Oseid/FaceBoom")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;34mEj\033[0m : cd Facebook")
                exit(0)
                

            elif fb == "03":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Facebook && git clone https://github.com/fu8uk1/Facebash")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;34mEj\033[0m : cd Facebook")
                exit(0)             

            elif fb == "04":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Facebook && git clone https://github.com/Cyb0r9/SocialBox")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;34mEj\033[0m : cd Facebook")
                exit(0)

            elif fb == "00":
                os.system("clear")
                banner(), menu()


        while opcion == "02":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;35mINSTAGRAM\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] Instainsane")
            print("[\033[0;31m02\033[0;m] Brutegram")
            print("[\033[0;31m03\033[0;m] Instagram Bruter") 
            print("[\033[0;31m04\033[0;m] InstaBurst")
            print("[\033[0;31m05\033[0;m] InstaShell")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            ig = input("\n==> ")
            if ig == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Instagram && git clone https://github.com/umeshshinde19/instainsane")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;35mEj\033[0m : cd Instagram")
                exit(0)


            elif ig == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Instagram && git clone https://github.com/Err0r-ICA/Brutegram")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                time.sleep(0.9)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;35mEj\033[0m : cd Instagram")
                exit(0)

            elif ig == "03":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Instagram && git clone https://github.com/Bitwise-01/Instagram-")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                time.sleep(0.9)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;35mEj\033[0m : cd Instagram")
                exit(0)
              

            elif ig == "04":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Instagram && git clone https://github.com/nuriyadin/InstaBurst")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                time.sleep(0.9)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;35mEj\033[0m : cd Instagram")
                exit(0)


            elif ig == "05":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Instagram && git clone https://github.com/maxrooted/instashell")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                time.sleep(0.9)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;35mEj\033[0m : cd Instagram")
                exit(0)


            elif ig == "00":
                os.system("clear")
                banner(), menu()


        while opcion == "03":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;36mTWITTER\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] TweetShell")
            print("[\033[0;31m02\033[0;m] TwitterSniper")
            print("[\033[0;31m03\033[0;m] Brute Force Twitter") 
            print("[\033[0;31m04\033[0;m] Pulse")
            print("[\033[0;31m05\033[0;m] 0xTBF")
            print("[\033[0;31m06\033[0;m] TWTBOOM")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            tw= input("\n==> ")
            if tw == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Twitter && git clone https://github.com/Ib-uth/tweetshell")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Twitter")
                exit(0)

            elif tw == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Twitter && git clone https://github.com/abdallahelsokary/TwitterSniper")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Twitter")
                exit(0)

            elif tw == "03":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Twitter && git clone https://github.com/0xfff0800/Brute-Forc-Twitter-")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Twitter")
                exit(0)                

            elif tw == "04":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Twitter && git clone https://github.com/Bitwise-01/Pulse-")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Twitter")
                exit(0)

            elif tw == "05":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Twitter && git clone https://github.com/EbrahimAlasaad/0xTBF")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Twitter")
                exit(0)    

            elif tw == "06":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Twitter && git clone https://github.com/Oseid/TWTBOOM")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Twitter")
                exit(0)

            elif tw == "00":
                os.system("clear")
                banner(), menu()


        while opcion == "04":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;33mGMAIL\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] Brute Force Gmail")
            print("[\033[0;31m02\033[0;m] Gmail Hack")
            print("[\033[0;31m03\033[0;m] GmailBruterV2") 
            print("[\033[0;31m04\033[0;m] Brutal-FX")
            print("[\033[0;31m05\033[0;m] GmailUnlocked")
            print("[\033[0;31m06\033[0;m] Gm-Hack")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            gm= input("\n==> ")
            if gm == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Gmail && git clone https://github.com/Matrix07ksa/Brute_Force")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Gmail")
                exit(0)

            elif gm == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Gmail && git clone https://github.com/Ha3MrX/Gemail-Hack")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Gmail")
                exit(0)

            elif gm == "03":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Gmail && git clone https://github.com/DEMON1A/GmailBruterV2")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Gmail")
                exit(0)                

            elif gm == "04":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Gmail && git clone https://github.com/Lon3r-101/Brutal-FX")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Gmail")
                exit(0)

            elif gm == "05":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Gmail && git clone https://github.com/hybridious/GmailUnlocked")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Gmail")
                exit(0)    

            elif gm == "06":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Gmail && git clone https://github.com/Background-Sajjad/Gm-Hack")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Gmail")
                exit(0)

            elif gm == "00":
                os.system("clear")
                banner(), menu()

        
        while opcion == "05":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;32mSPOTIFY\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] WSPOTIFY")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")
            
            sp= input("\n==> ")
            if sp == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Spotify && git clone https://github.com/wuseman/WSPOTIFY")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;32mEj\033[0m : cd Spotify")
                exit(0)

            elif sp == "00":
                os.system("clear")
                banner(), menu()


        while opcion == "06":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;37mWORDPRESS\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] WPForce")
            print("[\033[0;31m02\033[0;m] BruteWP")
            print("[\033[0;31m03\033[0;m] WordBrutePress") 
            print("[\033[0;31m04\033[0;m] WordPress Brute Force")
            print("[\033[0;31m05\033[0;m] XBruteForcer")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            wp= input("\n==> ")
            if wp == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd WordPress && git clone https://github.com/n00py/WPForce")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;37mEj\033[0m : cd WordPress")
                exit(0)

            elif wp == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd WordPress && git clone https://github.com/samuelproject/BruteWP")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;37mEj\033[0m : cd WordPress")
                exit(0)

            elif wp == "03":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd WordPress && git clone https://github.com/claudioviviani/wordbrutepress")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;37mEj\033[0m : cd WordPress")
                exit(0)               

            elif wp == "04":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd WordPress && git clone https://github.com/recepgunes1/WordPress-Brute-Force")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;37mEj\033[0m : cd WordPress")
                exit(0)

            elif wp == "05":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd WordPress && git clone https://github.com/Moham3dRiahi/XBruteForcer")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;37mEj\033[0m : cd WordPress")
                exit(0)    

            elif wp == "00":
                os.system("clear")
                banner(), menu()

        
        while opcion == "07":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;31mANDROID-LOGIN\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] Android-PIN-Bruteforce")
            print("[\033[0;31m02\033[0;m] AndroidPINCrack")
            print("[\033[0;31m03\033[0;m] WBRUTER-ANDROID") 
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            al= input("\n==> ")
            if al == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Android-Login && git clone https://github.com/urbanadventurer/Android-PIN-Bruteforce")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;31mEj\033[0m : cd Android-Login")
                exit(0) 

            elif al == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Android-Login && git clone https://github.com/PentesterES/AndroidPINCrack")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;31mEj\033[0m : cd Android-Login")
                exit(0) 

            elif al == "03":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Android-Login && git clone https://github.com/papusingh2sms/WBRUTER-ANDROID")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;31mEj\033[0m : cd Android-Login")
                exit(0)                    

            elif al == "00":
                os.system("clear")
                banner(), menu()

            
        while opcion == "08":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;33mSNAPCHAT\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] SnapBrute")
            print("[\033[0;31m02\033[0;m] Snap0x")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            sc= input("\n==> ")
            if sc == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Snapchat && git clone https://github.com/u0pattern/SnapBrute")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Snapchat")
                exit(0)

            elif sc == "02":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Snapchat && git clone https://github.com/0xfff0800/snap0x")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;33mEj\033[0m : cd Snapchat")
                exit(0)

            elif sc == "00":
                os.system("clear")
                banner(), menu()


        while opcion == "09":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;36mPAYPAL\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] Brute force paypal")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            pyl= input("\n==> ")
            if pyl == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd Paypal && git clone https://github.com/vv1ck/Brute-force-paypal")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;36mEj\033[0m : cd Paypal")
                exit(0)

            elif pyl == "00":
                os.system("clear")
                banner(), menu()


        while opcion == "10":
            os.system("clear")
            banner()
            print("\n")            
            print("[\033[1;4;37mTIKTOK\033[0;m \033[0;4;31mATTACK TOOLS\033[0;m]")
            print("[\033[0;31m01\033[0;m] Brute force Tiktok")
            print("[\033[0;32m00\033[0;m] \033[0;32mBack\033[0;m")

            pyl= input("\n==> ")
            if pyl == "01":
                print(GREEN + Style.BRIGHT +"\nClonando repositorio..."+ WHITE + Style.NORMAL)
                os.system("cd TikTok && git clone https://github.com/vv1ck/Brute-force-Tiktok")
                print(GREEN + Style.BRIGHT +"Completado ✔"+ WHITE + Style.NORMAL)
                if input("\n\033[1;37m¿Desea salir?\033[0;m \033[0;m[\033[0;32my\033[0;m / \033[0;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
                    os.system("clear")
                    banner()
                    menu()
                time.sleep(0.9)
                os.system("clear")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mls\033[0m : Ver repositorios clonados \033[1;36m]─┐\033[0m\n")
                print("\n\033[1;36m┌─[\033[0m \033[1;33mcd\033[0m : Cambiar de directorio \033[1;36m]─┐\033[0m")
                print("    \033[1;37mEj\033[0m : cd TikTok")
                exit(0)

            elif pyl == "00":
                os.system("clear")
                banner(), menu()                            


        while opcion == "00":
            slowness("\n\033[1;37m>>\033[0;m \033[1;33mGracias por probar este script, vuelve pronto! \033[1;37m<<\033[0;m")
            time.sleep(0.5)
            sys.exit(0)

menu()
