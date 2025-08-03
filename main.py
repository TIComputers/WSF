from __help__ import cl, point
from colorama import Fore
import sys

def write() -> str:
    cl()
    s = '''    
┌─┐┌─┐┬─┐┬┌─┐┌┬┐┬┌┐┌┌─┐  
└─┐│  ├┬┘│├─┘ │ │││││ ┬  
└─┘└─┘┴└─┴┴   ┴ ┴┘└┘└─┘  
'''
    print(Fore.RED + s + Fore.RESET)
    data :str = ''''''
    while True:
        try:
            data += input(Fore.RED + "> " + Fore.RESET) + "\n"
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\nSTOP WRTING!" + Fore.RESET)
            break
    return data

def Assmble(name:str, file:str, path:str, script:bool) -> None:
    from time import sleep
    import os
    
    # -- file name --
    if name == None or name == "":
        name = "Script."
    else:
        name += "."
        
    # -- type file --
    if file == None or file == "":
        print(Fore.RED + "WARNING TYPE FILE!" + Fore.RESET)
        sys.exit()
    
    # -- file path --
    if path == None or path == "":
        path = "C:\Program Files"
        
    # -- write script --
    if script == True:
        data = write()
    else:
        data = "" 
    
    # -- name file --
    sf = name + file
    
    with open(sf , "w") as f:
        f.write(data)
        
    point("Creating file", 2)
    os.system(f"move {sf} {path}")
    print(Fore.YELLOW + f"file path:{path}" + Fore.RESET)
    sleep(0.1)
    sys.exit()