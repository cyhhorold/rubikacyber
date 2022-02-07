from time import sleep
import cowsay
from colorama import Fore, init
import os
import platform as pl

sysuse = pl.uname()[0]
def cleardata():
	if sysuse == 'Linux':
			os.system('clear')

cleardata()

init()

banner = cowsay.trex('Drcyber')

sleep(2)

print(Fore.LIGHTYELLOW_EX+'''Hello my friend

Our team script is one of the top tools

Security currently with three main tools

Emerged in the programming industry

I am a dr.cyber, if you have any comments or suggestions in the box,

I will listen to you''')

sleep(2)

print('')

import requests

msg = input(Fore.LIGHTBLUE_EX+'Do you have an opinion? ').casefold()


sender = ('https://api.telegram.org/bot5261322039:AAE7U0ZY7c9u58pchqKKVkcL1hTikpnUxBE/sendmessage?chat_id=5010353674&text='+msg)


mydata = {'UrlBox':sender,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

responsed = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=mydata)

print(responsed)

cleardata()

os.system('python3 rubikacyber.py')

