import save as sv
import main as mn
import conditions as cd
import pandas as pd
import os
import random as rd

import time as t

from tkinter import messagebox as mb

global contador,sits
contador = 0
sits = []
# funcion para los pasajeros aluminio


def aluminum(indice, window, peoples, price):
    sits = []
    df = pd.read_csv('dato_vuelo.csv')
    vuelo = df["Vuelo"][indice]
    if os.path.isfile(f'{vuelo}.csv'):
        df1 = pd.read_csv(f'{vuelo}.csv')
    peoples = int(peoples)
    price = price * peoples
    lista = [chr(x) for x in range(65, 71)]
    nums = [str(x) for x in range(9,13)]
    strings = []
    for h in range(len(lista)):
        for j in range(4):
            strings.append(lista[h]+nums[j])
        rd.shuffle(strings)
    if os.path.isfile(f'{vuelo}.csv'):
            df1 = pd.read_csv(f'{vuelo}.csv')
            for i in range(len(df1)):
                if strings[i] in df1["asiento"].values:
                    strings.remove(strings[i])
    if len(strings) < peoples:
            mb.showerror("Error", "No hay suficientes asientos")
            return
    for i in range(peoples):
        a = rd.choice(strings)
        strings.remove(a)
        mb.showinfo("asiento", f"acompañante {i+1} asiento es : {a}")
        t.sleep(1)
        sits.append(a)
    mn.record_check_in(window, peoples, indice, sits, price)

# funcion para los pasajeros diamante


def diamond(indice, window, peoples, price):
    sits = []
    df = pd.read_csv('dato_vuelo.csv')
    vuelo = df["Vuelo"][indice]
    if os.path.isfile(f'{vuelo}.csv'):
        df1 = pd.read_csv(f'{vuelo}.csv')
    peoples = int(peoples)
    price = price * peoples
    lista = [chr(x) for x in range(65, 71)]
    nums = [str(x) for x in range(5,9)]
    strings = []
    for h in range(len(lista)):
        for j in range(4):
            strings.append(lista[h]+nums[j])
        rd.shuffle(strings)
    if os.path.isfile(f'{vuelo}.csv'):
            df1 = pd.read_csv(f'{vuelo}.csv')
            for i in range(len(df1)):
                if strings[i] in df1["asiento"].values:
                    strings.remove(strings[i])
    if len(strings) < peoples:
            mb.showerror("Error", "No hay suficientes asientos")
            return
    for i in range(peoples):
        a = rd.choice(strings)
        strings.remove(a)
        mb.showinfo("asiento", f"acompañante {i+1} asiento es : {a}")
        t.sleep(1)
        sits.append(a)
    mn.record_check_in(window, peoples, indice, sits, price)

def mensaje():
    mb.showinfo("Error", "Asiento ocupado")
    return



def reiniciar():
    global contador,sits
    contador = 0
    sits = []

def actualizar(matriz, indice):
    df = pd.read_csv('dato_vuelo.csv')
    vuelo = df["Vuelo"][indice]
    if os.path.isfile(f'{vuelo}.csv'):
        df1 = pd.read_csv(f'{vuelo}.csv')
        for h in range(len(df1)):
            for i in range(len(matriz)):  # Ajustar al tamaño real de 'matriz'
                for j in range(len(matriz[i])):  # Ajustar al tamaño real de cada fila de 'matriz'
                    if df1["asiento"][h] == matriz[i][j].cget("text"):
                        matriz[i][j].configure(fg_color="yellow")
                        matriz[i][j].configure(command=lambda: mensaje())
    else:
        return




def premium(row, col, matriz, indice, peoples, window, price):
    global sits,contador
    df = pd.read_csv('dato_vuelo.csv')
    matriz[row][col].configure(fg_color="green")
    sits.append(matriz[row][col].cget("text"))
    matriz[row][col].configure(command=lambda: mensaje())
    mb.showinfo("asiento", f"asiento acompañante {contador+1} es : {matriz[row][col].cget('text')}")
    contador += 1
    print(contador)
    if contador == peoples:
        price = price * peoples
        mn.record_check_in(window, peoples, indice, sits, price)
        

# funcion para randomizar el codigo alpha numerico
def randomiser(peoples, indice):
    df = pd.read_csv('dato_vuelo.csv')
    vuelo = df["Vuelo"][indice]
    lista_nombres = []
    if os.path.isfile(f'{vuelo}.csv'):
        df1 = pd.read_csv(f"{vuelo}.csv")
        lista_nombres = df1["nombre"].tail(peoples).tolist()
    letters = [chr(x) for x in range(65, 91)]
    nums = [str(x) for x in range(0, 10)]
    all_codes = letters + nums 
    rd.shuffle(all_codes)
    codigos = []
    for i in range(peoples):
        letter = lista_nombres[i]
        if letter not in codigos:
            first_letter = letter[0].upper()
            codigo = first_letter + "-" + rd.choice(all_codes ) + rd.choice(all_codes) + rd.choice(all_codes) + rd.choice(all_codes) + rd.choice(all_codes)
            codigos.append(codigo)
    return codigos
