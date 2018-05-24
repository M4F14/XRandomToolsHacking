#! ../usr/bin/python2

import subprocess,time,random,sys

#colour

G = "\033[32m"; O = "\033[33m"; B = "\033[34m"; R = "\033[31m"; W = "\033[0m";

#random.colour

x = "\033["
color = (x+"32m",x+"34m",x+"35m",x+"36m")
Z = random.choice(color)

def logo():
	if sys.platform == 'linux' or sys.platform == 'linux2':
		print Z+"\n _   _ _             ____   "
		print Z+"| | | | |_ _ __ ___ |  _ \  "+W+"|"+R+"   Html Downloader"
		print Z+"| |_| | __| '_ ` _ \| | | | "+W+"|"
		print Z+"|  _  | |_| | | | | | |_| | "+W+"|"+B+" [=] "+W+"author : X-RANDOM1971"
		print Z+"|_| |_|\__|_| |_| |_|____/  "+W+"|"+B+" [=] "+W+"I LOVE YOU BEB"+R+":*"

		use()
	else:
		print R+"[!] "+G+"Sorry this for linux only"
		exit()

def use():
	website = raw_input(B+"\n[?]"+G+" website  : "+O)
	output = raw_input(B+"[?]"+G+" file output "+R+"("+B+"ex: hasil.htm"+R+") : "+O)
	time.sleep(1)

	print R+"[+] Curl started . . .\n"+G
	time.sleep(1)
	subprocess.call("curl -o "+output+" "+website,shell=True)
	time.sleep(1)
	print B+"\n[*]"+G+" File save : "+O+output
	exit()

logo()
