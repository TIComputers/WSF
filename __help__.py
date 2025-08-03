from platform import system
from colorama import Fore
from time import sleep
import os

# -- clear Terminal ---
def cl() -> None:
    if system() == "Windows":
        cl = os.system("cls")
    else:
        cl = os.system("clear")
        
# -- ... ---    
def point(arg:str, time:int) -> None:
    if arg == "" or arg == None:
        arg = ""
    for i in range(time):
        for j in range(1,4):
            print(f"\r{arg}{"." * j}", end="")
            sleep(0.3)

# -- help menu --             
def __help__() -> None:
    point("", 1)
    cl()
    a = Fore.RED + f'''
    
    
    |                 |                ┓ ┏┏┓┏┓
    |!               !|                ┃┃┃┗┓┣ 
    |!               !|                ┗┻┛┗┛┻
    |1               1| 
    |@               @|                 {Fore.WHITE}-h    Display All Tools                                     {Fore.RED}
    |@!             !@|                 {Fore.WHITE}-u    Updata Program                                        {Fore.RED}
    |@!             !@|                 {Fore.WHITE}-a    Assmble File                                          {Fore.RED}
    |@@             @@|                 {Fore.WHITE}-t    Select Type File                                      {Fore.RED}
    |@!@           @!@|                 {Fore.WHITE}-w    Write Scritpt File                                    {Fore.RED}
      |@!@       @!@|                   {Fore.WHITE}-s    Save File Path                                        {Fore.RED}
        |@!@   @!@|                     {Fore.WHITE}-n    Name file                                             {Fore.RED}
          |@!@!@|                    
           _|@|_                      
         _|@| |@|_                   
       _|@|     |@|_                
      |@|_       _|@|                 
        |@|_   _|@|               
          |@|_|@|                      
            |@|   
            
        
        ''' + Fore.RESET
    print(a)
    

    

