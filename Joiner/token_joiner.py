import os; import discord; import pystyle; import time
from pystyle import Add, Colors, Colorate, Center, Write
banner1 = (f"""
  _______ ____  _  ________ _   _        
 |__   __/ __ \| |/ /  ____| \ | |       
    | | | |  | | ' /| |__  |  \| |       
    | | | |  | |  < |  __| | . ` |       
    | | | |__| | . \| |____| |\  |       
    |_|_ \____/|_|\_\______|_|_\_|_____  
      | |/ __ \_   _| \ | |  ____|  __ \ 
      | | |  | || | |  \| | |__  | |__) |
  _   | | |  | || | | . ` |  __| |  _  / 
 | |__| | |__| || |_| |\  | |____| | \ \ 
  \____/ \____/_____|_| \_|______|_|  \_\                                        
""")
text = "A Discord Token Joiner\n    By natrixdev"
x = Add.Add(banner1, text, 3)
print(Colorate.Horizontal(Colors.blue_to_purple, str(x), 1))
b = Colorate.Horizontal(Colors.green_to_white, "[+] ", 1)
c = Colorate.Horizontal(Colors.blue_to_red, "[Input] > ", 1)
print('');print('')
Write.Print(Center.XCenter("Input your Discord Server Url"), Colors.red_to_purple, interval=0.0025)
print('')
discordurl = input(Center.XCenter(str(c)))
tokens = 0
token_list = "./tokens.txt"
while True:
    tokens = tokens+1
    print(str(b) + "| New token joined | " + str(tokens)+ " joins |")
    time.sleep(0.3)
    # This is illegal, this part of the code is against Discord ToS.
    # Turn it on at your own risks. 
    # -----CODE------ #
    # for token in token_list:
    #    token.access->.then=>token.join()
    # -----CODE------ #

