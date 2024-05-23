import tkinter as tk 
from tkinter import messagebox as mb
import pandas as pd
import datetime 
import re
import pycountry
import os

def conditions_record(gender,name,lastname,id,telephone,nationality,email,birthday,attendance):
    if  os.path.isfile("registro_usuarios.csv"):
        df=pd.read_csv("registro_usuarios.csv",sep=";")
        if  int(id) in  df["documento"].values:
            mb.showerror("registro","registro fallido la identificacion ya existe") #si la identificacion ya existe

        elif email in df["correo"].values:
            mb.showerror("registro","registro fallido el correo esta registrado en otro usuario")
        
        elif int(telephone) in df["telefono"].values:
            mb.showerror("registro","registro fallido el telefono ya existe")
        
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
        
        mb.showinfo("registro","registro exitoso") #si todo esta correcto
        return True



def condition_login(id,email):#funcion que valida el login
    
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

def lista_vuelos(origen,destino,fecha):#funcion que retorna las listas de origen,destino y fecha
    df=pd.read_csv("dato_vuelo.csv",sep=",")#se lee el archivo csv
    origen = df['CiudadOrigen'].tolist()
    destino = df["CiudadDestino"].tolist()
    fecha = df['Fecha'].tolist()
    return origen,destino,fecha

        
def conditions_search(origin,destination,passenger):
    if origin=="" or destination=="" or passenger=="":
        mb.showerror("error","rellene todas las casillas") 
    elif not int(passenger.isdigit()):
        mb.showerror("error","el numero de pasajeros debe ser un numero")
    else:
        return True

def search(origin,destination):
    indices=[]
    df=pd.read_csv("dato_vuelo.csv",sep=",")
    for i in range(len(df)):
        if origin in df["CiudadOrigen"].values[i] and destination in df["CiudadDestino"].values[i]:
            indices.append(i)
        else:
            continue
    if len(indices)==0:
        mb.showerror("error","no hay vuelos disponibles")
    else:
        return indices