import pandas as pd
import os
from tkinter import messagebox as mb
import main as mn

# def profits(client,indice):
#     w

def record_base(peoples, datas, sits, index, window, pay_client):
    df = pd.read_csv('dato_vuelo.csv')
    flight = df["Vuelo"][index]
    for i in range(peoples):
        dataframe = {"asiento": [sits[i]], "nombre": [datas[i][1]],
                     "apellido": [datas[i][2]], "dni": [datas[i][3]],
                     "telefono": [datas[i][6]], "email": [datas[i][5]],
                     "nacimiento": [datas[i][7]], "nacionalidad": [datas[i][4]], "asistencia": [datas[i][8]]}
        df1 = pd.DataFrame(dataframe)
        if not os.path.isfile(f'{flight}.csv'):
            df1.to_csv(f'{flight}.csv', index=False,sep=",",header=True,mode='a')
        else:
            df1.to_csv(f'{flight}.csv', mode='a', header=False, index=False,sep=",")
