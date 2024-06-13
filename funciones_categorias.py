import save as sv
import main as mn
import conditions as cd
import pandas as pd
import os
import random as rd

import time as t

from tkinter import messagebox as mb

# funcion para los pasajeros aluminio


def aluminum(index, window, peoples, price):
    sits = []
    df = pd.read_csv('dato_vuelo.csv')
    flight = df["Vuelo"][index]
    if os.path.isfile(f'{flight}.csv'):
        df1 = pd.read_csv(f'{flight}.csv')

    peoples = int(peoples)
    for i in range(peoples):
        list = [chr(x) for x in range(65, 71)]
        nums = [str(x) for x in range(1, 13)]
        strings = []
        for h in range(len(list)):
            for j in range(8, 12, 1):
                strings.append(list[h]+nums[j])
        rd.shuffle(strings)

        if os.path.isfile(f'{flight}.csv'):
            df1 = pd.read_csv(f'{flight}.csv')
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
    mn.record_check_in(window, peoples, index, sits, price)

# funcion para los pasajeros diamante


def diamond(index, window, peoples, price):
    sits = []
    df = pd.read_csv('dato_vuelo.csv')
    flight = df["Vuelo"][index]
    if os.path.isfile(f'{flight}.csv'):
        df1 = pd.read_csv(f'{flight}.csv')
    peoples = int(peoples)
    price = price * peoples

    for i in range(peoples):
        list = [chr(x) for x in range(65, 71)]
        nums = [str(x) for x in range(5,9)]
        strings = []
        for h in range(len(list)):
            for j in range(4):
                strings.append(list[h]+nums[j])
        rd.shuffle(strings)

        if os.path.isfile(f'{flight}.csv'):
            df1 = pd.read_csv(f'{flight}.csv')
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
    mn.record_check_in(window, peoples, index, sits, price)

def premium(index):
    pass

def randomiser(peoples, index):
    # df = pd.read_csv('dato_vuelo.csv')
    # flight = df["Vuelo"][index]
    # df1 = pd.read_csv(f"{flight}.csv")
    # filter = df1.loc(df1.tail(peoples))
    letters = [chr(x) for x in range(65, 91)]
    nums = [str(x) for x in range(0, 10)]
    a = rd.choice(letters)
    combination = a + "-"
    for i in range(5):
        a = rd.choice(letters + nums)
        combination += a
    return combination

