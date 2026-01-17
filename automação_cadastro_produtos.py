import pyautogui
import time
import pandas as pd
import os

# quero deixar um tempo de pausa entre uma execução e outra
pyautogui.PAUSE = 1


# 1: Abrir o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)


# 2: fazer o login

pyautogui.click(x=717, y=509)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha qualquer para teste")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


# 3: abrir a base de dados (no caso dessa automação) para implementar na aplicação

tabela = pd.read_csv("produtos.csv")


# 4: vai ler e criar um histórico

arquivo_cadastrados = "produtos_cadastrados.csv"

if os.path.exists(arquivo_cadastrados):
    cadastrados = pd.read_csv(arquivo_cadastrados)
    codigos_cadastrados = set(cadastrados["codigo"])
else:
    cadastrados = pd.DataFrame(columns=["codigo"])
    codigos_cadastrados = set()

# 5: faz o cadastro

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]

    # verificação se os itens já foram cadastrados
    if codigo in codigos_cadastrados:
        continue

    # código
    pyautogui.click(x=690, y=367)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    else:
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(1)

    # salva no histórico

    codigos_cadastrados.add(codigo)

    novo = pd.DataFrame([[codigo]], columns=["codigo"])
    cadastrados = pd.concat([cadastrados, novo], ignore_index=True)
    cadastrados.to_csv(arquivo_cadastrados, index=False)

    pyautogui.scroll(5000)
