import save as sv
import main as mn
import conditions as cd
import pandas as pd
import os 
import random as rd

import time as t

from tkinter import messagebox as mb



def aluminum(indice,window,peoples):
    mensajes = []
    peoples = int(peoples)
    for i in range(peoples):
        lista = [ chr(x) for x in range(65,71) ]
        nums = [ str(x) for x in range(1,13) ]
        strings = []
        for i in range(len(lista)):
            for j in range(8,12,1):
                strings.append(lista[i]+nums[j])
        rd.shuffle(strings)
        a=rd.choice(strings)
        mb.showinfo("asiento",f"acompañante {i+1} asiento es : {a}")
        t.sleep(1)
    mn.record_check_in(window,peoples,indice)
