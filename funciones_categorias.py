import save as sv
import main as mn
import conditions as cd
import pandas as pd
import os
import random as rd

import time as t

from tkinter import messagebox as mb

# funcion para los pasajeros aluminio


def aluminum(indice, window, peoples, price):
    sits = []
    df = pd.read_csv('dato_vuelo.csv')
    vuelo = df["Vuelo"][indice]
    if os.path.isfile(f'{vuelo}.csv'):
        df1 = pd.read_csv(f'{vuelo}.csv')

    peoples = int(peoples)
    for i in range(peoples):
        lista = [chr(x) for x in range(65, 71)]
        nums = [str(x) for x in range(1, 13)]
        strings = []
        for h in range(len(lista)):
            for j in range(8, 12, 1):
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
    price = price * peoples

    peoples = int(peoples)
    for i in range(peoples):
        lista = [chr(x) for x in range(65, 71)]
        nums = [str(x) for x in range(1, 13)]
        strings = []
        for h in range(len(lista)):
            for j in range(0, 8, 1):
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
        a = rd.choice(strings)
        strings.remove(a)
        mb.showinfo("asiento", f"acompañante {i+1} asiento es : {a}")
        t.sleep(1)
        sits.append(a)
    mn.record_check_in(window, peoples, indice, sits, price)

def randomiser():
    letras = [chr(x) for x in range(65, 91)]
    nums = [str(x) for x in range(0, 10)]
    a = rd.choice(letras)
    combination = a + "-"
    for i in range(5):
        a = rd.choice(letras + nums)
        combination += a
    return combination
