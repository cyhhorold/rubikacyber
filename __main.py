import sys
import os
from colorama import Fore, init
from time import sleep
import platform as pl
import random

sys = pl.uname()[0]

if sys == 'Linux':
    os.system('clear')
print('')
sleep(2.4)
print(Fore.YELLOW+' RUBIKA CYBER 1.3.0 ')

print('')
print(' --------------------')
print('')
sleep(2)

print(Fore.LIGHTMAGENTA_EX+' [~] Hack by Id Rubika !')
print('')

datas = input(Fore.LIGHTGREEN_EX+' USERNAME / ID-Rubika : ')
sleep(2)

print('')

print(Fore.LIGHTYELLOW_EX+'id_test : https://web.rubika.ir/#/'+datas)
print('')
sleep(3)
print(Fore.CYAN+'YES response => 200 ')

sleep(3)

print('')
print(Fore.LIGHTWHITE_EX+'Number found ...')
sleep(2)
if sys == 'Linux':
    os.system('clear')

print('')
sleep(4)
print(Fore.GREEN+'SERVICE TOE CONECTED')
print('')
print(Fore.GREEN+'respons => 200')
sleep(3)
print('')
print('START ATTACKS TO '+datas)

sleep(3)
for i in range(99999,999999):
    print(Fore.LIGHTRED_EX+'[-] Test CODE : '+Fore.WHITE+str(i)+'  =>  '+Fore.RESET+datas)
sleep(2)
print(Fore.LIGHTBLACK_EX+'---------------')
kc = random.randint(000000, 999999)
print(Fore.LIGHTGREEN_EX+'[+] Found Code : '+str(kc))

print('')

se = input(Fore.YELLOW+'exit the script ? (Y) ').casefold()

if se == 'y':
    exit()
else:
    se == 'n'
    os.system('python3 rubikacyber.py')

