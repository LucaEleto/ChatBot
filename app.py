import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui


#abrir whatsapp

#ler planilha de clientes
workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2, max_row=3):
    nome = linha[0].value
    telefone = linha[1].value
    mensagem = f'Olá {nome}'

    #link personalizado para ennviar as mensagens
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(15)
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(5)
        pyautogui.click(seta[0], seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possivel enviar mensagem para {nome}')
        with open('erros.csv','a',newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {telefone}')