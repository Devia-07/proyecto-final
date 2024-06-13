import tkinter as tk
from tkinter import messagebox as mb
import pandas as pd
import datetime
import re
import pycountry
import os
import save as sv
import main as mn
import funciones_categorias as fc

def conditions_record(peoples, quantity, datas, sits, index, window,price):
    df = pd.read_csv('dato_vuelo.csv')
    if os.path.isfile(f'{df["Vuelo"][index]}.csv'):
        df1 = pd.read_csv(f'{df["Vuelo"][index]}.csv')
    datas = [[i.get() for i in subdatas] for subdatas in datas]
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@](gmail\.com|hotmail\.com|outlook\.com)$'
    # lista de paises
    for i in range(peoples):
        for j in range(quantity):
            if datas[i][j] == "":
                mb.showerror("registro", "registro fallido rellene todas las casillas")
                return
    countries = [country.name for country in pycountry.countries]
    for i in range(peoples):
        try:
            datetime.datetime.strptime(datas[i][7], '%d/%m/%Y')
        except ValueError:
            mb.showerror(
                "registro", "registro fallido la fecha debe tener el formato dd/mm/yyyy")
        if datas[i][j] == "":
            mb.showerror(
                "registro", "registro fallido rellene todas las casillas")
            return
        elif not datas[i][3].isdigit():
            mb.showerror(
                "registro", "registro fallido la identificacion debe ser un numero")
            return
        elif len(datas[i][3]) < 7 or len(datas[i][3]) >= 11:
            mb.showerror(
                "registro", "registro fallido la identificacion debe tener 10 digitos")
            return
        elif not datas[i][6].isdigit():
            mb.showerror(
                "registro", "registro fallido el telefono debe ser un numero")
            return
        elif len(datas[i][6]) != 10:
            mb.showerror(
                "registro", "registro fallido el telefono debe tener 10 digitos")
            return
        # si el numero no comienza por 3
        elif datas[i][6][0]  != "3":
            mb.showerror(
                "registro", "el numero debe de comenzar por 3")
            return
        elif not re.search(regex, datas[i][5]):
            mb.showerror(
                "registro", "registro fallido el dominio del correo no es valido")
            return
        elif datas[i][4].capitalize() not in countries:
            mb.showerror(
                "registro", "registro fallido la nacionalidad no es valida")
            return
        
        if os.path.isfile("clientes.csv"):
            df2 = pd.read_csv("clientes.csv", sep=";")
            if datas[i][3] in df2["dni"].values:
                mb.showerror("registro", "registro fallido el dni ya esta registrado")
                return
            elif datas[i][5] in df2["email"].values:
                mb.showerror("registro", "registro fallido el email ya esta registrado")
                return
            elif datas[i][6] in df2["telefono"].values:
                mb.showerror("registro", "registro fallido el telefono ya esta registrado")
                return
    mb.showinfo("registro", "registro exitoso")
    mn.pay_sits(window, peoples, datas, sits, index, price)


def conditions_pay(window_pay, pay_client, peoples, datas, sits, indice, price):
    pay_client = [i.get() for i in pay_client]
    for i in range(4):
        try:
            datetime.datetime.strptime(pay_client[2], '%d/%m/%Y')
        except ValueError:
            mb.showerror(
                "registro", "registro fallido la fecha debe tener el formato dd/mm/yyyy")
        if pay_client[i] == "":
            mb.showerror("pago", "rellene todas las casillas")
            return
        elif len(pay_client[3]) != 3:
            mb.showerror("pago", "el codigo de seguridad debe tener 3 digitos")
            return
        elif not pay_client[3].isdigit():
            mb.showerror("pago", "el codigo de seguridad debe ser un numero")
            return
        elif len(pay_client[1]) != 16:
            mb.showerror("pago", "el numero de tarjeta debe tener 16 digitos")
            return
        elif not pay_client[1].isdigit():
            mb.showerror("pago", "el numero de tarjeta debe ser un numero")
            return

# Convertir la fecha de vencimiento a un objeto datetime
        expiry_date = datetime.datetime.strptime(pay_client[2], "%d/%m/%Y")

        # Obtener la fecha actual
        now = datetime.datetime.now()

        # Comparar las fechas
        if expiry_date < datetime.datetime.strptime(now.strftime("%d/%m/%Y"), "%d/%m/%Y"):
            mb.showerror("pago", "la tarjeta esta vencida")
            return
    #pay_client[0] = nombre
    #pay_client[1] = numero de tarjeta
    #pay_client[2] = fecha de vencimiento
    #pay_client[3] = codigo de seguridad
    mb.showinfo("pago", "pago exitoso, has pagado: $"+str(price))
    sv.record_base(peoples, datas, sits, indice, window_pay, pay_client)
    df = pd.read_csv("dato_vuelo.csv")
    sv.record_profits(pay_client[0],pay_client[1],pay_client[2],pay_client[3],price)
    sv.fly(df["Vuelo"][indice])
    mn.tickets(window_pay, peoples, datas, sits, indice)


def condition_check_in(code, dni, window_check_in):# funcion que valida el login
    if code == "admin" and dni == "1234":
        mb.showinfo("bienvenido administrador", "Bienvenido administrador")
        mn.admin(window_check_in)
        return
    if os.path.isfile("base.csv"):
        df = pd.read_csv("base.csv", sep=",")  # se lee el archivo csv
        for i in df.index:
            archivo = df["archivo"].values[i]
            df1 = pd.read_csv(f"{archivo}", sep=",")
            if code in df1["codigo"].values and int(dni) in df1["dni"].values:
                mb.showinfo("check-in", "check-in exitoso")
                mb.showinfo("check-in", "asientos asignados")
                return
    mb.showerror("check-in", "codigo o dni incorrecto")


def lista_vuelos():  # funcion que retorna la lista de vuelos
    df = pd.read_csv("dato_vuelo.csv", sep=",")  # se lee el archivo csv
    origen = set(df['CiudadOrigen'])  # se obtiene la columna "CiudadOrigen"
    destino = set(df["CiudadDestino"])  # se obtiene la columna "CiudadDestino"
    return origen, destino


def conditions_search(destination, origin, going, window, peoples):
    if origin == "" or destination == "" or peoples == "":
        mb.showerror("error", "rellene todas las casillas")
        return
    elif not int(peoples.isdigit()):
        mb.showerror("error", "el numero de pasajeros debe ser un numero")
        return
    elif origin == destination or destination == origin:
        mb.showerror(
            "error", "la ciudad de origen y destino no pueden ser iguales")
        return
    elif going == "":
        mb.showerror("error", "rellene la casilla de ida")
    
        return
    peoples = int(peoples)
    if peoples > 72:
        mb.showerror("error", "no hay cupos disponibles")
        return
    else:
        indices = search(origin, destination)
        if indices == []:
            mb.showerror("error", "no hay vuelos disponibles")
            return
        else:
            mn.search_fly(indices, window, peoples)


def search(origin, destination):
    indices = []
    dates_june = []
    for day in range(1, 31):
        date = datetime.datetime(2024, 6, day)
        if date.weekday() in [2, 3]:  # 2 es miércoles, 3 es jueves
            dates_june.append(date.strftime("%Y-%m-%d"))
    print(dates_june)
    df = pd.read_csv("dato_vuelo.csv", sep=",")
    df_filtered = df.loc[(df["CiudadOrigen"] == origin) & (df["CiudadDestino"] == destination) & (df["Fecha"].isin(dates_june))]
    for i in df_filtered.index:
        indices.append(i)
    return indices


def filter_search(filtrar,days,indices,window,peoples,buttons,frame):
    if filtrar == "":
        mb.showerror("error", "rellene la casilla de filtro")
        return
    elif filtrar == "barato":
        buttons = sv.search_low(filtrar,days,indices,window,peoples,buttons,frame)
    elif filtrar == "caro":
        buttons = sv.search_high(filtrar,days,indices,window,peoples,buttons,frame)
    elif filtrar == "medio":
        buttons =sv.search_medium(filtrar,days,indices,window,peoples,buttons,frame)
        
    

#busqueda de horas
def search_hours(indice):
    df = pd.read_csv("dato_vuelo.csv", sep=",")
    horas = []
    filtered = df.loc[(df["Fecha"] == df["Fecha"].values[indice]) & 
                    (df["CiudadOrigen"] == df["CiudadOrigen"].values[indice]) & 
                    (df["CiudadDestino"] == df["CiudadDestino"].values[indice])]
    for i in filtered.index:
        horas.append(i)
    return horas


def getnums(text):  # funcion que retorna los numeros de un string
    nums = []
    for i in range(len(text)):  # se recorre el string
        if text[i].isdigit():  # si el caracter es un digito
            nums.append(text[i])  # se agrega a la lista
    return int("".join(nums))  # se retorna la lista de numeros



def see_profits():
    df = pd.read_csv("profits.csv", sep=",")
    df["ganancias"] = df["precio"].values.sum()
    df.to_csv("profits.csv", index=False, sep=";", mode="w")
    os.system("start excel.exe profits.csv")
    return
