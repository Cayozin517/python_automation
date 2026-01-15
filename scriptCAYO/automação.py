import pyautogui
import pyperclip
import time
    
pyautogui.PAUSE=0.5
pyautogui.press("win")
pyautogui.write("bloco de notas")
pyautogui.press("enter")
time.sleep(3)

import pandas 

ordem =pandas.read_csv("dadospessoais.csv", encoding="utf-8")
print (ordem)

for linha in ordem.index:
    nome = str(ordem.loc[linha, "Nome"])
    estado= str(ordem.loc[linha, "Estado"])
    idade= str(ordem.loc[linha, "Idade"])
    cidade= str (ordem.loc[linha, "Cidade"])
    tudo=(f"NOME: {nome} | ESTADO:  {estado} | IDADE: {idade} | CIDADE: {cidade}")
    pyperclip.copy(tudo)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(1)


