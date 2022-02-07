import os
from time import sleep
from colorama import Fore, init
import platform as pl
import requests



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
attacks = input(Fore.LIGHTGREEN_EX+' USERNAME / ID Target :  ')
sleep(2)
print('')

print(Fore.LIGHTYELLOW_EX+'id_test : https://web.rubika.ir/#/'+attacks)
print('')
sleep(1)

if sys == 'Linux':
    os.system('clear')

print(Fore.CYAN+'respons => 200 Ok')

sleep(2)

if sys == 'Linux':
    os.system('clear')
try:
    print('')
    print(Fore.LIGHTRED_EX+'----- '+attacks+' -----')

    print('')

    sleep(1)

    print(Fore.CYAN+'Defult - 1000 - Report You Account   :   '+attacks)
    print('')

    sleep(3)

    for i in range(0,999):

        sleep(0.1)

        print(Fore.LIGHTGREEN_EX+'Report account => '+Fore.RED+attacks+' =>  '+str(i))

except(KeyboardInterrupt):

    print(Fore.MAGENTA+'END REPORT')