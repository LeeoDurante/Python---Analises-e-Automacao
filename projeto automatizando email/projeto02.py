import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

#Recebendo a armazenando a ação escolhida pelo usuario
ticker = input("Digite o código de ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2024-08-03", end="2024-09-03")
fechamento = dados.Close

#imprimindo resultados

maxima     =  round(fechamento.max(),  2)
minimo     =  round(fechamento.min(),  2)
valorMedio =  round(fechamento.mean(), 2)

destinatario = "leodurante.pereira@gmail.com"
assunto      = "Analises de Ações"
mensagem     =  f""" Prezado Gestor,
                Seguem as análises solicitadas da ação: {ticker}
                
                Cotação máxima: R${maxima}
                Cotação mínima: R${minimo}
                Valor Médio:  R${valorMedio}

                Qualquer dúvida, estou à disposição.

                Att.
                """

#abrir navegador para o email
webbrowser.open("www.gmail.com")
time.sleep(5)

pyautogui.PAUSE = 3

#clicar automatico no botão escrever

pyautogui.click(x=55, y=211)

#automatizar mensagem

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#enviar mensagem
pyautogui.click(x=847, y=693)

pyautogui.hotkey("ctrl", "f4")

print("e-mail enviado com sucesso")