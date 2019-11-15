# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

try:
	import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')
        
def entertools():
	os.system('sh niodlog.sh')

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=62895704349609&text=Assalamualaikum')

def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Sudah punya ID dan Password nya? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║LOGIN UNTUK MELANJUTKAN║\n╠═══════════════════════╝'
   user = raw_input('║ID      : ')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'Noniod7' and user == 'NiodTech':
      print '║LOGIN SUKSES\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login GAGAL, Silahkan hubungi ADMIN'
      wa()
      ressture()
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        
def lodhirt():
    lodhirt = [
     'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech', '      ', 'NiodTech\n']
    for o in lodhirt:
        print '\r\x1b[1;97m╔═[\x1b[1;32m+\x1b[1;97m] \x1b[1;92mLIST MENU \x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

os.system('clear')
logoname = '\033[1;32m  ____________\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\033[1;33m  ╔╗╔╔═╗╔╦╗╔═╗\n\033[1;32m ╔════════════╗\033[1;33m ║║║╠═╣║║║╠═╣\n\033[1;32m ╚════════════╝\033[1;33m ╝╚╝╩ ╩╩ ╩╩ ╩\n\033[1;31m  ║\033[1;36m██████████\033[1;31m╚╗\033[1;33m ╦╔═╔═╗╔╦╗╦ ╦\n\033[1;31m  ║\033[1;36m██\033[1;31m╔══╗\033[1;36m█\033[1;31m╔═╗\033[1;36m█\033[1;31m║\033[1;33m ╠╩╗╠═╣║║║║ ║\n\033[1;31m  ║\033[1;36m██\033[1;31m║\033[1;33m╬\033[1;31m╔╝\033[1;36m█\033[1;31m╚╗║\033[1;36m█\033[1;31m║\033[1;33m ╩ ╩╩ ╩╩ ╩╚═╝\n\033[1;31m  ║\033[1;36m██\033[1;31m╚═╝\033[1;36m█\033[1;31m║\033[1;36m█\033[1;31m╚╝\033[1;36m█\033[1;31m║\033[0m Subscribe\n\033[1;31m  ╚╗\033[1;36m█████████\033[1;31m═╝ \033[0mChannel\n\033[1;31m   ╚╗║╠╩╩╩╩╩╝   \033[0mNiod Tech\n\033[1;31m    ║║╚╗\033[1;33m┈\033[1;34m█▐█████\033[1;31m▒\033[0m.｡oO\n\033[1;31m    ║\033[1;36m██\033[1;31m╠╦╦╦╗\n\033[1;31m    ╚╗\033[1;36m██████ \033[0mAuthor \033[1;31m: \033[1;32mNiod Tech\n\033[1;31m     ╚════╝    \033[0mTeam \033[1;31m: \033[1;32mCukimay Cyber Team\n \033[1;33m<══════════════════════════════════>\n\033[1;31m'
print logoname
enternamek = raw_input("\033[1;31m[*] \033[1;32mMASUKAN NAMA KAMU: \033[1;36m")
os.system('clear')

print 32 * '\x1b[1;97m\xe2\x95\x90'
print '\033[1;33m █░░░█ █▀▀ █░░ ▄▀ ▄▀▄ █▄░▄█ █▀▀\n █░█░█ █▀▀ █░▄ █░ █░█ █░█░█ █▀▀\n ░▀░▀░ ▀▀▀ ▀▀▀ ░▀ ░▀░ ▀░░░▀ ▀▀▀'
print '                 \033[1;31m[*] \033[1;37mHi \033[1;36m' + enternamek
print 32 * '\x1b[1;97m\xe2\x95\x90'
lodhirt()
print '╠═▶\033[1;37m{\033[1;33m1\033[1;37m} \033[1;34mLogin Toolnya\033[1;37m'
print '╠═▶\033[1;37m{\033[1;33m2\033[1;37m} \033[1;34mHubungi Author \033[0m(\033[1;32mWhatsApp\033[1;37m)'
print '╠═▶\033[1;37m{\033[1;33m3\033[1;37m} \033[1;34mCukimay Cyber Team \033[0m(\033[1;32mWhatsApp\033[1;37m)\033[1;37m'
print '╠═▶\033[1;37m{\033[1;31m0\033[1;37m} \033[1;31mExit.'
pilih = input("\033[1;37m╰━╤═╤━────━ \x1b[1;91m҂\x1b[1;97m ")
if pilih == 1:
	tik()
	entertools()
elif pilih == 2:
	tik()
	wa()
	print '\n\033[1;37mTerimakasih Telah Menggunakan Tools Ini :v'
elif pilih == 3:
	os.system('xdg-open https://chat.whatsapp.com/LvvbiFlx94uDD7IS13WD26')
elif pilih == 0:
	os.system('clear')
	print '\033[1;37mTerimakasih Telah Menggunakan Tools Ini :v'
	os.system('exit')
	
