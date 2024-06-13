import tkinter as tk
from tkinter import messagebox as mb
from tkinter import PhotoImage
from tkinter import ttk
import pandas as pd
import os
import PIL as pil
from PIL import ImageTk, Image, ImageOps


import conditions as c
import save as s
import datetime
from tkcalendar import Calendar

import funciones_categorias as fc

import customtkinter as ctk


ctk.set_appearance_mode("light")

def functions(function):
    function


def fly(window_search=None): 
    
    
    if window_search is not None:
        window_search.destroy()

    origen, destino, fecha = c.lista_vuelos()

    # Creación de la ventana de menú fly
    window_fly = ctk.CTk()
    window_fly.title("Fly_Heaven")
    window_fly.geometry("1850x1900+0+0")
    
    window_fly.iconbitmap("fly_heaven.ico")
    label = ctk.CTkLabel(window_fly, text="")
    label = ctk.CTkLabel(window_fly, text="")
    label.grid(row=0, column=0)
    
    #imagen banner
    image_logo = ctk.CTkImage(dark_image=Image.open(fr"imagenes\Heaven.png"), size=(200, 700))
    image_logo = ctk.CTkLabel(window_fly, image=image_logo,text ="")
    image_logo.place(x = 50, y = 40)
    

    # Crear una lista de días de junio
    dates_june = []
    for day in range(1, 31):
        date = datetime.datetime(2024, 6, day)
        if date.weekday() in [2, 3]:  # 2 es miércoles, 3 es jueves
            dates_june.append(date.strftime("%Y-%m-%d"))
    dates_june = []
    for day in range(1, 31):
        date = datetime.datetime(2024, 6, day)
        if date.weekday() in [2, 3]:  # 2 es miércoles, 3 es jueves
            dates_june.append(date.strftime("%Y-%m-%d"))

    going = ctk.StringVar()

    # Creación de frame para los widgets de la búsqueda
    frame_busqueda = ctk.CTkFrame(window_fly, fg_color="DodgerBlue3")
    
    
    frame_busqueda.place(x=400,y=50)

    # Creación de elementos de la pantalla de menú fly dentro del frame: frame_busqueda
    label_passenger = ctk.CTkLabel(frame_busqueda,text="Número de pasajeros",text_color="white")
    entry_passenger = ctk.CTkEntry(frame_busqueda)
    space = ctk.CTkLabel(frame_busqueda, text="")
    space = ctk.CTkLabel(frame_busqueda, text="")
    only_going = ctk.CTkRadioButton(
    frame_busqueda, text="Solo ida",text_color="white", variable=going, value=2, height=5, width=10)
    cities_origin = ctk.CTkComboBox(
    frame_busqueda, values=list(origen), state="readonly")
    cities_origin.set("Ciudad de origen")
    cities_destination = ctk.CTkComboBox(
    frame_busqueda, values=list(destino), state="readonly")
    cities_destination.set("Ciudad de destino")
    list_going = ctk.CTkComboBox(
    frame_busqueda, values=dates_june, state="readonly")
    list_going.set("ida")

    # Creación de frame para el botón de búsqueda
    frame_button_search = ctk.CTkFrame(
        window_fly, width=100, height=50, fg_color="#EBEBEB")
    frame_button_search.place(x=700, y=160)

    button_search = ctk.CTkButton(
        frame_button_search, text="BUSCAR",
        command=lambda: c.conditions_search(
            cities_destination.get(), cities_origin.get(),
            going.get(), window_fly,
            entry_passenger.get()),
        width=90, height=40
    )

    # Posicionar los elementos de la pantalla de menú fly
    cities_origin.grid(row=8, column=0)
    cities_destination.grid(row=8, column=1)
    list_going.grid(row=8, column=2, padx=10, pady=10)
    space.grid(row=0, column=0)
    only_going.grid(row=1, column=0)
    space.grid(row=0, column=0)
    only_going.grid(row=1, column=0)
    button_search.grid(row=2, column=0, padx=10, pady=10)
    label_passenger.grid(row=8, column=5, padx=10, pady=10)
    entry_passenger.grid(row=8, column=6, padx=10, pady=10)

    # frame principal del scroll
    frame_vuelos = ctk.CTkScrollableFrame(
    window_fly, fg_color="white", width=1000, height=400)
    frame_vuelos.place(x=300,y=350)

    # ______________________________________________________

    # Crear el frame para Cali
    frame_cali = ctk.CTkFrame(frame_vuelos, fg_color="white",
                              border_color="DodgerBlue3", border_width=3, width=400, height=300)
    frame_cali.grid(row=1, column=0, padx=1, pady=1)

    # Label para Cali
    label_cali = ctk.CTkLabel(frame_cali, text="Cali",
                              fg_color="DodgerBlue3", font=("Times New Roman", 25))
    label_cali.grid(row=0, column=0, padx=10, pady=10)

    # Cargar la imagen con CTkImage
    imagen_path = "imagenes/cali.png"
    imagen_cali = ctk.CTkImage(
        dark_image=Image.open(imagen_path), size=(300, 100))

    # Crear un Label para mostrar la imagen
    label_imagen_cali = ctk.CTkLabel(frame_cali, image=imagen_cali,text="")
    label_imagen_cali.grid(row=1, column=0, padx=10, pady=10)

    # Label para información de Cali
    label_info_cali = ctk.CTkLabel(frame_cali, text="""Es conocida como la capital mundial de la salsa y es uno de los principales centros deportivos de Colombia.
    En el año 2019 ha sido galardonado
    por los World Travel Awards como ciudad destino cultural de Suramérica, 
    gracias a su oferta cultural deportiva y turística.""", font=("Times New Roman", 20))
    label_info_cali.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Medellín
    frame_medellin = ctk.CTkFrame(frame_vuelos, fg_color="white",
                                  border_color="DodgerBlue3", border_width=3, width=400, height=300)
    frame_medellin.grid(row=0, column=0, padx=10, pady=10)
    label_medellin = ctk.CTkLabel(
    frame_medellin, text="Medellín", fg_color="DodgerBlue3", font=("Times New Roman", 20))
    label_medellin.grid(row=0, column=0, padx=10, pady= 10)
    imagen_path = "imagenes/medellin.png"
    imagen_medellin = ctk.CTkImage(
        dark_image=Image.open(imagen_path), size=(300, 100))
    label_imagen_medellin = ctk.CTkLabel(frame_medellin, image=imagen_medellin,text="")
    label_imagen_medellin.grid(row=1, column=0, padx=10, pady=10)
    label_info_medellin = ctk.CTkLabel(frame_medellin, text="""Es conocida como la capital de la montaña y la ciudad de la eterna primavera.
    Es la segunda ciudad más grande de Colombia y es un importante centro económico y cultural.""", font=("Times New Roman", 20))
    label_info_medellin.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Bogotá
    frame_bogota = ctk.CTkFrame(frame_vuelos, fg_color="white",
                                border_color="DodgerBlue3", border_width=3, width=400, height=300)
    frame_bogota.grid(row=2, column=0, padx=10, pady=10)
    label_bogota = ctk.CTkLabel(
        frame_bogota, text="Bogotá", fg_color="DodgerBlue3", font=("Times New Roman", 25))
    label_bogota.grid(row=0, column=0, padx=10, pady=10)
    imagen_path = "imagenes/bogota.png"
    imagen_bogota = ctk.CTkImage(
        dark_image=Image.open(imagen_path), size=(300, 100))
    label_imagen_bogota = ctk.CTkLabel(frame_bogota, image=imagen_bogota,text ="")
    label_imagen_bogota.grid(row=1, column=0, padx=10, pady=10)
    label_info_bogota = ctk.CTkLabel(frame_bogota, text="""Es la capital de Colombia y es la ciudad más grande del país.
    Es el centro político, económico, administrativo, industrial, artístico, cultural, deportivo y turístico de Colombia.""", font=("Times New Roman", 20))
    label_info_bogota.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Cartagena
    frame_cartagena = ctk.CTkFrame(
        frame_vuelos, fg_color="white", border_color="blue", border_width=3, width=400, height=300)
    frame_cartagena.grid(row=3, column=0, padx=10, pady=10)
    label_cartagena = ctk.CTkLabel(
        frame_cartagena, text="Cartagena", fg_color="DodgerBlue3", font=("Times New Roman", 20))
    label_cartagena.grid(row=0, column=0, padx=10, pady=10)
    imagen_path = "imagenes/cartagena.png"
    imagen_cartagena = ctk.CTkImage(
        dark_image=Image.open(imagen_path), size=(300, 100))
    label_imagen_cartagena = ctk.CTkLabel(
        frame_cartagena, image=imagen_cartagena,text ="")
    label_imagen_cartagena.grid(row=1, column=0, padx=10, pady=10)
    label_info_cartagena = ctk.CTkLabel(frame_cartagena, text="""Es conocida como la ciudad amurallada y es uno de los destinos turísticos más importantes de Colombia.
    Es un importante centro turístico, histórico y cultural.""", font=("Times New Roman", 20))
    label_info_cartagena.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Santa Marta
    frame_santamarta = ctk.CTkFrame(
        frame_vuelos, fg_color="white", border_color="blue", border_width=3, width=400, height=300)
    frame_santamarta.grid(row=5, column=0, padx=1, pady=1)
    label_santamarta = ctk.CTkLabel(
        frame_santamarta, text="Santa Marta", fg_color="DodgerBlue3", font=("Times New Roman", 20))
    label_santamarta.grid(row=0, column=0, padx=10, pady=10)
    imagen_path = "imagenes/santa_marta.png"
    imagen_santamarta = ctk.CTkImage(
        dark_image=Image.open(imagen_path), size=(300, 100))
    label_imagen_santamarta = ctk.CTkLabel(
        frame_santamarta, image=imagen_santamarta)
    label_imagen_santamarta.grid(row=1, column=0, padx=10, pady=10)
    label_info_santamarta = ctk.CTkLabel(frame_santamarta, text="""Es conocida como la perla de América y es uno de los destinos turísticos más importantes de Colombia.
    Es un importante centro turístico, histórico y cultural.""", font=("Times New Roman", 20))
    label_info_santamarta.grid(row=2, column=0, padx=10, pady=10)

    window_fly.mainloop()


# Función para buscar vuelos disponibles


def search_fly(indices, window_fly, peoples):
    window_fly.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    window_search = ctk.CTk()
    window_search.geometry("1850x1900+0+0")
    window_search.state("zoomed")
    window_search.resizable(0, 0)
    window_search.title("Búsqueda de vuelos")

    # Crear frame para el label
    frame_label = ctk.CTkFrame(window_search, fg_color="#EBEBEB",border_color= "blue", border_width=3)
    frame_label.place(x = 600 , y = 50)
    label = ctk.CTkLabel(
        frame_label,font = ("Times New Roman", 40),text=f"IDA: de {df['CiudadOrigen'].values[indices[0]]} a {
            df['CiudadDestino'].values[indices[0]]}"
    )
    label.grid(row=0, column=0)

    # Crear frame con scrollbar para los botones
    frame_buttons = ctk.CTkScrollableFrame(
    window_search, width=1000, height=350)
    frame_buttons.place(relx=0.5, rely=0.4, anchor="center")

    

    # Crear botones dentro del frame con scrollbar
    for i in indices:
        mensaje = f"""Vuelo: {df['Vuelo'].values[i]}
        Fecha: {df['Fecha'].values[i]}
        Desde ${int(df['ValorMin'].values[i])} COP"""
        button = ctk.CTkButton(
            frame_buttons, text=mensaje,font = ("Times New Roman", 40),
            command=lambda i=i: functions(
                info_buy(i, window_search, indices, peoples)),
            width=1000, height=150
        )
        button.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    # Crear frame para el botón de regreso
    # Crear frame para el botón de regreso
    frame_button_back = ctk.CTkFrame(window_search, fg_color="#EBEBEB")
    frame_button_back.place(relx=0.5, rely=0.9, anchor="center")
    
    # Crear el botón de regreso
    button_back = ctk.CTkButton(
        frame_button_back, font=("Times New Roman", 40), text="VOLVER",
        command=lambda: functions(fly(window_search)),
        width=200, height=100
    )
    button_back.grid(row=2, column=0, padx=10, pady=10)

    window_search.mainloop()

# Información de vuelos disponibles en tales horas
def info_buy(indice, window, indices, peoples):
    if window is not None:
        window.destroy()

    hours = c.search_hours(indice)
    df = pd.read_csv("dato_vuelo.csv")
    window_info = ctk.CTk()
    window_info.geometry("1850x1900+0+0")
    
    frame_hours_f = ctk.CTkFrame(window_info, fg_color="white", border_color="blue", border_width=3, width=1000, height=300)
    frame_hours_f.place(x=250, y=200)
    
    label_hours = ctk.CTkLabel(frame_hours_f, text="Vuelos disponibles", font=("Times New Roman", 20))
    label_hours.grid(row=0, column=0, pady=(10, 0))
    
    scroll_hours = ctk.CTkScrollableFrame(frame_hours_f, width=1000, height=300, fg_color="white")
    scroll_hours.grid(row=1, column=0, pady=10)
    
    row_counter = 0
    for i in hours:
        mensaje = f"""Vuelo: {df['Vuelo'].values[i]}
        Hora salida: {df['HoraSalida'].values[i]}
        Hora llegada: {df['HoraLlegada'].values[i]}"""
        button_hours = ctk.CTkButton(
            scroll_hours, text=mensaje, font=("Times New Roman", 30),
            command=lambda i=i: functions(buy(i, window_info, hours, peoples)),
            width=300, height=100
        )
        button_hours.grid(row=row_counter, column=0, padx=(350, 0), pady=10, sticky="EW")
        row_counter += 1
        
    button_back = ctk.CTkButton(
        window_info, text="VOLVER", font=("Times New Roman", 30),
        command=lambda: functions(search_fly(indices, window_info, peoples)),
        width=300, height=100
    )
    button_back.place(relx=0.5, rely=0.9, anchor='s', y=-10)  # y=-10 to give some padding from the bottom

    window_info.mainloop()


def mostrar_vuelos(df, frame):
    # Limpiar el frame de vuelos anteriores
    for widget in frame.winfo_children():
        widget.destroy()

    # Asumiendo que existe una función para mostrar cada vuelo en el frame
    for i, row in df.iterrows():
        # Mostrar cada vuelo en el frame
        # Esta es una simplificación, deberías ajustar según cómo quieras mostrar los vuelos
        label = ctk.CTkLabel(frame, text=f"Vuelo: {row['Vuelo']} - Precio: {row['ValorMin']} a {row['ValorMax']}")
        label.pack()


def buy(indice, window, indices, peoples):
    if window is not None:
        window.destroy()

    df = pd.read_csv("dato_vuelo.csv")
    window_buy = ctk.CTk()
    window_buy.geometry("1850x1900+0+0")
    label = ctk.CTkLabel(window_buy, text="Compra de paquetes")
    label.grid(row=0, column=0)
    label1 = ctk.CTkLabel(window_buy, text="Selecciona alguno de los paquetes")
    label1.grid(row=1, column=0)

    frame_1 = ctk.CTkFrame(window_buy)
    frame_1.grid(row=2, column=0)
    label_1 = ctk.CTkLabel(
        frame_1, text=f"""Aluminio:
    1 artículo personal (bolso) (Debe caber debajo del asiento)
    1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
    Asiento Estándar (Sujeto a disponibilidad)
    Cambios de vuelo (No es permitido)
    Reembolso (No es permitido)
    PRECIO: {df['ValorMin'].values[indice]}"""
    )
    label_1.grid(row=0, column=0)
    button_aluminio = ctk.CTkButton(frame_1, text="Comprar", width=20,
                                    height=2, command=lambda: fc.aluminum(indice, window_buy, peoples, df["ValorMin"].values[indice]))
    button_aluminio.grid(row=1, column=0)

    frame_2 = ctk.CTkFrame(window_buy)
    frame_2.grid(row=1, column=1)
    label_2 = ctk.CTkLabel(
        frame_2, text=f"""Diamante:
    1 artículo personal (bolso) (Debe caber debajo del asiento)
    1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
    Asiento Estándar (Sujeto a disponibilidad)
    Cambios de vuelo (Permitido con costo adicional)
    Reembolso (Permitido con costo adicional)
    PRECIO: {df['ValorMedio'].values[indice]}"""
    )
    label_2.grid(row=0, column=0)
    button_diamond = ctk.CTkButton(frame_2, text="Comprar", width=20, height=2,)
    button_diamond.grid(row=1, column=0)

    frame_3 = ctk.CTkFrame(window_buy)
    frame_3.grid(row=2, column=3)
    label_3 = ctk.CTkLabel(
        frame_3, text=f"""Premium:
    1 artículo personal (bolso) (Debe caber debajo del asiento)
    1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
    Asiento Preferencial (Incluido)
    Cambios de vuelo (Permitido sin costo adicional)
    Reembolso (Permitido)
    PRECIO : {df['ValorMax'].values[indice]}"""
    )
    label_3.grid(row=0, column=0)
    button_premium = ctk.CTkButton(frame_3, text="Comprar", width=20, height=2)
    button_premium.grid(row=1, column=0)

    window_buy.mainloop()

# Usuario escoge asiento solo si es premium


def choose_sit(indice=None, window=None, indices=None):
    if window is not None:
        window.destroy()

    df = pd.read_csv("dato_vuelo.csv")

    # Creación de ventana para la elección de asiento
    window_buy = ctk.CTk()
    window_buy.geometry("1250x750")
    window_buy.resizable(0, 0)
    window_buy.iconbitmap("fly_heaven.ico")
    window_buy.title("Elección de asiento")

    # Creación de frame label a, b, c, d, e, f
    frame_label = ctk.CTkFrame(window_buy)
    label_sit = ctk.CTkLabel(
        frame_label, text="A    B      C      D      E      F")
    label_sit.grid(row=0, column=0)
    frame_label.place(relx=0.5, rely=0.0, anchor="n")

    # Creación de asientos
    frame_sits = ctk.CTkFrame(window_buy)
    frame_sits.place(relx=0.5, rely=0.1, anchor="n")
    matriz = []
    for i in range(12):
        buttons = []
        for j in range(6):
            button_sit = ctk.CTkButton(
                frame_sits, text=f"{chr(65+j)}{i+1}", width=5, height=2)
            button_sit.grid(row=i, column=j, padx=10, pady=10)
            text = c.getnums(button_sit.cget("text"))
            if text >= 9:
                button_sit.configure(fg_color="green", state="disabled")
            elif text >= 5:
                button_sit.configure(fg_color="red", state="disabled")
            else:
                button_sit.configure(fg_color="blue")
            buttons.append(button_sit)
        matriz.append(buttons)

    # Frame label categorías
    frame_premium = ctk.CTkFrame(window_buy)
    label_premium = ctk.CTkLabel(frame_premium, text="Asientos premium")
    frame_premium.place(relx=0.8, rely=0.2, anchor="e")
    label_premium.grid(row=0, column=0)

    frame_diamond = ctk.CTkFrame(window_buy)
    label_diamond = ctk.CTkLabel(frame_diamond, text="Asientos diamond")
    frame_diamond.place(relx=0.8, rely=0.4, anchor="e")
    label_diamond.grid(row=0, column=0)

    frame_aluminio = ctk.CTkFrame(window_buy)
    label_aluminio = ctk.CTkLabel(frame_aluminio, text="Asientos aluminio")
    frame_aluminio.place(relx=0.8, rely=0.7, anchor="e")
    label_aluminio.grid(row=0, column=0)

    window_buy.mainloop()


# ______________________________________________________
    # darle posicion a los botones y elementos de la pantalla de busqueda de vuelos


def record_check_in(window, peoples, indice, sits, price):
    window.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    window_record = ctk.CTk()
    window_record.title("Registro")
    window_record.geometry("1920x1080")
    window_record.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # frame del responsable de pago

    # frame de acompañantes
    frame_acompanantes = ctk.CTkScrollableFrame(
        window_record, fg_color="grey26", border_color="green", border_width=3, width=1000, height=300)
    frame_acompanantes.grid(row=1, column=0)

    # frame de información de vuelo
    frame_info_fly = ctk.CTkFrame(window_record, fg_color="grey26",
                                  border_color="green", border_width=2, width=500, height=300)
    frame_info_fly.grid(row=0, column=0, padx=10, pady=30)
    label_fly = ctk.CTkLabel(frame_info_fly, text="Información de vuelo")
    label_fly.grid(row=0, column=0)
    label_fly1 = ctk.CTkLabel(frame_info_fly, text=f"Vuelo: {
                              df['Vuelo'].values[indice]}")
    label_hour = ctk.CTkLabel(frame_info_fly, text=f"Hora de salida: {
                              df['HoraSalida'].values[indice]}")
    label_hour1 = ctk.CTkLabel(frame_info_fly, text=f"Hora de llegada: {
                               df['HoraLlegada'].values[indice]}")
    label_price = ctk.CTkLabel(frame_info_fly, text=f"Precio: {price}")
    label_fly1.grid(row=1, column=0)
    label_hour.grid(row=2, column=0)
    label_hour1.grid(row=3, column=0)
    label_price.grid(row=4, column=0)

    # hora de salida
    frame_hours_f = ctk.CTkFrame(
        window_record, fg_color="grey26", border_color="green", border_width=2)
    frame_hours_f.grid(row=0, column=0)
    label_hours = ctk.CTkLabel(frame_hours_f, text="Información de vuelo")
    label_hours.grid(row=0, column=0)

    datas = []
    for i in range(peoples):
        help = []
        # label y entry de acompañantes
        frame_persona = ctk.CTkFrame(
            frame_acompanantes, fg_color="grey26", border_color="green", border_width=2)
        frame_persona.grid(row=i, column=0, padx=10, pady=30)
        label_acompanantes = ctk.CTkLabel(frame_persona, text=f"Acompañante {
                                          i+1} \t asiento: {sits[i]}")
        # posicion de los elementos
        label_acompanantes.grid(row=0, column=0, padx=10, pady=10)

        genero = ctk.StringVar()
        # radiobutton de genero
        radio_m = ctk.CTkRadioButton(
            frame_persona, text="Masculino", variable=genero, value="Masculino")
        radio_f = ctk.CTkRadioButton(
            frame_persona, text="Femenino", variable=genero, value="Femenino")
        # posicion de los elementos
        radio_m.grid(row=1, column=0, padx=10, pady=10)
        radio_f.grid(row=1, column=1, padx=10, pady=10)

        label_name = ctk.CTkLabel(frame_persona, text="Primer nombre")
        entry_name = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_name.grid(row=1, column=2, padx=10, pady=10)
        entry_name.grid(row=1, column=3, padx=10, pady=10)

        label_last_name = ctk.CTkLabel(frame_persona, text="Primer apellido")
        entry_last_name = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_last_name.grid(row=1, column=4, padx=10, pady=10)
        entry_last_name.grid(row=1, column=5, padx=10, pady=10)

        label_id = ctk.CTkLabel(frame_persona, text="Identificación")
        entry_id = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_id.grid(row=2, column=0, padx=10, pady=10)
        entry_id.grid(row=2, column=1, padx=10, pady=10)

        label_nationality = ctk.CTkLabel(frame_persona, text="Nacionalidad")
        entry_nationality = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_nationality.grid(row=2, column=2, padx=10, pady=10)
        entry_nationality.grid(row=2, column=3, padx=10, pady=10)

        label_email = ctk.CTkLabel(frame_persona, text="Correo")
        entry_email = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_email.grid(row=2, column=4, padx=10, pady=10)
        entry_email.grid(row=2, column=5, padx=10, pady=10)

        label_telephone = ctk.CTkLabel(frame_persona, text="Teléfono")
        entry_telephone = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_telephone.grid(row=3, column=0, padx=10, pady=10)
        entry_telephone.grid(row=3, column=1, padx=10, pady=10)

        asistencia = ctk.StringVar()
        label_asistencia = ctk.CTkLabel(
            frame_persona, text="Requiere Asistencia")
        radio_si = ctk.CTkRadioButton(
            frame_persona, text="Si", variable=asistencia, value="Si")
        radio_no = ctk.CTkRadioButton(
            frame_persona, text="No", variable=asistencia, value="No")

        label_asistencia.grid(row=3, column=2, padx=10, pady=10)
        radio_si.grid(row=3, column=3, padx=10, pady=10)
        radio_no.grid(row=3, column=4, padx=10, pady=10)

        label_birth = ctk.CTkLabel(frame_persona, text="Fecha de nacimiento")
        entry_birth = ctk.CTkEntry(frame_persona)
        # posicion de los elementos
        label_birth.grid(row=4, column=0, padx=10, pady=10)
        entry_birth.grid(row=4, column=1, padx=10, pady=10)

        help = [genero, entry_name, entry_last_name, entry_id, entry_nationality,
                entry_email, entry_telephone, entry_birth, asistencia]
        datas.append(help)
    # boton de enviar
    button_send = ctk.CTkButton(frame_acompanantes, hover_color="green", text="Enviar",
                                command=lambda: c.conditions_record(peoples, 9, datas, sits, indice, window_record), width=9, height=2)
    button_send.grid(row=peoples, column=0, padx=10, pady=10)

    window_record.mainloop()

# ARREGLAR ESTA FUNCION PARA HACER LA CONFIRMACION DE VUELO (CHECK IN)


def pay_sits(window, peoples, datas, sits, indice):
    window.destroy()
    window_pay = ctk.CTk()
    window_pay.title("Iniciar sesión")
    window_pay.geometry("400x400")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Crear frame para los widgets de
    pay_frame = ctk.CTkFrame(
        window_pay, fg_color="grey26", width=100, height=300)
    pay_frame.grid(row=0, column=0)
    label = ctk.CTkLabel(pay_frame, text="Pago")
    label.grid(row=0, column=0)

    label_name = ctk.CTkLabel(
        pay_frame, text="Nombre completo del titular de la tarjeta")
    entry_name = ctk.CTkEntry(pay_frame)
    label_name.grid(row=1, column=0)
    entry_name.grid(row=1, column=1)

    label_number = ctk.CTkLabel(pay_frame, text="Número de la tarjeta")
    entry_number = ctk.CTkEntry(pay_frame)
    label_number.grid(row=2, column=0)
    entry_number.grid(row=2, column=1)

    label_date = ctk.CTkLabel(pay_frame, text="Fecha de vencimiento")
    entry_date = ctk.CTkEntry(pay_frame)
    label_date.grid(row=3, column=0)
    entry_date.grid(row=3, column=1)

    label_cvv = ctk.CTkLabel(pay_frame, text="CVV")
    entry_cvv = ctk.CTkEntry(pay_frame)
    label_cvv.grid(row=4, column=0)
    entry_cvv.grid(row=4, column=1)
    pay_client = [entry_name, entry_number, entry_date, entry_cvv]
    button_pay = ctk.CTkButton(pay_frame, text="Pagar", command=lambda: c.conditions_pay(
        window_pay, pay_client, peoples, datas, sits, indice), width=100, height=10)
    button_pay.grid(row=5, column=0, padx=10, pady=10)
    window_pay.mainloop()

def tickets(window, peoples, datas, sits, indice):
    window.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    window_tickets = ctk.CTk()
    window_tickets.geometry("1000x1000")
    window_tickets.title("Tickets")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    frame_scroll = ctk.CTkScrollableFrame(window_tickets, width=600, height=300)
    frame_scroll.grid(row=0, column=0)
    for i in range(peoples):
            frame_ticket = ctk.CTkFrame(frame_scroll, fg_color="grey26", border_color="green", border_width=2)
            frame_ticket.grid(row=i, column=0, padx=10, pady=30)
            combinacion = fc.randomiser()
            label = ctk.CTkLabel(frame_ticket, text=f"Pase de abordaje")
            label.grid(row=0, column=0, padx=10, pady=10)
            label_name = ctk.CTkLabel(frame_ticket, text=f"Nombre: {datas[i][1]} {datas[i][2]}")
            label_name.grid(row=1, column=0, padx=10, pady=10)
            label_origin = ctk.CTkLabel(frame_ticket, text=f"Origen: {df['CiudadOrigen'].values[indice]}")
            label_origin.grid(row=2, column=0, padx=10, pady=10)
            label_destiny = ctk.CTkLabel(frame_ticket, text=f"Destino: {df['CiudadDestino'].values[indice]}")
            label_destiny.grid(row=3, column=0, padx=10, pady=10)
            label_hour = ctk.CTkLabel(frame_ticket, text=f"Hora de salida: {df['HoraSalida'].values[indice]}")
            label_hour.grid(row=3, column=1 , padx=10, pady=10)
            label_hour1 = ctk.CTkLabel(frame_ticket, text=f"Hora de llegada: {df['HoraLlegada'].values[indice]}")
            label_hour1.grid(row=3, column=2 , padx=10, pady=10)
            label_fly = ctk.CTkLabel(frame_ticket, text=f"Vuelo: {df['Vuelo'].values[indice]}")
            label_fly.grid(row=1, column=1, padx=10, pady=10)
            label_code = ctk.CTkLabel(frame_ticket, text=f"Código de abordaje: {combinacion}")
            label_code.grid(row=4, column=0, padx=10, pady=10)
    window_tickets.mainloop()
            
            
                    
        


if __name__ == '__main__':
    functions(fly())
