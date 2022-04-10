# Cristal 2022
# Gestore dei comandi (cmdhandler)

# ____    ___   _ _   _____
# | | \  /   \ | | | / ___/
# | __/  | | |  \ /  \__ \
# | | \  \___/   |  /____/
import json
from colorama import Fore

def cmdNotFound(problem):
    print(problem)

def cmd(cmd,username):
    Fore.RESET
    #Permette al cmdhandler di accedere al nome dei comandi
    import os
    cDir = os.getcwd()+'\\Cristal'

    #Controllo del comando inserito
    with open(f'{os.getcwd()}\\source\\cmds\\files\\commands_{username}.json','r') as file:
        try:
            command = json.load(file)
            
            #if cmd == command['COUNTEXTENSION']:
            #    import cm
            #    help.help()

            if cmd[0] == command['CALC']:
                from cmds import calc
                calc.calc()
                return
            
            if cmd[0] == command['DATE']:
                from cmds import now
                now.DateAndTime.date()
                return

            if cmd[0] == command['HELP']:
                import cmds.help
                cmds.help.General.help()
                return
            
            if cmd[0] == command['NICKNAME']:
                import cmds.nickname
                name = cmds.nickname.change()
                return name

            if cmd[0] == command['TIME']:
                from cmds import now
                now.DateAndTime.time()
                return


            else:
                if cmd == ['']:
                    return
                else:
                    print(f'{Fore.WHITE}Il comando "{Fore.YELLOW + cmd[0] + Fore.WHITE}" è un comando sconosciuto')
      
        except Exception as problem:
            cmdNotFound(problem)
        