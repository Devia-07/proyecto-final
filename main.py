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

    going = ctk.StringVar()

    # Creación de frame para los widgets de la búsqueda
    search_frame = ctk.CTkFrame(window_fly, fg_color="grey26")
    search_frame.grid(row=0, column=2)

    # Creación de elementos de la pantalla de menú fly dentro del frame: search_frame
    label_passenger = ctk.CTkLabel(search_frame, text="Número de pasajeros")
    entry_passenger = ctk.CTkEntry(search_frame)
    space = ctk.CTkLabel(search_frame, text="")
    space = ctk.CTkLabel(search_frame, text="")
    only_going = ctk.CTkRadioButton(
        search_frame, text="Solo ida", variable=going, value=2, height=5, width=10)
    cities_origin = ctk.CTkComboBox(
        search_frame, values=list(origen), state="readonly")
    cities_origin.set("Ciudad de origen")
    cities_destination = ctk.CTkComboBox(
        search_frame, values=list(destino), state="readonly")
    cities_destination.set("Ciudad de destino")
    list_going = ctk.CTkComboBox(
        search_frame, values=dates_june, state="readonly")
    list_going.set("ida")

    # Creación de frame para el botón de búsqueda
    frame_button_search = ctk.CTkFrame(
        window_fly, width=100, height=50, fg_color="grey26")
    frame_button_search.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

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

    flight_frames = ctk.CTkScrollableFrame(
        window_fly, fg_color="grey26", width=1000, height=400)
    flight_frames.grid(row=2, column=2)

    # ______________________________________________________

    # Crear el frame para Cali
    frame_cali = ctk.CTkFrame(flight_frames, fg_color="grey26",
                              border_color="blue", border_width=2, width=400, height=300)
    frame_cali.grid(row=1, column=0, padx=1, pady=1)

    # Label para Cali
    label_cali = ctk.CTkLabel(frame_cali, text="Cali",
                              fg_color="skyblue", font=("Times New Roman", 20))
    label_cali.grid(row=0, column=0, padx=10, pady=10)

    # Cargar la imagen con CTkImage
    path_image = "imagenes/cali.png"
    cali_image = ctk.CTkImage(
        dark_image=Image.open(path_image), size=(300, 100))

    # Crear un Label para mostrar la imagen
    label_cali_image = ctk.CTkLabel(frame_cali, image=cali_image)
    label_cali_image.grid(row=1, column=0, padx=10, pady=10)

    # Label para información de Cali
    label_info_cali = ctk.CTkLabel(frame_cali, text="""Es conocida como la capital mundial de la salsa y es uno de los principales centros deportivos de Colombia.
    En el año 2019 ha sido galardonado
    por los World Travel Awards como ciudad destino cultural de Suramérica, gracias a su oferta cultural
    deportiva y turística.""", font=("Times New Roman", 20))
    label_info_cali.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Medellín
    frame_medellin = ctk.CTkFrame(flight_frames, fg_color="grey26",
                                  border_color="blue", border_width=2, width=400, height=300)
    frame_medellin.grid(row=1, column=1, padx=1, pady=1)
    label_medellin = ctk.CTkLabel(
        frame_medellin, text="Medellín", fg_color="skyblue", font=("Times New Roman", 20))
    label_medellin.grid(row=0, column=0, padx=10, pady=10)
    path_image = "imagenes/medellin.png"
    medellin_image = ctk.CTkImage(
        dark_image=Image.open(path_image), size=(300, 100))
    label_medellin_image = ctk.CTkLabel(frame_medellin, image=medellin_image)
    label_medellin_image.grid(row=1, column=0, padx=10, pady=10)
    label_info_medellin = ctk.CTkLabel(frame_medellin, text="""Es conocida como la capital de la montaña y la ciudad de la eterna primavera.
    Es la segunda ciudad más grande de Colombia y es un importante centro económico y cultural.""", font=("Times New Roman", 20))
    label_info_medellin.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Bogotá
    frame_bogota = ctk.CTkFrame(flight_frames, fg_color="grey26",
                                border_color="blue", border_width=2, width=400, height=300)
    frame_bogota.grid(row=2, column=0, padx=1, pady=1)
    label_bogota = ctk.CTkLabel(
        frame_bogota, text="Bogotá", fg_color="skyblue", font=("Times New Roman", 20))
    label_bogota.grid(row=0, column=0, padx=10, pady=10)
    path_image = "imagenes/bogota.png"
    bogota_image = ctk.CTkImage(
        dark_image=Image.open(path_image), size=(300, 100))
    label_bogota_image = ctk.CTkLabel(frame_bogota, image=bogota_image)
    label_bogota_image.grid(row=1, column=0, padx=10, pady=10)
    label_info_bogota = ctk.CTkLabel(frame_bogota, text="""Es la capital de Colombia y es la ciudad más grande del país.
    Es el centro político, económico, administrativo, industrial, artístico, cultural, deportivo y turístico de Colombia.""", font=("Times New Roman", 20))
    label_info_bogota.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Cartagena
    frame_cartagena = ctk.CTkFrame(
        flight_frames, fg_color="grey26", border_color="blue", border_width=2, width=500, height=200)
    frame_cartagena.grid(row=2, column=1, padx=10, pady=10)
    label_cartagena = ctk.CTkLabel(
        frame_cartagena, text="Cartagena", fg_color="skyblue", font=("Times New Roman", 20))
    label_cartagena.grid(row=0, column=0, padx=10, pady=10)
    path_image = "imagenes/cartagena.png"
    cartagena_image = ctk.CTkImage(
        dark_image=Image.open(path_image), size=(300, 100))
    label_cartagena_image = ctk.CTkLabel(
        frame_cartagena, image=cartagena_image)
    label_cartagena_image.grid(row=1, column=0, padx=10, pady=10)
    label_info_cartagena = ctk.CTkLabel(frame_cartagena, text="""Es conocida como la ciudad amurallada y es uno de los destinos turísticos más importantes de Colombia.
    Es un importante centro turístico, histórico y cultural.""", font=("Times New Roman", 20))
    label_info_cartagena.grid(row=2, column=0, padx=10, pady=10)

    # ______________________________________________________

    # Crear el frame para Santa Marta
    frame_santamarta = ctk.CTkFrame(
        flight_frames, fg_color="grey26", border_color="blue", border_width=2, width=500, height=200)
    frame_santamarta.grid(row=2, column=2, padx=1, pady=1)
    label_santamarta = ctk.CTkLabel(
        frame_santamarta, text="Santa Marta", fg_color="skyblue", font=("Times New Roman", 20))
    label_santamarta.grid(row=0, column=0, padx=10, pady=10)
    path_image = "imagenes/santa_marta.png"
    santamarta_image = ctk.CTkImage(
        dark_image=Image.open(path_image), size=(300, 100))
    label_santamarta_image = ctk.CTkLabel(
        frame_santamarta, image=santamarta_image)
    label_santamarta_image.grid(row=1, column=0, padx=10, pady=10)
    label_info_santamarta = ctk.CTkLabel(frame_santamarta, text="""Es conocida como la perla de América y es uno de los destinos turísticos más importantes de Colombia.
    Es un importante centro turístico, histórico y cultural.""", font=("Times New Roman", 20))
    label_info_santamarta.grid(row=2, column=0, padx=10, pady=10)

    window_fly.mainloop()

# Función para buscar vuelos disponibles


def search_fly(indexs, window_fly, peoples):
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
        frame_label, text=f"IDA: de {df['CiudadOrigen'].values[indexs[0]]} a {
            df['CiudadDestino'].values[indexs[0]]}"
    )
    label.grid(row=0, column=0)

    # Crear frame con scrollbar para los botones
    frame_buttons = ctk.CTkScrollableFrame(
        window_search, width=500, height=200)
    frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    frame_buttons.place(relx=0.5, rely=0.2, anchor="center")

    # Crear botones dentro del frame con scrollbar
    # Crear frame con scrollbar para los botones
    frame_buttons = ctk.CTkScrollableFrame(
        window_search, width=500, height=200)
    frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    frame_buttons.place(relx=0.5, rely=0.2, anchor="center")
    
    #hacer un frame para filtrar la busqueda    
    frame_filter = ctk.CTkFrame(window_search, fg_color="grey26")
    frame_filter.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
    label_filter = ctk.CTkLabel(frame_filter, text="Filtrar precios :")
    label_filter.grid(row=0, column=0)
    filter = ctk.CTkComboBox(frame_filter, values=["barato","medio","caro"], state="readonly")
    filter.set("precio")
    filter.grid(row=0, column=1)
    
    dates_june = []
    for day in range(1, 31):
        date = datetime.datetime(2024, 6, day)
        if date.weekday() in [2, 3]:  # 2 es miércoles, 3 es jueves
            dates_june.append(date.strftime("%Y-%m-%d"))
    filter_days = ctk.CTkComboBox(frame_filter, values=dates_june, state="readonly")
    filter_days.set("dias")
    # filtrar los dias de junio 
    filter_days.grid(row=0, column=2)
    buttons = []
    button_filter = ctk.CTkButton(frame_filter, text="Filtrar", command=lambda: c.filter_search(filter.get(),filter_days.get(), indices, window_search, peoples,buttons,frame_buttons))
    button_filter.grid(row=0, column=3,padx=10, pady=10)

    # Crear botones dentro del frame con scrollbar
    for i in indexs:
        message = f"""Vuelo: {df['Vuelo'].values[i]}
        Fecha: {df['Fecha'].values[i]}
        Desde COP: {df['ValorMin'].values[i]}"""
        button = ctk.CTkButton(
            frame_buttons, text=message,
            command=lambda i=i: functions(
                info_buy(i, window_search, indexs, peoples)),
            width=200, height=50
        )
        button.grid(row=i, column=0, padx=10, pady=10)
        buttons.append(button)

        
    # Crear frame para el botón de regreso
    # Crear frame para el botón de regreso
    frame_button_back = ctk.CTkFrame(window_search, fg_color="grey26")
    frame_button_back.place(relx=0., rely=1, anchor="s")

    button_back = ctk.CTkButton(
        frame_button_back, text="VOLVER",
        command=lambda: functions(fly(window_search)),
        width=120, height=60
    )
    button_back.grid(row=2, column=0, padx=10, pady=10)

    window_search.mainloop()


# Información de vuelos disponibles en tales horas
def info_buy(index, window, indexs, peoples):
    if window is not None:
        window.destroy()

    hours = c.search_hours(index)
    df = pd.read_csv("dato_vuelo.csv")
    window_info = ctk.CTk()
    frame_hours_f = ctk.CTkFrame(window_info, fg_color="grey26")
    frame_hours_f.grid(row=0, column=0)
    label_hours = ctk.CTkLabel(frame_hours_f, text="Vuelos disponibles")
    label_hours.grid(row=0, column=0)

    for i in hours:
        message = f"""Vuelo: {df['Vuelo'].values[i]}
        Hora salida: {df['HoraSalida'].values[i]}
        Hora llegada: {df['HoraLlegada'].values[i]}"""
        button_hours = ctk.CTkButton(
            frame_hours_f, text=message,
            command=lambda i=i: functions(buy(i, window_info, hours, peoples)),
            width=20, height=2
        )
        button_hours.grid(row=1, column=i, padx=10, pady=10)

    window_info.mainloop()


def buy(index, window, indexs, peoples):
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
    PRECIO: {df['ValorMin'].values[index]}"""
    )
    label_1.grid(row=0, column=0)
    button_aluminio = ctk.CTkButton(frame_1, text="Comprar", width=20,
                                    height=2, command=lambda: fc.aluminum(index, window_buy, peoples, df["ValorMin"].values[index]))
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
    PRECIO: {df['ValorMedio'].values[index]}"""
    )
    label_2.grid(row=0, column=0)
    button_diamond = ctk.CTkButton(frame_2, text="Comprar", width=20, 
                                   height=2, command=lambda: fc.diamond(index, window_buy, peoples, df["ValorMedio"].values[index]))
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
    PRECIO : {df['ValorMax'].values[index]}"""
    )
    label_3.grid(row=0, column=0)
    button_premium = ctk.CTkButton(frame_3, text="Comprar", width=20, height=2,
        command=lambda: functions(choose_sit(indice, window_buy, indices, peoples)))
    
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
                frame_sits, text=f"{chr(65+j)}{i+1}", width=5, height=2,
                command=lambda i=i,j=j: fc.premium(i,j,matriz, indice, peoples, window_buy,df["ValorMax"].values[indice]))
            button_sit.grid(row=i, column=j, padx=10, pady=10)
            text = c.getnums(button_sit.cget("text"))
            if text >= 9:
                button_sit.configure(fg_color="green", state="disabled")
            elif text >=  5:
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
    label_diamond = ctk.CTkLabel(frame_diamond, text="Asientos diamante")
    frame_diamond.place(relx=0.8, rely=0.4, anchor="e")
    label_diamond.grid(row=0, column=0)

    frame_aluminum = ctk.CTkFrame(window_buy)
    label_aluminum = ctk.CTkLabel(frame_aluminum, text="Asientos aluminio")
    frame_aluminum.place(relx=0.8, rely=0.7, anchor="e")
    label_aluminum.grid(row=0, column=0)

    window_buy.mainloop()


# ______________________________________________________
    # darle posicion a los botones y elementos de la pantalla de busqueda de vuelos


def record_check_in(window, peoples, index, sits, price):
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
    accompanying_frame = ctk.CTkScrollableFrame(
        window_record, fg_color="grey26", border_color="green", border_width=3, width=1000, height=300)
    accompanying_frame.grid(row=1, column=0)

    # frame de información de vuelo
    frame_info_fly = ctk.CTkFrame(window_record, fg_color="grey26",
                                  border_color="green", border_width=2, width=500, height=300)
    frame_info_fly.grid(row=0, column=0, padx=10, pady=30)
    label_fly = ctk.CTkLabel(frame_info_fly, text="Información de vuelo")
    label_fly.grid(row=0, column=0)
    label_fly1 = ctk.CTkLabel(frame_info_fly, text=f"Vuelo: {
                              df['Vuelo'].values[index]}")
    label_hour = ctk.CTkLabel(frame_info_fly, text=f"Hora de salida: {
                              df['HoraSalida'].values[index]}")
    label_hour1 = ctk.CTkLabel(frame_info_fly, text=f"Hora de llegada: {
                               df['HoraLlegada'].values[index]}")
    label_price = ctk.CTkLabel(frame_info_fly, text=f"Precio: {price}")
    label_fly1.grid(row=1, column=0)
    label_hour.grid(row=2, column=0)
    label_hour1.grid(row=3, column=0)
    label_price.grid(row=4, column=0)

    # hora de salida
    frame_hours_f = ctk.CTkFrame(
        window_record, fg_color="grey26", border_color="green", border_width=2)
    frame_hours_f.grid(row=0, column=0, padx=10, pady=10)
    label_hours = ctk.CTkLabel(frame_hours_f, text="Información de vuelo")
    label_hours.grid(row=0, column=0, padx=10, pady=10)
    label_people = ctk.CTkLabel(frame_hours_f, text=f"Numero de personas: {peoples}")
    label_people.grid(row=1, column=0, padx=10, pady=10)
    label_price_total = ctk.CTkLabel(frame_hours_f, text=f"Precio total: {price}")
    label_price_total.grid(row=2, column=0, padx=10, pady=10)
    label_unit_price = ctk.CTkLabel(frame_hours_f, text=f"Precio unitario: {price/peoples}")
    label_unit_price.grid(row=3, column=0, padx=10, pady=10)
    

    datas = []
    for i in range(peoples):
        help = []
        # label y entry de acompañantes
        person_frame = ctk.CTkFrame(
            accompanying_frame, fg_color="grey26", border_color="green", border_width=2)
        person_frame.grid(row=i, column=0, padx=10, pady=30)
        accompanying_label = ctk.CTkLabel(person_frame, text=f"Acompañante {
                                          i+1} \t asiento: {sits[i]}")
        # posicion de los elementos
        accompanying_label.grid(row=0, column=0, padx=10, pady=10)

        gender = ctk.StringVar()
        # radiobutton de genero
        radio_m = ctk.CTkRadioButton(
            person_frame, text="Masculino", variable=gender, value="Masculino")
        radio_f = ctk.CTkRadioButton(
            person_frame, text="Femenino", variable=gender, value="Femenino")
        # posicion de los elementos
        radio_m.grid(row=1, column=0, padx=10, pady=10)
        radio_f.grid(row=1, column=1, padx=10, pady=10)

        label_name = ctk.CTkLabel(person_frame, text="Primer nombre")
        entry_name = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_name.grid(row=1, column=2, padx=10, pady=10)
        entry_name.grid(row=1, column=3, padx=10, pady=10)

        label_last_name = ctk.CTkLabel(person_frame, text="Primer apellido")
        entry_last_name = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_last_name.grid(row=1, column=4, padx=10, pady=10)
        entry_last_name.grid(row=1, column=5, padx=10, pady=10)

        label_id = ctk.CTkLabel(person_frame, text="Identificación")
        entry_id = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_id.grid(row=2, column=0, padx=10, pady=10)
        entry_id.grid(row=2, column=1, padx=10, pady=10)

        label_nationality = ctk.CTkLabel(person_frame, text="Nacionalidad")
        entry_nationality = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_nationality.grid(row=2, column=2, padx=10, pady=10)
        entry_nationality.grid(row=2, column=3, padx=10, pady=10)

        label_email = ctk.CTkLabel(person_frame, text="Correo")
        entry_email = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_email.grid(row=2, column=4, padx=10, pady=10)
        entry_email.grid(row=2, column=5, padx=10, pady=10)

        label_telephone = ctk.CTkLabel(person_frame, text="Teléfono")
        entry_telephone = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_telephone.grid(row=3, column=0, padx=10, pady=10)
        entry_telephone.grid(row=3, column=1, padx=10, pady=10)

        attendance = ctk.StringVar()
        label_attendance = ctk.CTkLabel(
            person_frame, text="Requiere Asistencia")
        radio_yes = ctk.CTkRadioButton(
            person_frame, text="Si", variable=attendance, value="Si")
        radio_no = ctk.CTkRadioButton(
            person_frame, text="No", variable=attendance, value="No")

        label_attendance.grid(row=3, column=2, padx=10, pady=10)
        radio_yes.grid(row=3, column=3, padx=10, pady=10)
        radio_no.grid(row=3, column=4, padx=10, pady=10)

        label_birth = ctk.CTkLabel(person_frame, text="Fecha de nacimiento")
        entry_birth = ctk.CTkEntry(person_frame)
        # posicion de los elementos
        label_birth.grid(row=4, column=0, padx=10, pady=10)
        entry_birth.grid(row=4, column=1, padx=10, pady=10)

        help = [gender, entry_name, entry_last_name, entry_id, entry_nationality,
                entry_email, entry_telephone, entry_birth, attendance]
        datas.append(help)
    # boton de enviar
    button_send = ctk.CTkButton(accompanying_frame, hover_color="green", text="Enviar",
                                command=lambda: c.conditions_record(peoples, 9, datas, sits, index, window_record), width=9, height=2)
    button_send.grid(row=peoples, column=0, padx=10, pady=10)

    window_record.mainloop()

# ARREGLAR ESTA FUNCION PARA HACER LA CONFIRMACION DE VUELO (CHECK IN)


def pay_sits(window, peoples, datas, sits, index):
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
        window_pay, pay_client, peoples, datas, sits, index), width=100, height=10)
    button_pay.grid(row=5, column=0, padx=10, pady=10)
    window_pay.mainloop()

def tickets(window, peoples, datas, sits, index):
    window.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    window_tickets = ctk.CTk()
    window_tickets.geometry("1000x1000")
    window_tickets.title("Tickets")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    frame_scroll = ctk.CTkScrollableFrame(window_tickets, width=600, height=300)
    frame_scroll.grid(row=0, column=0)
    combinacion = fc.randomiser(peoples, indice)
    for i in range(peoples):
            frame_ticket = ctk.CTkFrame(frame_scroll, fg_color="grey26", border_color="green", border_width=2)
            frame_ticket.grid(row=i, column=0, padx=10, pady=30)
            combinacion = fc.randomiser(peoples, indice)
            label = ctk.CTkLabel(frame_ticket, text="Pase de abordaje")
            label.grid(row=0, column=0, padx=10, pady=10)
            label_name = ctk.CTkLabel(frame_ticket, text=f"Nombre: {datas[i][1]} {datas[i][2]}")
            label_name.grid(row=1, column=0, padx=10, pady=10)
            label_origin = ctk.CTkLabel(frame_ticket, text=f"Origen: {df['CiudadOrigen'].values[index]}")
            label_origin.grid(row=2, column=0, padx=10, pady=10)
            label_destiny = ctk.CTkLabel(frame_ticket, text=f"Destino: {df['CiudadDestino'].values[index]}")
            label_destiny.grid(row=3, column=0, padx=10, pady=10)
            label_hour = ctk.CTkLabel(frame_ticket, text=f"Hora de salida: {df['HoraSalida'].values[index]}")
            label_hour.grid(row=3, column=1 , padx=10, pady=10)
            label_hour1 = ctk.CTkLabel(frame_ticket, text=f"Hora de llegada: {df['HoraLlegada'].values[index]}")
            label_hour1.grid(row=3, column=2 , padx=10, pady=10)
            label_fly = ctk.CTkLabel(frame_ticket, text=f"Vuelo: {df['Vuelo'].values[index]}")
            label_fly.grid(row=1, column=1, padx=10, pady=10)
            label_code = ctk.CTkLabel(frame_ticket, text=f"Código de abordaje: {combinacion}")
            label_code.grid(row=4, column=0, padx=10, pady=10)
    window_tickets.mainloop()
            
def check_in(index):
    window_check_in = ctk.CTk()
    window_check_in.geometry("400x500")
    window_check_in.title("Check in")
    window_check_in.configure(bg="#EBEBEB")  # Set background color
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    frame_check_in = ctk.CTkFrame(window_check_in, fg_color="#EBEBEB")
    frame_check_in.place(relx=0.5, rely=0.5, anchor="center")
    image_path = "imagenes\\a airplane with the.jpg"
    plane_image = Image.open(image_path).resize((150, 150))
    photo = ImageTk.PhotoImage(plane_image)
    label = ctk.CTkLabel(frame_check_in, text="", image=photo)
    label.plane_image = photo
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    label_code = ctk.CTkLabel(frame_check_in, text="Codigo")
    label_code.grid(row=1, column=0, padx=10, pady=10)
    entry_code = ctk.CTkEntry(frame_check_in)
    entry_code.grid(row=1, column=1, padx=10, pady=10)
    label_dni = ctk.CTkLabel(frame_check_in, text="DNI")
    label_dni.grid(row=2, column=0, padx=10, pady=10)
    entry_dni = ctk.CTkEntry(frame_check_in)
    entry_dni.grid(row=2, column=1, padx=10, pady=10)
    button = ctk.CTkButton(frame_check_in, text="Realizar Check-in", command=lambda: c.condition_check_in(entry_code.get(), entry_dni.get(), window_check_in, index))
    button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    window_check_in.mainloop()
                    
        


if __name__ == '__main__':
    # functions(fly())
    # choose_sit()
    check_in(index=None)
