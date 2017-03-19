import os, urllib, re, sys, socket
from time import *

os.system('clear')
print('''
	|==================================|
	|	                           |	
	| [+] Author: marcos Alexandre     |
	| [+] NickName: Krypton Zero       |
	| [+] Data: 14/03/2017             |
	| [+] Email:systemmendax@gmail.com |
	|==================================|
''')
print ('''
	[1] == Extrair emails de sites
	[2] == Quebrar Hexadecimal
	
       ''')

def escolha():	
        
   
    opcao = int(input('Informe sua opcao: '))
    print
    if opcao == 1:
        #pedir para informar o site
	site = str(raw_input('Site para Extrair: '))
	#pegando ip do site
	substituir = site.replace('http://', '')
        ip_host = socket.gethostbyname(substituir)
	print site+" Ip: "+ip_host
	sleep(1)
        print (''' Pegando os Emails do Site: ''')+site

	url = urllib.urlopen(site)

	codigo = (url.read())

	emails_do_site = re.findall(r"[\w.]+[\w-]+[\w_]+[\w.]+[\w-]+[\w_]@[\w.]+[\w-]+[\w_]+[\w.]+[\w-]+[\w_]",codigo)

	for lista in emails_do_site:
   	     print '[+] Email: '+lista+'\n'
             sleep(2)  

    #opcao para quebrar hash em hexadecimal                          
    elif opcao == 2:
         #pedir para informar hash
         hash_hexadecimal = raw_input("Digite sua Hash em Hexadecimal: ")
	 sleep(1)
	 print "Sua Hash foi quebrada: "+hash_hexadecimal.decode("hex")
        
        
        
    else:
        print 'Essa opcao ainda nao esta no menu!!!'
        print

    opcao_continuar = raw_input ('Ir para o menu ? s ou n : ')
    if opcao_continuar == 's':
	os.system('clear')
	print ('''
	[1] == Extrair emails de sites
	[2] == Quebrar Hexadecimal
	
       ''')
        escolha()
	sleep(2)
    else: 
	os.system("clear")
        print '......Fechando.....'
        return

escolha()



