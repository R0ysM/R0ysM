import json
from colorama import Fore
class General:
    def help():
        import os
        cDir = os.getcwd()
        os.chdir(f'{cDir}\\cmds\\files\\')
        with open('commands.json','r') as file:
            l = json.load(file)
            for i in l:
                print(f'{Fore.WHITE + l[i].upper()}')
        os.chdir(cDir)
    
    def help_detailed():
        #Qui verranno date informazioni sulla sintassi dei comandi
        pass

class Specific:
    # Diverse funzioni spiegeranno come usare determinati comandi, e a cosa servono con degli esempi visivi
    pass