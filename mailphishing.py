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

##################################################################
# Cores
##################################################################
cores = {
    "limpar": "\033[m",
    "branco": "\033[1;30m",
    "vermelho": "\033[1;31m",
    "verde": "\033[1;32m",
    "amarelo": "\033[1;33m",
    "azul": "\033[1;34m",
    "magenta": "\033[1;35m",
    "ciano": "\033[1;36m",
    "cinza": "\033[1;34m",
}

##################################################################
# Validação do concentimento !
##################################################################
os.system('clear')
print(f'''
{cores['vermelho']}
___  ___      _ _  ______ _     _     _     _
|  \/  |     (_) | | ___ \ |   (_)   | |   (_)
| .  . | __ _ _| | | |_/ / |__  _ ___| |__  _ _ __   __ _
| |\/| |/ _` | | | |  __/| '_ \| / __| '_ \| | '_ \ / _` |
| |  | | (_| | | | | |   | | | | \__ \ | | | | | | | (_| |
\_|  |_/\__,_|_|_| \_|   |_| |_|_|___/_| |_|_|_| |_|\__, |
                                                     __/ |
                   ___  _          __               |___/
                  / _ \| |         | |
                 / /_\ \ | ___ _ __| |_
                 |  _  | |/ _ \ '__| __|
                 | | | | |  __/ |  | |_
                 \_| |_/_|\___|_|   \__|

########################### ALERTA #################################
# Esta ferramenta é destinada exclusivamente para fins educativos  #
# e de conscientização sobre os perigos do phishing. O uso desta   #
# ferramenta em ambientes não autorizados ou para atividades       #
# maliciosas é estritamente proibido.                              #
####################################################################
#                                                                  #
# Ao executar esta ferramenta, você concorda em usá-la de maneira  #
# ética e responsável. Não nos responsabilizamos por qualquer uso  #
# indevido ou ilegal desta ferramenta. Certifique-se de obter o    #
# devido consentimento antes de realizar testes de conscientização.#
#                                                                  #
########################### ALERTA #################################''')
consentimento = input(f'''{cores['azul']}Concorda? (sim ou nao)> {cores['limpar']}''')

if consentimento == 'sim':
    print(f'''{cores['amarelo']}Carregando...{cores['limpar']}''')
    time.sleep(2)
    pass
else:
    sys.exit()

##################################################################
# Classes e Funções
##################################################################
def menu():
    os.system('clear')
    print(f'''{cores['azul']}
888b     d888          d8b 888
8888b   d8888          Y8P 888
88888b.d88888              888
888Y88888P888  8888b.  888 888
888 Y888P 888     "88b 888 888
888  Y8P  888 .d888888 888 888
888   "   888 888  888 888 888
888       888 "Y888888 888 888
{cores['vermelho']}
8888888b.  888      d8b          888      d8b
888   Y88b 888      Y8P          888      Y8P
888    888 888                   888
888   d88P 88888b.  888 .d8888b  88888b.  888 88888b.   .d88b.
8888888P"  888 "88b 888 88K      888 "88b 888 888 "88b d88P"88b
888        888  888 888 "Y8888b. 888  888 888 888  888 888  888
888        888  888 888      X88 888  888 888 888  888 Y88b 888
888        888  888 888  88888P' 888  888 888 888  888  "Y88888
                                                            888
{cores['amarelo']}by github.com/AlldDev{cores['vermelho']}                                  Y8b d88P
                                                        "Y88P"{cores['limpar']}
Select from the menu:
    1) Alvo Unico
    2) Múltiplos Alvos
    3) Help
   99) Sair
''')



def enviar_email(email_vitima, fake_remetente,title_email, path_body_email, server_smtp, login_smtp, passwd_smtp):
    print(f'''{cores['azul']}Enviando phishing para a vítima {email_vitima} aguarde...{cores['limpar']}''')
    try:
        if fake_remetente == None:
            fake_remetente = email_vitima
        else:
            pass


        with open(path_body_email, 'rb') as file:
            file = file.read()
            body_email = file.decode()

        msg = MIMEMultipart()
        msg['Subject'] = title_email
        msg['From'] = fake_remetente
        msg['To'] = email_vitima

        body_email = MIMEText(body_email, 'html', 'utf-8')
        msg.attach(body_email)

        smtp = smtplib.SMTP(server_smtp)
        smtp.starttls()

        smtp.login(login_smtp, passwd_smtp)
        smtp.sendmail(login_smtp, email_vitima, msg.as_string())
        print(f'''{cores['verde']}Phishing enviado com sucesso para {email_vitima}!{cores['limpar']}''')
    except:
        print(f'''{cores['vermelho']}Falha ao enviar Phishing para {email_vitima}!{cores['limpar']}''')

##################################################################
# Main / Principal
##################################################################
if __name__ == "__main__":

    #####################
    # LOOP Principal
    #####################
    while True:
        while True:
            try:
                menu()
                entry = int(input(f'''{cores['ciano']}select> {cores['limpar']}'''))
                break
            except:
                pass
        while True:
            match entry:
                case 1: # ALVO UNICO
                    email_vitima = input(f'''{cores['ciano']}email vítima> {cores['limpar']}''')
                    fake_remetente = input(f'''{cores['ciano']}email remetente ({cores['vermelho']}fake{cores['ciano']})> {cores['limpar']}''')
                    title_email = input(f'''{cores['ciano']}título do email> {cores['limpar']}''')
                    path_body_email = input(f'''{cores['ciano']}caminho da mensagem ({cores['vermelho']}.txt{cores['ciano']})> {cores['limpar']}''')
                    server_smtp = input(f'''{cores['ciano']}servidor smtp ({cores['vermelho']}ex:mail.server.com:587{cores['ciano']})> {cores['limpar']}''')
                    login_smtp = input(f'''{cores['ciano']}login do smtp> {cores['limpar']}''')
                    passwd_smtp = input(f'''{cores['ciano']}senha do smtp> {cores['limpar']}''')

                    enviar_email(email_vitima, fake_remetente, title_email, path_body_email, server_smtp, login_smtp, passwd_smtp)
                    print(f'''{cores['amarelo']}Voltando para o menu em 10 segundos!{cores['amarelo']}''')
                    time.sleep(10)
                    break
                case 2: # MULTIPLOS ALVOS
                    path_emails = input(f'''{cores['ciano']}lista de emails ({cores['vermelho']}.txt{cores['ciano']})> {cores['limpar']}''')

                    with open(path_emails, 'r') as file:
                        file = file.read()
                        emails = file.replace('\n', '').split(';')

                    fake_remetente = input(f'''{cores['ciano']}email remetente ({cores['vermelho']}fake{cores['ciano']})> {cores['limpar']}''')
                    title_email = input(f'''{cores['ciano']}título do email> {cores['limpar']}''')
                    path_body_email = input(f'''{cores['ciano']}caminho da mensagem ({cores['vermelho']}.txt{cores['ciano']})> {cores['limpar']}''')
                    server_smtp = input(f'''{cores['ciano']}servidor smtp ({cores['vermelho']}ex:mail.server.com:587{cores['ciano']})> {cores['limpar']}''')
                    login_smtp = input(f'''{cores['ciano']}login do smtp> {cores['limpar']}''')
                    passwd_smtp = input(f'''{cores['ciano']}senha do smtp> {cores['limpar']}''')

                    for email in emails:
                        enviar_email(email, fake_remetente, title_email, path_body_email, server_smtp, login_smtp, passwd_smtp)

                    print(f'''{cores['amarelo']}Voltando para o menu em 10 segundos!{cores['amarelo']}''')
                    time.sleep(10)
                    break

                case 3: # HELP (precisa fazer ainda)
                    pass
                case 99: # SAIR
                    print(f'''{cores['azul']}Já vai tão cedo? Que pena... Vejo o Sr(a) em breve certo?{cores['amarelo']} Até mais ;D{cores['limpar']}''')
                    sys.exit()
