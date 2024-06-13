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
        df1 = pd.DataFrame(dataframe)
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
        button = ctk.CTkButton(frame, text=mensaje, command=lambda i=i: mn.info_buy(i,window,indices,peoples))
        button.grid(row=rows, column=0)
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
        button = ctk.CTkButton(frame, text=mensaje, command=lambda i=i: mn.info_buy(i,window,indices,peoples))
        button.grid(row=rows, column=0)
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
        button = ctk.CTkButton(frame, text=mensaje, command=lambda i=i: mn.info_buy(i,window,indices,peoples))
        button.grid(row=rows, column=0)
        buttons.append(button)
        rows += 1
    return buttons
        
        
        
        