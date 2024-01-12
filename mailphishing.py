##################################################################
# Imports
##################################################################
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP
import smtplib
import sys
import os
import time

# from datetime import datetime

##################################################################
# Variáveis globais / Outros
##################################################################


##################################################################
# Cores
##################################################################
cores = {
    "limpar": "\033[m",
    "branco": "\033[0;30m",
    "vermelho": "\033[1;31m",
    "verde": "\033[0;32m",
    "amarelo": "\033[0;33m",
    "azul": "\033[1;34m",
    "magenta": "\033[0;35m",
    "ciano": "\033[0;36m",
    "cinza": "\033[0;34m",
}

##################################################################
# Classes e Funções
##################################################################
def logo():
    os.system('cls' or 'clear')
    print(f'''                                                     
{cores['azul']}                           ,,    ,,                                                    
{cores['azul']}`7MMM.     ,MMF'           db  `7MM  {cores['vermelho']}     .M"""bgd                                     {cores['limpar']}
{cores['azul']}  MMMb    dPMM                   MM  {cores['vermelho']}    ,MI    "Y                                     
{cores['azul']}  M YM   ,M MM   ,6"Yb.  `7MM    MM  {cores['vermelho']}    `MMb.   `7MMpdMAo.  ,6"Yb.  `7MMpMMMb.pMMMb.  
{cores['azul']}  M  Mb  M' MM  8)   MM    MM    MM  {cores['vermelho']}      `YMMNq. MM   `Wb 8)   MM    MM    MM    MM  
{cores['azul']}  M  YM.P'  MM   ,pm9MM    MM    MM  {cores['vermelho']}    .     `MM MM    M8  ,pm9MM    MM    MM    MM  
{cores['azul']}  M  `YM'   MM  8M   MM    MM    MM  {cores['vermelho']}    Mb     dM MM   ,AP 8M   MM    MM    MM    MM  
{cores['azul']}.JML. `'  .JMML.`Moo9^Yo..JMML..JMML.{cores['vermelho']}   P"Ybmmd"  MMbmmd'  `Moo9^Yo..JMML  JMML  JMML.
{cores['azul']}                                     {cores['vermelho']}              MM                                  
{cores['amarelo']}by github.com/AlldDev        {cores['vermelho']}                    .JMML.                                
{cores['limpar']}''')

def menu():
    print(f'''
Select from the menu:
    1) Alvo Unico
    2) Vários Alvos
    3) Help
   99) Sair
''')

def enviar_email(email_vitima, title_email, path_body_email, server_smtp, login_smtp, passwd_smtp):
    print(f'Enviando spam para a vítima {email_vitima} aguarde...')
    try:
        with open(path_body_email, 'rb') as file:
            file = file.read()
            body_email = file.decode()

        msg = MIMEMultipart()
        msg['Subject'] = title_email
        msg['From'] = email_vitima
        msg['To'] = email_vitima

        body_email = MIMEText(body_email, 'html', 'utf-8')
        msg.attach(body_email)

        smtp = smtplib.SMTP(server_smtp)
        smtp.starttls()

        smtp.login(login_smtp, passwd_smtp)
        smtp.sendmail(login_smtp, email_vitima, msg.as_string())
        print(f'Spam enviado com sucesso para {email_vitima}')
    except:
        print(f'Falha ao enviar Spam para {email_vitima}!')

##################################################################
# Main / Principal
##################################################################
if __name__ == "__main__":
    #logo()
    #menu()

##################################################################
# LOOP Principal
##################################################################
    while True:
        # LOOP DO MENU
        while True:
            try:
                logo()
                menu()
                entry = int(input('select> '))
                break
            except:
                pass
        # LOOP DAS INTERAÇÔES
        while True:
            match entry:
                case 1: # ALVO UNICO
                    email_vitima = input('email da vítima> ')
                    title_email = input('título do email> ')
                    path_body_email = input('caminho do arquivo/corpo da mensagem> ')
                    server_smtp = input('servidor smtp (ex:mail.server.com:587)> ')
                    login_smtp = input('login do email smtp> ')
                    passwd_smtp = input('senha do smtp> ')
                    enviar_email(email_vitima, title_email, path_body_email, server_smtp, login_smtp, passwd_smtp)
                    print('Voltando para o menu em 10 segundos')
                    time.sleep(10)
                    break
                case 2: # MULTIPLOS ALVOS
                    pass
                case 3: # HELP (precisa fazer ainda)
                    pass
                case 99: # SAIR
                    print('Saindo')
                    sys.exit()
