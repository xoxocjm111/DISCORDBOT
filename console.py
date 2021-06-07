import os
import time
from termcolor import colored

os.system('clear')

print(colored("""
 ,'|"\   ,---.      ,--,  .---.  .-. .-.   .---.  .---.  ,-.    ,---.   
 | |\ \  | .-.\   .' .') / .-. ) |  \| |  ( .-._)/ .-. ) | |    | .-'   
 | | \ \ | |-' \  |  |(_)| | |(_)|   | | (_) \   | | |(_)| |    | `-.   
 | |  \ \| |--. \ \  \   | | | | | |\  | _  \ \  | | | | | |    | .-'   
 /(|`-' /| |`-' /  \  `-.\ `-' / | | |)|( `-'  ) \ `-' / | `--. |  `--. 
(__)`--' /( `--'    \____\)---'  /(  (_) `----'   )---'  |( __.'/( __.' 
        (__)             (_)    (__)             (_)     (_)   (__)     
""", "red"))

print('[1] Discord Bot')
print('[2] Exit')
print('')

usrImpt = input('db console > ')

if usrImpt == '1':
  os.system('python3 discordapiyes.py')

if usrImpt == '2':
  exit()
