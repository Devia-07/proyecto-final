import save as sv
import main as mn
import conditions as cd
import pandas as pd
import os 
import random as rd

from tkinter import messagebox as mb



def aluminum(indice):
    lista = [ chr(x) for x in range(65,71) ]
    nums = [ str(x) for x in range(1,13) ]
    strings = []
    for i in range(len(lista)):
        for j in range(8,12,1):
            strings.append(lista[i]+nums[j])
    rd.shuffle(strings)
    a=rd.choice(strings)
    print(a)
    return mb.showinfo("asiento",f"su asiento es: {a} ")

aluminum(1)