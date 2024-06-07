from tkinter import messagebox as mb
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

def functions(function):
    function

def fly(window_search=None):
    if window_search is not None:
        window_search.destroy()
        
    origen, destino, fecha = c.lista_vuelos()
    
    # Creación de la ventana de menú fly
    window_fly = ctk.CTk()
    window_fly.title("Fly_Heaven")
    window_fly.geometry("850x500")
    window_fly.iconbitmap("fly_heaven.ico")
    label = ctk.CTkLabel(window_fly, text="")
    label = ctk.CTkLabel(window_fly, text="")
    label.grid(row=0, column=0)

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
    frame_busqueda = ctk.CTkFrame(window_fly, fg_color="grey26")
    frame_busqueda.grid(row=0, column=0)
    
    # Creación de elementos de la pantalla de menú fly dentro del frame: frame_busqueda
    label_passenger = ctk.CTkLabel(frame_busqueda, text="Número de pasajeros")
    entry_passenger = ctk.CTkEntry(frame_busqueda)
    space = ctk.CTkLabel(frame_busqueda, text="")
    space = ctk.CTkLabel(frame_busqueda, text="")
    only_going = ctk.CTkRadioButton(frame_busqueda, text="Solo ida", variable=going, value=2, height=5, width=10)
    cities_origin = ctk.CTkComboBox(frame_busqueda, values=list(origen), state="readonly")
    cities_origin.set("Ciudad de origen")
    cities_destination = ctk.CTkComboBox(frame_busqueda, values=list(destino), state="readonly")
    cities_destination.set("Ciudad de destino")
    list_going = ctk.CTkComboBox(frame_busqueda, values=dates_june, state="readonly")
    list_going.set("ida")
    
    # Creación de frame para el botón de búsqueda
    frame_button_search = ctk.CTkFrame(window_fly, width=100, height=50, fg_color="grey26")
    frame_button_search.grid(row=1, column=0)
    
    button_search = ctk.CTkButton(
        frame_button_search, text="BUSCAR",
        command=lambda: c.conditions_search(
            cities_destination.get(), cities_origin.get(),
            entry_passenger.get(), going.get(), window_fly,
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
    
    frame_vuelos = ctk.CTkScrollableFrame(window_fly, fg_color="grey26",width=500,height=200)
    frame_vuelos.grid(row=2, column=0)
    label_vuelos = ctk.CTkLabel(frame_vuelos, text="Lugares")
    label_vuelos.grid(row=0, column=0,columnspan=2 , padx=10, pady=10)
    
    
    # Crear el frame para Cali
    frame_cali = ctk.CTkFrame(frame_vuelos, fg_color="grey26",border_color="blue",border_width=2)
    frame_cali.grid(row=2, column=0, padx=10, pady=10)

    # Label para Cali
    label_cali = ctk.CTkLabel(frame_cali, text="Cali",fg_color="skyblue")
    label_cali.grid(row=0, column=0, padx=10, pady=10)

    # Cargar la imagen con CTkImage
    imagen_path = "imagenes/cali.png"
    imagen_cali = ctk.CTkImage(dark_image=Image.open(imagen_path), size=(200, 200))

    # Crear un Label para mostrar la imagen
    label_imagen_cali = ctk.CTkLabel(frame_cali, image=imagen_cali)
    label_imagen_cali.grid(row=1, column=0, padx=10, pady=10)

    # Label para información de Cali
    label_info_cali = ctk.CTkLabel(frame_cali, text="""Es conocida como la capital mundial de la salsa y es uno de los principales centros deportivos de Colombia.
    En el año 2019 ha sido galardonado
    por los World Travel Awards como ciudad destino cultural de Suramérica, gracias a su oferta cultural, deportiva y turística.""")
    label_info_cali.grid(row=2, column=0, padx=10, pady=10)


    
    
    
    
    
    window_fly.mainloop()

# Función para buscar vuelos disponibles
def search_fly(indices, window_fly,peoples):
    window_fly.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    window_search = ctk.CTk()
    window_search.geometry("1250x750")
    window_search.state("zoomed")
    window_search.resizable(0, 0)
    window_search.title("Búsqueda de vuelos")
    
    # Crear frame para el label
    frame_label = ctk.CTkFrame(window_search, fg_color="grey26")
    frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    label = ctk.CTkLabel(
        frame_label, text=f"IDA: de {df['CiudadOrigen'].values[indices[0]]} a {df['CiudadDestino'].values[indices[0]]}"
    )
    label.grid(row=0, column=0)
    
    # Crear frame con scrollbar para los botones
    frame_buttons = ctk.CTkScrollableFrame(window_search, width=500, height=200)
    frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    frame_buttons.place(relx= 0.5, rely=0.2, anchor="center")

    # Crear botones dentro del frame con scrollbar
    # Crear frame con scrollbar para los botones
    frame_buttons = ctk.CTkScrollableFrame(window_search, width=500, height=200)
    frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    frame_buttons.place(relx= 0.5, rely=0.2, anchor="center")

    # Crear botones dentro del frame con scrollbar
    for i in indices:
        mensaje = f"""Vuelo: {df['Vuelo'].values[i]}
        Fecha: {df['Fecha'].values[i]}
        Desde COP: {df['ValorMin'].values[i]}"""
        button = ctk.CTkButton(
            frame_buttons, text=mensaje,
            command=lambda i=i: functions(info_buy(i, window_search, indices,peoples)),
            width=200, height=50
        )
        button.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)
    
    # Crear frame para el botón de regreso
    # Crear frame para el botón de regreso
    frame_button_back = ctk.CTkFrame(window_search, fg_color="grey26")
    frame_button_back.place(relx=0.   , rely=1, anchor="s")
    
    button_back = ctk.CTkButton(
        frame_button_back, text="VOLVER",
        command=lambda: functions(fly(window_search)),
        width=120, height=60
    )
    button_back.grid(row=2, column=0, padx=10, pady=10)
    
    window_search.mainloop()
    
    
# Información de vuelos disponibles en tales horas
def info_buy(indice, window ,indices, peoples):
    if window is not None:
        window.destroy()
    
    hours = c.search_hours(indice)
    df = pd.read_csv("dato_vuelo.csv")
    window_info = ctk.CTk()
    frame_hours_f = ctk.CTkFrame(window_info, fg_color="grey26")
    frame_hours_f.grid(row=0, column=0)
    label_hours = ctk.CTkLabel(frame_hours_f, text="Vuelos disponibles")
    label_hours.grid(row=0, column=0)
    
    for i in hours:
        mensaje = f"""Vuelo: {df['Vuelo'].values[i]}
        Hora salida: {df['HoraSalida'].values[i]}
        Hora llegada: {df['HoraLlegada'].values[i]}"""
        button_hours = ctk.CTkButton(
            frame_hours_f, text=mensaje,
            command=lambda i=i: functions(buy(i, window_info, hours,peoples)),
            width=20, height=2
        )
        button_hours.grid(row=1, column=i, padx=10, pady=10)
    
    window_info.mainloop()

def buy(indice, window, indices , peoples):
    if window is not None:
        window.destroy()
    
    df = pd.read_csv("dato_vuelo.csv")
    window_buy = ctk.CTk()
    label = ctk.CTkLabel(window_buy, text="Compra de paquetes")
    label.grid(row=0, column=0)
    label1 = ctk.CTkLabel(window_buy, text="Selecciona alguno de los paquetes")
    label1.grid(row=1, column=0)
    
    frame_1 = ctk.CTkFrame(window_buy)
    frame_1.grid(row=1, column=0)
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
    button_aluminio = ctk.CTkButton(frame_1, text="Comprar", width=20, height=2,command=lambda: fc.aluminum(indice,window_buy,peoples))
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
    button_diamond = ctk.CTkButton(frame_2, text="Comprar", width=20, height=2)
    button_diamond.grid(row=1, column=0)

    frame_3 = ctk.CTkFrame(window_buy)
    frame_3.grid(row=1, column=2)
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
    label_sit = ctk.CTkLabel(frame_label, text="A    B      C      D      E      F")
    label_sit.grid(row=0, column=0)
    frame_label.place(relx=0.5, rely=0.0, anchor="n")
    
    # Creación de asientos
    frame_sits = ctk.CTkFrame(window_buy)
    frame_sits.place(relx=0.5, rely=0.1, anchor="n")
    matriz = []
    for i in range(12):
        buttons = []
        for j in range(6):
            button_sit = ctk.CTkButton(frame_sits, text=f"{chr(65+j)}{i+1}", width=5, height=2)
            button_sit.grid(row=i, column=j, padx=10, pady=10)
            texto = c.getnums(button_sit.cget("text"))
            if texto >= 9:
                button_sit.configure(fg_color="green", state="disabled")
            elif texto >= 5:
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
    


#______________________________________________________
    #darle posicion a los botones y elementos de la pantalla de busqueda de vuelos



def record_check_in(window,peoples,indice):
    window.destroy()
    window_record = ctk.CTk()
    window_record.title("Registro")
    window_record.geometry("1920x1080")
    window_record.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    #frame del responsable de pago
    
    
    #frame de acompañantes
    frame_acompanantes = ctk.CTkScrollableFrame(window_record, fg_color="grey26",border_color="green",border_width=3,width=1000,height=300)
    frame_acompanantes.grid(row=1, column=0)
    
    
    #frame de información de vuelo
    frame_info_fly = ctk.CTkFrame(window_record, fg_color="grey26",border_color="green",border_width=2,width=500,height=300)
    frame_info_fly.grid(row=0, column=0,padx=10, pady=30)
    label_fly = ctk.CTkLabel(frame_info_fly, text="Información de vuelo")
    
    
    label_fly.grid(row=0, column=0)
    
    #hora de salida
    frame_hours_f = ctk.CTkFrame(window_record, fg_color="grey26",border_color="green",border_width=2)
    frame_hours_f.grid(row=0, column=0)
    label_hours = ctk.CTkLabel(frame_hours_f, text="Información de vuelo")
    label_hours.grid(row=0, column=0)
    
    
    
    datas = []
    for i in range(peoples):
        ayuda = []
        #label y entry de acompañantes
        frame_persona = ctk.CTkFrame(frame_acompanantes, fg_color="grey26",border_color="green",border_width=2)
        frame_persona.grid(row=i, column=0,padx=10, pady=30)
        label_acompanantes = ctk.CTkLabel(frame_persona, text=f"Acompañante {i+1}")
        #posicion de los elementos
        label_acompanantes.grid(row=0, column=0, padx=10, pady=10)
        
        genero=ctk.StringVar()
        #radiobutton de genero
        radio_m = ctk.CTkRadioButton(frame_persona, text="Masculino", variable=genero, value="Masculino")
        radio_f = ctk.CTkRadioButton(frame_persona, text="Femenino", variable=genero, value="Femenino")
        #posicion de los elementos
        radio_m.grid(row=1, column=0, padx=10, pady=10)
        radio_f.grid(row=1, column=1, padx=10, pady=10)
        
        label_name = ctk.CTkLabel(frame_persona, text="Primer nombre")
        entry_name = ctk.CTkEntry(frame_persona)
        #posicion de los elementos
        label_name.grid(row=1, column=2, padx=10, pady=10)
        entry_name.grid(row=1, column=3, padx=10, pady=10)
        
        label_last_name = ctk.CTkLabel(frame_persona, text="Primer apellido")
        entry_last_name = ctk.CTkEntry(frame_persona)
        #posicion de los elementos
        label_last_name.grid(row=1, column=4, padx=10, pady=10)
        entry_last_name.grid(row=1, column=5, padx=10, pady=10)
        
        label_id = ctk.CTkLabel(frame_persona, text="Identificación")
        entry_id = ctk.CTkEntry(frame_persona)
        #posicion de los elementos
        label_id.grid(row=2, column=0, padx=10, pady=10)
        entry_id.grid(row=2, column=1, padx=10, pady=10)
        
        label_nationality = ctk.CTkLabel(frame_persona, text="Nacionalidad")
        entry_nationality = ctk.CTkEntry(frame_persona)
        #posicion de los elementos
        label_nationality.grid(row=2, column=2, padx=10, pady=10)
        entry_nationality.grid(row=2, column=3, padx=10, pady=10)
        
        label_email = ctk.CTkLabel(frame_persona, text="Correo")
        entry_email = ctk.CTkEntry(frame_persona)
        #posicion de los elementos
        label_email.grid(row=2, column=4, padx=10, pady=10)
        entry_email.grid(row=2, column=5, padx=10, pady=10)
        
        label_telephone = ctk.CTkLabel(frame_persona, text="Teléfono")
        entry_telephone = ctk.CTkEntry(frame_persona)
        #posicion de los elementos
        label_telephone.grid(row=3, column=0, padx=10, pady=10)
        entry_telephone.grid(row=3, column=1, padx=10, pady=10)
        
        asistencia = ctk.StringVar()
        label_asistencia = ctk.CTkLabel(frame_persona, text="Requiere Asistencia")
        radio_si = ctk.CTkRadioButton(frame_persona, text="Si", variable=asistencia, value="Si")
        radio_no = ctk.CTkRadioButton(frame_persona, text="No", variable=asistencia, value="No")
        
        label_asistencia.grid(row=3, column=2, padx=10, pady=10)
        radio_si.grid(row=3, column=3, padx=10, pady=10)
        radio_no.grid(row=3, column=4, padx=10, pady=10)
        if i == 0 :
            responsable = []
            label_acargo = ctk.CTkLabel(frame_persona, text="Responsable de pago")
            label_acargo.grid(row=0, column=1)
            label_tarjeta = ctk.CTkLabel(frame_persona, text="Tarjeta de crédito")
            entry_tarjeta = ctk.CTkEntry(frame_persona)
            label_cvv = ctk.CTkLabel(frame_persona, text="CVV")
            entry_cvv = ctk.CTkEntry(frame_persona)
            #posicion de los elementos
            
            label_tarjeta.grid(row=4, column=0, padx=10, pady=10)
            entry_tarjeta.grid(row=4, column=1, padx=10, pady=10)
            label_cvv.grid(row=4, column=2, padx=10, pady=10)
            entry_cvv.grid(row=4, column=3, padx=10, pady=10)
            responsable = [genero,entry_name,entry_last_name,entry_id,entry_nationality,entry_email,entry_telephone,asistencia,entry_tarjeta,entry_cvv]
        else:
            ayuda = [genero,entry_name,entry_last_name,entry_id,entry_nationality,entry_email,entry_telephone,asistencia]
            datas.append(ayuda)
            
                    
    window_record.mainloop()

# ARREGLAR ESTA FUNCION PARA HACER LA CONFIRMACION DE VUELO (CHECK IN)
# def login(window):
#     window.destroy()
#     window_login = ctk.CTk()
#     window_login.title("Iniciar sesión")
#     window_login.geometry("400x400")
#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")

#     label_id = ctk.CTkLabel(window_login, text="Identificación") #label para la identificacion
#     entry_id = ctk.CTkEntry(window_login) #entry para la identificacion
#     label_email = ctk.CTkLabel(window_login, text="Correo") #label para el correo
#     entry_email = ctk.CTkEntry(window_login) #entry para el correo 
#     button_back = ctk.CTkButton(window_login, text="Volver", command=lambda: return_menu(window_login), width=9, height=2 ) #boton para volver
#     button_send = ctk.CTkButton(window_login, text="Enviar", command=lambda: c.condition_login(entry_id.get(), entry_email.get()), width=9, height=2) #boton para enviar
#     window_login.bind("<Return>", lambda e: c.condition_login(entry_id.get(), entry_email.get())) #evento para enviar
#     window_login.bind("<Escape>", lambda e: return_menu(window_login)) #evento para volver

#     label_id.grid(row=0, column=0, padx=10, pady=10)
#     entry_id.grid(row=0, column=1, padx=10, pady=10)
#     label_email.grid(row=1, column=0, padx=10, pady=10)
#     entry_email.grid(row=1, column=1, padx=10, pady=10)
#     button_send.grid(row=2, column=0, padx=10, pady=10)
#     button_back.grid(row=2, column=1, padx=10, pady=10)
    
#     window_login.mainloop()

# Función del menú
# def menu():
#     window_menu = ctk.CTk()
#     window_menu.title("Menú")
#     window_menu.geometry("400x400")
#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")

#     label = ctk.CTkLabel(window_menu, text="Menú")

#     button_record = ctk.CTkButton(window_menu, text="Registrarse", command=lambda: record(window_menu), width=9, height=2)
#     button_login = ctk.CTkButton(window_menu, text="Iniciar sesión", command=lambda: login(window_menu), width=9, height=2)
#     button_out = ctk.CTkButton(window_menu, text="Salir", command=lambda: window_menu.destroy(), width=9, height=2)

#     window_menu.bind("<Control_L>", lambda e: record(window_menu))
#     window_menu.bind("<Return>", lambda e: login(window_menu))
#     window_menu.bind("<Escape>", lambda e: window_menu.destroy())

#     label.grid(row=0, column=0)
#     button_record.grid(row=2, column=0, padx=30, pady=15)
#     button_login.grid(row=3, column=0, padx=30, pady=15)
#     button_out.grid(row=4, column=0, padx=30, pady=15)
    
#     window_menu.mainloop()

# def return_menu(window):
#     window.destroy()
#     menu()





if __name__=='__main__':
    functions(fly())