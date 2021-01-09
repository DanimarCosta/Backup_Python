# -*- coding: utf-8 -*-
# Back-End.ipynb // Desenvolvido utilizando o SDK

"""
Backup do arquivo disponivel no Google DataSheets.
This file is located at
    https://docs.google.com/spreadsheets/d/e/2PACX-1vRhmpkzwSgtoSMQEZfonBbpSmo3UP1skA3ATxatGZ5ENjU8A01SuSmwaVe6o_jD5SnBx-dUl_N9k2BD/pub?output=csv

"""

# Importa as Bibliotecas necessarias para o projeto
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

# Requisitando os Dados do Google SDK
database = pd.read_csv(
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vRhmpkzwSgtoSMQEZfonBbpSmo3UP1skA3ATxatGZ5ENjU8A01SuSmwaVe6o_jD5SnBx-dUl_N9k2BD/pub?output=csv", 
    sep=",",
    encoding="utf-8"
)
database = pd.DataFrame(database)
database.set_index("Potencia_A") 

graus_a = database.Degrees_A
indice_a = len(graus_a) - 1

graus_b = database.Degrees_B
indice_b = len(graus_b) - 1

graus_a = graus_a [indice_a]
graus_b = graus_b [indice_b]

var_graus = graus_b - graus_a

def Degrees():
    plt.title("Graus do Motor")
    motores = ["Motor A", "Motor_B"]
    graus = [graus_a, graus_b]

    cor = "yellow"

    if var_graus <= 1:
        cor = "green"

    if var_graus >= -1:
        cor = "green"
    
    elif var_graus >= 4:
        cor = "red"

    elif var_graus <= -4:
        cor = "red"
    
    elif var_graus > 1:
        cor = "yellow"
    
    elif var_graus < -1:
        cor = "yellow"
    
    print(var_graus)
                
    plt.bar(motores, graus, color=cor)
    plt.scatter(motores, graus, color='orange')
    plt.xlabel("Comparação")
    plt.savefig("Graus do Motor")
    plt.show

potencia_a = database.Potencia_A.mean()
potencia_b = database.Potencia_B.mean()

var_potencia = potencia_b - potencia_a

def Power():
    plt.title("Potencia do motor")
    motores = ["Motor A", "Motor B"]
    potencia = [potencia_a, potencia_b]

    cor = "yellow"

    if var_potencia <= 1.2:
        cor = "green"

    if var_potencia >= -1.2:
        cor = "green"
    
    elif var_potencia >= 3:
        cor = "red"

    elif var_potencia <= -3:
        cor = "red"
    
    elif var_potencia > 1.2:
        cor = "yellow"
    
    elif var_potencia < -1.2:
        cor = "yellow"

    plt.bar(motores, potencia, color=cor)
    plt.scatter(motores, potencia, color='orange')
    plt.xlabel("Comparação")
    plt.savefig("Potencia do Motor")
    plt.show

def Radar():
    print("A variacao de potencia e de", var_potencia, "%")

    df = pd.DataFrame(dict(
        r=[var_potencia, var_graus, 1],
        theta=['Varição de Potencia (%)','Variação dos Graus (g)','Balanceameto']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.show()

Power()
Degrees()