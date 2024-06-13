import pandas as pd
import os
from tkinter import messagebox as mb
import main as mn
import customtkinter as ctk

# def profits(client,indice):
#     w

def record_base(peoples, datas, sits, indice, window, pay_client):
    df = pd.read_csv('dato_vuelo.csv')
    vuelo = df["Vuelo"][indice]
    for i in range(peoples):
        dataframe = {"asiento": [sits[i]], "nombre": [datas[i][1]],
                     "apellido": [datas[i][2]], "dni": [datas[i][3]],
                     "telefono": [datas[i][6]], "email": [datas[i][5]],
                     "nacimiento": [datas[i][7]], "nacionalidad": [datas[i][4]], "asistencia": [datas[i][8]]}
        base_datos = {"nombre": [datas[i][1]], "apellido": [datas[i][2]], "dni": [datas[i][3]],"telefono": [datas[i][6]], "email": [datas[i][5]]}
        df1 = pd.DataFrame(dataframe)
        df2 = pd.DataFrame(base_datos)
        if os.path.isfile("clientes.csv"):
            df2.to_csv("clientes.csv", mode='a', header=False, index=False, sep=";")
        else:
            df2.to_csv("clientes.csv", index=False, sep=";", header=True, mode='a')
            
        if not os.path.isfile(f'{vuelo}.csv'):
            df1.to_csv(f'{vuelo}.csv', index=False,sep=",",header=True,mode='a')
        else:
            df1.to_csv(f'{vuelo}.csv', mode='a', header=False, index=False,sep=",")


def search_low (filter,day,indices,window,peoples,buttons,frame):
    buttons = [i.destroy() for i in buttons]
    buttons = []
    df = pd.read_csv('dato_vuelo.csv')
    df_filtered = df.loc[indices]
    df_filtered = df_filtered[df_filtered['Fecha'] == day]  # Filtra el DataFrame con los índices
    if df_filtered.empty:
        mb.showerror("error", "no hay vuelos disponibles ese dia")
        return
    df_filtered = df_filtered.sort_values(by='ValorMin',ascending=True)# Ordena el DataFrame filtrado
    rows = 0
    for i in df_filtered.index:  # Itera sobre los índices del DataFrame filtrado y ordenado
        mensaje = f"Vuelo: {df_filtered['Vuelo'][i]} \n"
        mensaje += f"Origen: {df_filtered['CiudadOrigen'][i]} \n"
        mensaje += f"Destino: {df_filtered['CiudadDestino'][i]} \n"
        mensaje += f"Fecha: {df_filtered['Fecha'][i]} \n"
        mensaje += f"Hora salida: {df_filtered['HoraSalida'][i]} \n"
        mensaje += f"Hora llegada: {df_filtered['HoraLlegada'][i]} \n"
        mensaje += f"Valor: {df_filtered['ValorMin'][i]} \n"
        button = ctk.CTkButton(frame, text=mensaje, command=lambda i=i: mn.info_buy(i,window,indices,peoples),width=900,height=150,font = ("Arial", 20))
        button.grid(row=rows, column=0, padx=20, pady=10)
        buttons.append(button)
        rows += 1
    return buttons
        
def search_medium (filter,days,indices,window,peoples,buttons,frame):
    buttons = [i.destroy() for i in buttons]
    buttons = []
    df = pd.read_csv('dato_vuelo.csv')
    df_filtered = df.loc[indices]  # Filtra el DataFrame con los índices
    df_filtered = df_filtered[df_filtered['Fecha'] == days]  # Filtra el DataFrame con los índices
    df_filtered = df_filtered.sort_values(by='ValorMedio',ascending=True)  # Ordena el DataFrame filtrado
    rows = 0
    if df_filtered.empty:
        mb.showerror("error", "no hay vuelos disponibles")
        return
    for i in df_filtered.index:  # Itera sobre los índices del DataFrame filtrado y ordenado
        mensaje = f"Vuelo: {df_filtered['Vuelo'][i]} \n"
        mensaje += f"Origen: {df_filtered['CiudadOrigen'][i]} \n"
        mensaje += f"Destino: {df_filtered['CiudadDestino'][i]} \n"
        mensaje += f"Fecha: {df_filtered['Fecha'][i]} \n"
        mensaje += f"Hora salida: {df_filtered['HoraSalida'][i]} \n"
        mensaje += f"Hora llegada: {df_filtered['HoraLlegada'][i]} \n"
        mensaje += f"Valor: {df_filtered['ValorMedio'][i]} \n"
        button = ctk.CTkButton(frame, text=mensaje, command=lambda i=i: mn.info_buy(i,window,indices,peoples),width=900,height=150,font=("Arial", 20))
        button.grid(row=rows, column=0, padx=20, pady=10)
        buttons.append(button)
        rows += 1
    return buttons



def search_high (filter,days,indices,window,peoples,buttons,frame):
    buttons = [i.destroy() for i in buttons]
    buttons = []
    df = pd.read_csv('dato_vuelo.csv')
    df_filtered = df.loc[indices]  # Filtra el DataFrame con los índices
    df_filtered = df_filtered[df_filtered['Fecha'] == days]  # Filtra el DataFrame con los índices
    df_filtered = df_filtered.sort_values(by='ValorMax',ascending=True)  # Ordena el DataFrame filtrado
    rows = 0
    if df_filtered.empty:
        mb.showerror("error", "no hay vuelos disponibles")
        return
    for i in df_filtered.index:  # Itera sobre los índices del DataFrame filtrado y ordenado
        mensaje = f"Vuelo: {df_filtered['Vuelo'][i]} \n"
        mensaje += f"Origen: {df_filtered['CiudadOrigen'][i]} \n"
        mensaje += f"Destino: {df_filtered['CiudadDestino'][i]} \n"
        mensaje += f"Fecha: {df_filtered['Fecha'][i]} \n"
        mensaje += f"Hora salida: {df_filtered['HoraSalida'][i]} \n"
        mensaje += f"Hora llegada: {df_filtered['HoraLlegada'][i]} \n"
        mensaje += f"Valor: {df_filtered['ValorMax'][i]} \n"
        button = ctk.CTkButton(frame, text=mensaje, command=lambda i=i: mn.info_buy(i,window,indices,peoples),width=900,height=150,font=("Arial", 20))
        button.grid(row=rows, column=0, padx=20, pady=10)
        buttons.append(button)
        rows += 1
    return buttons

def get_last():
    if os.path.isfile("base.csv"):
        df = pd.read_csv("base.csv")
        num = df.tail(1)
        return num["numero_vuelo"].values[0]+1
    else:
        return 1


def fly(vuelo):
    if os.path.isfile(f'{vuelo}.csv'):
        if os.path.isfile("base.csv"):
            df = pd.read_csv("base.csv")
            if vuelo in df["vuelo"].values:
                return 
        df1 = pd.read_csv(f'{vuelo}.csv')
        num = get_last()
        data = {"numero_vuelo":[num],"archivo":[f'{vuelo}.csv'], "vuelo":[vuelo]}
        df2 = pd.DataFrame(data)
        if not os.path.isfile("base.csv"):
            df2.to_csv("base.csv", index=False, sep=",", header=True, mode='a')
        else:
            df2.to_csv("base.csv", mode='a', header=False, index=False, sep=",")
    else:
        pass

def record_profits(name, number, date, code, price):
    if os.path.isfile("profits.csv"):
        data = {"nombre": [name], "numero": [number], "fecha": [date], "codigo": [code], "precio": [price],"ganancia": [0]}
        df = pd.DataFrame(data)
        df.to_csv("profits.csv", mode='a', header=False, index=False, sep=",")
    else:
        data = {"nombre": [name], "numero": [number], "fecha": [date], "codigo": [code], "precio": [price],"ganancia": [0]}
        df = pd.DataFrame(data)
        df.to_csv("profits.csv", mode='a', header=True, index=False, sep=",")