
from tkinter import messagebox as mb
from tkinter import ttk
import pandas as pd 
import os 
import PIL as pil
import conditions as c 
import  save as s
import datetime 
from tkcalendar import Calendar
import customtkinter as ctk
def functions(function):
    function

def fly(window_search=None):
    
    
    if window_search == None:
        pass
    else:
        window_search.destroy()
        
    origen, destino, fecha = c.lista_vuelos()
    
    # creacion de la ventana de menu fly
    
    window_fly = ctk.CTk()
    window_fly.title("Fly_Heaven")
    window_fly.geometry("1250x750")
    window_fly.resizable(0, 0)  # no se puede cambiar el tamaño de la ventana
    window_fly.iconbitmap("fly_heaven.ico")
    label = ctk.CTkLabel(window_fly, text="Menu")
    label.grid(row=0, column=0)

    # crear una lista de dias de junio
    dates_june = [f"2024-06-{day:02d}" for day in range(1, 31)]
    
    going = ctk.StringVar()

    # creacion de frame para los wigets de la busqueda
    
    frame_busqueda = ctk.CTkFrame(window_fly)
    frame_busqueda.configure(fg_color = "grey26")
    frame_busqueda.place(relx = 0.5, rely = 0.1, anchor = "center")
    
    # creacion de elementos de la pantalla de menu fly dentro del frame: frame_busqueda
    
    label_passenger = ctk.CTkLabel(frame_busqueda, text="numero de pasajeros")
    entry_passenger = ctk.CTkEntry(frame_busqueda)
    only_going = ctk.CTkRadioButton(frame_busqueda, text="solo ida", variable=going, value = 2, height=5, width=10)
    cities_origin = ctk.CTkComboBox(frame_busqueda, values=list(origen), state="readonly")  # steate readonly para que no se pueda escribir
    cities_origin.set("Ciudad de origen")  # coloca un texto por defecto
    cities_destination = ctk.CTkComboBox(frame_busqueda, values=list(destino), state="readonly")  # steate readonly para que no se pueda escribir
    cities_destination.set("Ciudad de destino")  # coloca un texto por defecto
    list_going = ctk.CTkComboBox(frame_busqueda, values=dates_june, state="readonly")  # steate readonly para que no se pueda escribir
    list_going.set("ida")  # coloca un texto por defecto
    
    # creacion de frame para el boton de busqueda
    frame_button_search = ctk.CTkFrame(window_fly)
    frame_button_search.configure(width = 100, height = 50  ,fg_color = "grey26")
    frame_button_search.place(relx = 0.5, rely = 0.5, anchor = "s")
    
    button_search = ctk.CTkButton(frame_button_search, text="BUSCAR", command=lambda: c.conditions_search(cities_destination.get(), cities_origin.get(), entry_passenger.get(), going.get(),window_fly), width=90, height=40)
    # dar posicion a los elementos de la pantalla de menu fly
    
    
    cities_origin.grid(row=8, column=0)
    cities_destination.grid(row=8, column=1)
    list_going.grid(row=8, column=2, padx=10, pady=10)
    only_going.grid(row=0, column=0)
    button_search.place(relx = 0.5, rely = 0.5, anchor = "center")
    label_passenger.grid(row=8, column=5, padx=10, pady=10)
    entry_passenger.grid(row=8, column=6, padx=10, pady=10)
    
    window_fly.mainloop()

# funcion para buscar vuelos disponibles
def search_fly(indices, window_fly):
    window_fly.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    
    window_search = ctk.CTk()
    window_search.geometry("1250x750")
    window_search.state("zoomed")
    window_search.resizable(0, 0)
    window_search.title("busqueda de vuelos")
    
    #crear frame para el label
    frame_label = ctk.CTkFrame(window_search)
    frame_label.configure(fg_color = "grey26")
    frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    label = ctk.CTkLabel(frame_label, text=f"IDA:  de {df['CiudadOrigen'].values[indices[0]]} a {df['CiudadDestino'].values[indices[0]]}")
    label.grid(row=0, column=0)
    
    # creacion de frame para los botones
    frame_buttons = ctk.CTkFrame(window_search)
    frame_buttons.configure(fg_color = "grey26")
    frame_buttons.grid(row=1, column=5, padx=10, pady=10)

    # creacion de  botones = []
    for i in indices:
        mensaje= f"""vuelo:{df['Vuelo'].values[i]}
        fecha:{df['Fecha'].values[i]}
        desde COP:{df["ValorMin"].values[i]}"""
        button = ctk.CTkButton(frame_buttons, text=f"{mensaje}", command=lambda i=i: functions(info_buy(i, window_search, indices)), width=20, height=2)
        button.grid(row=1, column=i, padx=10, pady=10)
    #cracion frame para el boton de regreso
    frame_button_back = ctk.CTkFrame(window_search)
    frame_button_back.configure(fg_color = "grey26")
    frame_button_back.place(relx = 0.5, rely = 1, anchor = "s")
    
    button_back = ctk.CTkButton(frame_button_back, text="VOLVER", command=lambda: functions(fly(window_search)), width=120, height= 60)
    button_back.grid(row=2, column=0, padx=10, pady=10)
    
    window_search.mainloop()


#informacion de vuelos disponibles en tales horas
def info_buy(indice,window=None,indices=None):
    if window==None:
        pass
    else:
        window.destroy()
    hours=c.search_hours(indice)
    
    print(indice)
    df=pd.read_csv("dato_vuelo.csv")
    window_info=ctk.CTk()
    frame_hours_f=ctk.CTkFrame(window_info) #frame para los botones
    frame_hours_f.configure(fg_color = "grey26") #color del frame
    frame_hours_f.grid(row=0,column=0) #posicion del frame
    label_hours=ctk.CTkLabel(frame_hours_f,text="vuelos disponibles") #label para los vuelos disponibles
    label_hours.grid(row=0,column=0) #posicion del label
    button=[] #lista de botones
    for i in hours: #recorre las horas
        mensaje=f"""vuelo:{df['Vuelo'].values[i]} 
        hora salida= {df['HoraSalida'].values[i]}
        hora llegada= {df['HoraLlegada'].values[i]}"""
        button_hours=ctk.CTkButton(frame_hours_f,text=f"{mensaje}",command=lambda i=i:  functions(buy(i,window_info,hours)),width=20,height=2)
        button_hours.grid(row=1,column=i,padx=10,pady=10)
        button.append(button_hours)
    window_info.mainloop()

def buy(indice,window=None,indices=None):
    if window==None:
        pass
    else:
        window.destroy()#se destruye la ventana
    df=pd.read_csv("dato_vuelo.csv")
    window_buy=ctk.CTk()
    label=ctk.CTkLabel(window_buy,text="compra de paquetes")
    label.grid(row=0,column=0)
    label1=ctk.CTkLabel(window_buy,text="selecciona alguno de los paquetes")
    label1.grid(row=1,column=0)
    frame_1 = ctk.CTkFrame(window_buy)  # frame para el paquete aluminio
    frame_1.grid(row=1, column=0)  # posicion del frame
    label_1 = ctk.CTkLabel(frame_1, text=f"""Aluminio:
    1 artículo personal (bolso) (Debe caber debajo del asiento)
    1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
    Asiento Estándar (Sujeto a disponibilidad)
    Cambios de vuelo (No es permitido)
    Reembolso (No es permitido)
    PRECIO: {df['ValorMin'].values[indice]}""")
    label_1.grid(row=0, column=0)# posicion del texto
    button_aluminio=ctk.CTkButton(frame_1,text="comprar",width=20,height=2)
    button_aluminio.grid(row=1,column=0)

    # Diamante:
    frame_2 = ctk.CTkFrame(window_buy)
    frame_2.grid(row=1, column=1)
    label_2 = ctk.CTkLabel(frame_2, text=f"""Diamante:
    1 artículo personal (bolso) (Debe caber debajo del asiento)
    1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
    Asiento Estándar (Sujeto a disponibilidad)
    Cambios de vuelo (Permitido con costo adicional)
    Reembolso (Permitido con costo adicional)
    PRECIO: {df['ValorMedio'].values[indice]}""")
    label_2.grid(row=0, column=0)
    button_diamond=ctk.CTkButton(frame_2,text="comprar",width=20,height=2)
    button_diamond.grid(row=1,column=0)

    # Premium:
    frame_3 = ctk.CTkFrame(window_buy)
    frame_3.grid(row=1, column=2)
    label_3 = ctk.CTkLabel(frame_3, text=f"""Premium:
    1 artículo personal (bolso) (Debe caber debajo del asiento)
    1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)
    Asiento Preferencial (Incluido)
    Cambios de vuelo (Permitido sin costo adicional)
    Reembolso (Permitido)
    PRECIO : {df['ValorMax'].values[indice]}""")
    label_3.grid(row=0, column=0)
    button_premium=ctk.CTkButton(frame_3,text="comprar",width=20,height=2)
    button_premium.grid(row=1,column=0)
    window_buy.mainloop()





















#usuario escoge asiento solo si es premium
def choose_sit(indice=None,window=None,indices=None):
    if window==None:
        pass
    else:
        window.destroy()
    df=pd.read_csv("dato_vuelo.csv")
    
    # creacion de ventana para la eleccion de asiento
    window_buy=ctk.CTk()
    window_buy.geometry("1250x750")
    window_buy.resizable(0,0)
    window_buy.iconbitmap("fly_heaven.ico")
    window_buy.title("eleccion de asiento")
    

    
    
    
    #creacion de frame label a,b,c,d,e,f
    
    frame_label=ctk.CTkFrame(window_buy)
    label_sit=ctk.CTkLabel(frame_label,text="A    B      C      D      E      F")
    label_sit.grid(row=0,column=0)
    frame_label.place(relx = 0.5, rely = 0.0, anchor = "n")
    
    #creacion de asientos
    
    frame_sits=ctk.CTkFrame(window_buy)
    frame_sits.place(relx = 0.5, rely = 0.1, anchor = "n")
    buttons=[]
    matriz=[]
    for i in range(12):
        buttons=[]
        for j in range(6):
            button_sit=ctk.CTkButton(frame_sits,text=f"{chr(65+j)}{i+1}",width=5,height=2)
            button_sit.grid(row=i,column=j,padx=10,pady=10)
            texto=c.getnums(button_sit.cget("text"))
            if texto >=9:
                button_sit.configure(fg_color="green",state="disabled")
            elif texto >=5:
                button_sit.configure(fg_color="red",state="disabled")
            else:
                button_sit.configure(fg_color="blue")
            buttons.append(button_sit)
        matriz.append(buttons)
        
    # frame label categorias
    frame_premium=ctk.CTkFrame(window_buy)
    label_premium=ctk.CTkLabel(frame_premium,text="asientos premium")
    frame_premium.place(relx = 0.8, rely = 0.2, anchor = "e")
    label_premium.grid(row=0,column=0)
    #
    frame_diamond=ctk.CTkFrame(window_buy)
    label_diamond=ctk.CTkLabel(frame_diamond,text="asientos diamond")
    frame_diamond.place(relx = 0.8, rely = 0.4, anchor = "e")
    label_diamond.grid(row=0,column=0)
    #
    frame_aluminio=ctk.CTkFrame(window_buy)
    label_aluminio=ctk.CTkLabel(frame_aluminio,text="asientos aluminio")
    frame_aluminio.place(relx = 0.8, rely = 0.7, anchor = "e")
    label_aluminio.grid(row=0,column=0)
    
    window_buy.mainloop()
            
#______________________________________________________
    #darle posicion a los botones y elementos de la pantalla de busqueda de vuelos



# Función para el registro
# def record_check_in(window):
#     window.destroy()
#     window_record = ctk.CTk()
#     window_record.title("Registro")
#     window_record.geometry("600x600")
#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")

#     gender = ctk.StringVar()
#     label_gender = ctk.CTkLabel(window_record, text="Género", font=("Times New Roman", 14))
#     checkbox = ctk.CTkRadioButton(window_record, text="Masculino", variable=gender, value="masculino", font=("Times New Roman", 14))
#     checkbox1 = ctk.CTkRadioButton(window_record, text="Femenino", variable=gender, value="femenino", font=("Times New Roman", 14))
    
#     label_name = ctk.CTkLabel(window_record, text="Nombre", font=("Times New Roman", 14))
#     entry_name = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     label_lastname = ctk.CTkLabel(window_record, text="Apellido", font=("Times New Roman", 14))
#     entry_lastname = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     label_id = ctk.CTkLabel(window_record, text="Identificación", font=("Times New Roman", 14))
#     entry_id = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     label_telephone = ctk.CTkLabel(window_record, text="Teléfono", font=("Times New Roman", 14))
#     entry_telephone = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     label_nationality = ctk.CTkLabel(window_record, text="Nacionalidad", font=("Times New Roman", 14))
#     entry_nationality = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     label_email = ctk.CTkLabel(window_record, text="Correo", font=("Times New Roman", 14))
#     entry_email = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     label_birthday = ctk.CTkLabel(window_record, text="Fecha de nacimiento", font=("Times New Roman", 14))
#     entry_birthday = ctk.CTkEntry(window_record, font=("Times New Roman", 14))
    
#     attendance = ctk.StringVar()
#     label_attendance = ctk.CTkLabel(window_record, text="Requiere asistencia", font=("Times New Roman", 14))
#     radiuobutton = ctk.CTkRadioButton(window_record, text="Asistencia", variable=attendance, value="requiere", font=("Times New Roman", 14))
#     radiuobutton1 = ctk.CTkRadioButton(window_record, text="No asistencia", variable=attendance, value="no requiere", font=("Times New Roman", 14))
    
#     button_send = ctk.CTkButton(window_record, text="Enviar", command=lambda: c.conditions_record(gender.get(), entry_name.get(), entry_lastname.get(), entry_id.get(), entry_telephone.get(), entry_nationality.get(), entry_email.get(), entry_birthday.get(), attendance.get(),window_record),font=("Times New Roman", 14))
#     button_back = ctk.CTkButton(window_record, text="Volver", command=lambda: return_menu(window_record), width=9, height=2, font=("Times New Roman", 14))
    
#     window_record.bind("<Return>", lambda e: c.conditions_record(gender.get(), entry_name.get(), entry_lastname.get(), entry_id.get(), entry_telephone.get(), entry_nationality.get(), entry_email.get(), entry_birthday.get(), attendance.get()))
#     window_record.bind("<Escape>", lambda e: return_menu(window_record))
#     # Posicionamiento de los elementos
#     label_gender.grid(row=0, column=0, padx=10, pady=10)
#     checkbox.grid(row=0, column=1, padx=10, pady=10)
#     checkbox1.grid(row=0, column=2, padx=10, pady=10)
#     label_name.grid(row=1, column=0, padx=10, pady=10)
#     entry_name.grid(row=1, column=1, padx=10, pady=10)
#     label_lastname.grid(row=1, column=2, padx=10, pady=10)
#     entry_lastname.grid(row=1, column=3, padx=10, pady=10)
#     label_id.grid(row=2, column=0, padx=10, pady=10)
#     entry_id.grid(row=2, column=1, padx=10, pady=10)
#     label_telephone.grid(row=2, column=2, padx=10, pady=10)
#     entry_telephone.grid(row=2, column=3, padx=10, pady=10)
#     label_nationality.grid(row=3, column=0, padx=10, pady=10)
#     entry_nationality.grid(row=3, column=1, padx=10, pady=10)
#     label_email.grid(row=3, column=2, padx=10, pady=10)
#     entry_email.grid(row=3, column=3, padx=10, pady=10)
#     button_send.grid(row=7, column=0, padx=10, pady=10)
#     label_birthday.grid(row=4, column=0, padx=10, pady=10)
#     entry_birthday.grid(row=4, column=1, padx=10, pady=10)
#     label_attendance.grid(row=5, column=0, padx=10, pady=10)
#     radiuobutton.grid(row=6, column=0, padx=10, pady=10)
#     radiuobutton1.grid(row=6, column=1, padx=10, pady=10)
#     button_back.grid(row=7, column=1, padx=10, pady=10)
    
#     window_record.mainloop()

# Función para verificar e iniciar sesión

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