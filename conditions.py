import tkinter as tk 
from tkinter import messagebox as mb
import pandas as pd
import datetime 
import re
import pycountry
import os
import save as sv
import main as mn

def conditions_record(gender,name,lastname,id,telephone,nationality,email,birthday,attendance,window):

    countries = [country.name for country in pycountry.countries] #lista de paises
#_______________________________________________________________________________________________________________________
    # registro fecha
    try:
        datetime.datetime.strptime(birthday, '%d/%m/%Y')
    except ValueError:
        mb.showerror("registro","registro fallido la fecha debe tener el formato dd/mm/yyyy")
#_______________________________________________________________________________________________________________________
    # Esta regex solo permitirá correos de dominio Gmail , Hotmail y Outlook
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@](gmail\.com|hotmail\.com|outlook\.com)$'
#_______________________________________________________________________________________________________________________
    if gender=="":#si la casilla de genero esta vacia
        mb.showerror("registro","registro fallido rellene las casillas de masculino o femenino")
        
#_______________________________________________________________________________________________________________________
    elif attendance=="":#si la casilla de asistencia esta vacia
        mb.showerror("registro","registro fallido rellene las casillas de si requiere asistencia o no")
#_______________________________________________________________________________________________________________________
    elif name=="" or lastname=="" or id=="" or telephone=="" or nationality=="" or email=="":#si alguna casilla esta vacia
        mb.showerror("registro","registro fallido rellene todas las casillas")
#_______________________________________________________________________________________________________________________
    elif not id.isdigit():#si la identificacion es digito o no
        mb.showerror("registro","registro fallido la identificacion debe ser un numero")
#_______________________________________________________________________________________________________________________
    elif len(id)<7 or len(id)>=11:#si la identificacion es menor a 7 digitos o mayor a 10
        mb.showerror("registro","registro fallido la identificacion debe tener 10 digitos") 
#____________________________________________________________________________________________________________________

    elif not telephone.isdigit(): # si el telefono es digito o no
        mb.showerror("registro","registro fallido  telefono debe ser un numero")
#____________________________________________________________________________________________________________________

    elif not re.search(regex, email): # si el correo no es de un dominio permitido
        mb.showerror("registro","registro fallido el dominio del correo no es valido")
#____________________________________________________________________________________________________________________

    elif len(telephone)!=10:
        mb.showerror("registro","registro fallido el telefono debe tener 10 digitos")#si el telefono no tiene 10 digitos
        
#____________________________________________________________________________________________________________________
    elif nationality.capitalize() not in countries:    #si la nacionalidad no esta en la lista de paises
        mb.showerror("registro","registro fallido la nacionalidad no es valida")
    
#____________________________________________________________________________________________________________________

    # comprobacion de que los datos no esten repetidos
    else:
        if  os.path.isfile("registro_usuarios.csv"):
            df=pd.read_csv("registro_usuarios.csv",sep=";")
            
            if  int(id) in  df["documento"].values:
                mb.showerror("registro","registro fallido la identificacion ya existe") #si la identificacion ya existe
                return

            elif email in df["correo"].values:
                mb.showerror("registro","registro fallido el correo esta registrado en otro usuario")
                return

            elif int(telephone) in df["telefono"].values:
                mb.showerror("registro","registro fallido el telefono ya existe")
                return
        
        sv.record_base(gender,name,lastname,id,telephone,nationality,email,birthday,attendance,window)



def condition_login(id,email):#funcion que valida el login
    if os.path.isfile("registro_usuarios.csv"):#si el archivo csv existe
        df=pd.read_csv("registro_usuarios.csv")#se lee el archivo csv
        if int(id) in df["documento"].values and email in df["correo"].values:#si los datos coinciden
            mb.showinfo("login","login exitoso")
        else:
            mb.showerror("login","login fallido los datos no coinciden")
    
    if id == "" or email == "":
        mb.showerror("login","rellene todas las casillas")#si alguna casilla esta vacia
    else:
        if os.path.isfile("registro_usuarios.csv"):#si el archivo csv existe
            df=pd.read_csv("registro_usuarios.csv")#se lee el archivo csv
            if int(id) in df["documento"].values and email in df["correo"].values:#si los datos coinciden
                mb.showinfo("login","login exitoso")
            else:
                mb.showerror("login","login fallido los datos no coinciden")#si los datos no coinciden
        else:
            mb.showerror("login","login fallido no hay usuarios registrados")#si no hay usuarios registrados

def lista_vuelos():#funcion que retorna la lista de vuelos
    df = pd.read_csv("dato_vuelo.csv", sep=",")#se lee el archivo csv
    origen = set(df['CiudadOrigen']) #se obtiene la columna "CiudadOrigen"
    destino = set(df["CiudadDestino"]) #se obtiene la columna "CiudadDestino"
    fecha = set(df['Fecha']) #se obtiene la columna "Fecha"
    return origen, destino, fecha

        
def conditions_search(origin,destination,passenger,going,window,peoples):
    if origin=="" or destination=="" or passenger=="":
        mb.showerror("error","rellene todas las casillas") 
        return
    elif not int(passenger.isdigit()):
        mb.showerror("error","el numero de pasajeros debe ser un numero")
        return
    elif origin==destination or destination==origin:
        mb.showerror("error","la ciudad de origen y destino no pueden ser iguales")
        return
    elif going  == "":
        mb.showerror("error","rellene la casilla de ida")
        return
    else:
        indices=search(origin,destination)
        if indices==None:
            mb.showerror("error","no hay vuelos disponibles")
            return
        else:
            mn.search_fly(indices,window,peoples)
def search(origin,destination):
    indices=[]
    df=pd.read_csv("dato_vuelo.csv",sep=",")
    for i in range(len(df)):
        if destination in df["CiudadDestino"].values[i] and origin in df["CiudadOrigen"].values[i]  :
            indices.append(i)
        else:
            continue
    if len(indices)==0:
        mb.showerror("error","no hay vuelos disponibles")
    else:
        return indices

def search_hours(indice):
    df=pd.read_csv("dato_vuelo.csv",sep=",")
    horas=[]
    for i in range(len(df)):
        if  df['Fecha'].values[i]==df['Fecha'].values[indice] and df['CiudadOrigen'].values[i]==df['CiudadOrigen'].values[indice] and df['CiudadDestino'].values[i]==df['CiudadDestino'].values[indice]:
            horas.append(i)
    return horas

def getnums(text): #funcion que retorna los numeros de un string
    nums=[]
    for i in range(len(text)): #    se recorre el string
        if text[i].isdigit():   #si el caracter es un digito
            nums.append(text[i]) #se agrega a la lista
    return int("".join(nums)) #se retorna la lista de numeros
