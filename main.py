
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


# def return_menu(window):
#     window.destroy()
#     menu()







def conditions_searchs(destination,origin,passenger):
    indices=[]
    if c.conditions_search(destination,origin,passenger):
        mb.showinfo("info","datos correctos")
        indices=c.search(destination,origin)
        search_fly(indices)
    else:
        mb.showerror("error", "datos incorrectos")


def fly():
    origen, destino, fecha = c.lista_vuelos()
    window_fly = ctk.CTk()
    window_fly.title("menu fly")
    window_fly.geometry("500x 500")
    window_fly.resizable(0, 0)  # no se puede cambiar el tamaño de la ventana
    label = ctk.CTkLabel(window_fly, text="Menu")
    label.grid(row=0, column=0)

    # crear una lista de dias de junio
    dates_june = [f"2024-06-{day:02d}" for day in range(1, 31)]
    going = ctk.StringVar()

    # creacion de frame para los wigets de la busqueda
    
    frame_busqueda = ctk.CTkFrame(window_fly)
    frame_busqueda.configure(fg_color = "grey26")
    
    # creacion de elementos de la pantalla de menu fly dentro del frame: frame_busqueda
    
    label_passenger = ctk.CTkLabel(frame_busqueda, text="numero de pasajeros")
    entry_passenger = ctk.CTkEntry(frame_busqueda)
    only_going = ctk.CTkCheckBox(frame_busqueda, text="solo ida", variable=going, onvalue="solo ida", offvalue = 2)
    cities_origin = ctk.CTkComboBox(frame_busqueda, values=list(origen), state="readonly")  # steate readonly para que no se pueda escribir
    cities_origin.set("Ciudad de origen")  # coloca un texto por defecto
    cities_destination = ctk.CTkComboBox(frame_busqueda, values=list(destino), state="readonly")  # steate readonly para que no se pueda escribir
    cities_destination.set("Ciudad de destino")  # coloca un texto por defecto
    list_going = ctk.CTkComboBox(frame_busqueda, values=dates_june, state="readonly")  # steate readonly para que no se pueda escribir
    list_going.set("ida")  # coloca un texto por defecto
    
    # creacion de frame para el boton de busqueda
    frame_button_search = ctk.CTkFrame(window_fly)
    frame_button_search.configure(width = 20 , height = 25  ,fg_color = "grey26")
    
    button_search = ctk.CTkButton(frame_button_search, text="BUSCAR", command=lambda: conditions_searchs(cities_destination.get(), cities_origin.get(), entry_passenger.get(),window_fly), width=30, height=10)

    # dar posicion a los elementos de la pantalla de menu fly
    
    
    frame_busqueda.grid(row=8, column=0)
    frame_button_search.grid(row=20, column=0, sticky="nsew", padx=150, pady=50)
    cities_origin.grid(row=8, column=0)
    cities_destination.grid(row=8, column=1)
    list_going.grid(row=8, column=2, padx=10, pady=10)
    only_going.grid(row=0, column=0)
    button_search.place(relx = 0.5, rely = 0.5, anchor = "center")
    label_passenger.grid(row=8, column=5, padx=10, pady=10)
    entry_passenger.grid(row=8, column=6, padx=10, pady=10)
    window_fly.mainloop()
    return window_fly


# funcion para buscar vuelos disponibles
def search_fly(indices, window_fly):
    window_fly.destroy()
    df = pd.read_csv("dato_vuelo.csv")
    window_search = ctk.CTk()
    window_search.geometry("500x500")
    window_search.resizable(0, 0)
    window_search.title("busqueda de vuelos")
    #crear frame para el label
    frame_label = ctk.CTkFrame(window_search)
    frame_label.configure(fg_color = "grey26")
    frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    label = ctk.CTkLabel(frame_label, text=f"IDA: {df['CiudadDestino'].values[indices[0]]} desde {df['CiudadOrigen'].values[indices[0]]}")
    label.grid(row=0, column=0)
    
    # creacion de frame para los botones
    frame_buttons = ctk.CTkFrame(window_search)
    frame_buttons.configure(fg_color = "grey26")
    frame_buttons.grid(row=1, column=0, padx=10, pady=10) 
    # creacion de botones
    botones = []
    for i in range(len(indices) - 1):
        button_see = ctk.CTkButton(frame_buttons, text=f"{df['Fecha'].values[indices[i]]} {df['ValorMedio'].values[indices[i]]}")
        button_see.grid(row=0, column=i, padx=10, pady=10)
        botones.append(button_see)
    
    window_search.mainloop()

#______________________________________________________
    #darle posicion a los botones y elementos de la pantalla de busqueda de vuelos






#verifica los datos del registro
# def record_condition(gender,name,lastname,id,telephone,nationality,email,birthday,attendance):
#     if c.conditions_record(gender,name,lastname,id,telephone,nationality,email,birthday,attendance):
#         s.record_base(gender,name,lastname,id,telephone,nationality,email,birthday,attendance)
# #_______________________________________________________________________________________________________________________
# # funcion para el registro

# def record(window):
#     global checkbox,checkbox1,radiuobutton,radiuobutton1
#     window.destroy()
#     window_record=tk.Tk()
#     window_record.title("registro")
#     window_record.config(bg="black")
#     window_record.geometry()
#     gender=tk.StringVar()  # variable para almacenar el genero
#     label_gender=tk.Label(window_record,text="genero", bg="red",fg="white",font=("Times New Roman",14))
#     checkbox=tk.Radiobutton(window_record,text="masculino",bg="red",fg="white",variable=gender,value="masculino",font=("Times New Roman",14))
#     checkbox1=tk.Radiobutton(window_record,text="femenino",bg="red",fg="white",variable=gender,value="femenino", font =("Times New Roman",14))
#     label_name=tk.Label(window_record,text="nombre",bg="red",fg="white", font= ("Times New Roman",14))
#     entry_name=tk.Entry(window_record,font=("Times New Roman",14))
#     label_lastname=tk.Label(window_record,text="apellido",bg="red",fg="white",font=("Times New Roman",14))
#     entry_lastname=tk.Entry(window_record,font=("Times New Roman",14))
#     label_id=tk.Label(window_record,text="identificacion",bg="red",fg="white",font=("Times New Roman",14))
#     entry_id=tk.Entry(window_record,font=("Times New Roman",14))
#     label_telephone=tk.Label(window_record,text="telefono",bg="red",fg="white",font=("Times New Roman",14))
#     entry_telephone=tk.Entry(window_record,font=("Times New Roman",14))
#     label_nationality=tk.Label(window_record,text="nacionalidad",bg="red",fg="white",font=("Times New Roman",14))
#     entry_nationality=tk.Entry(window_record,font=("Times New Roman",14))
#     label_email=tk.Label(window_record,text="correo",bg="red",fg="white",font=("Times New Roman",14))
#     entry_email=tk.Entry(window_record,font=("Times New Roman",14))
#     label_birthday=tk.Label(window_record,text="fecha de nacimiento",bg="red",fg="white",font=("Times New Roman",14))
#     entry_birthday=tk.Entry(window_record,font=("Times New Roman",14))#fuente de letra
#     attendance=tk.StringVar()
#     label_attendance=tk.Label(window_record,text="requiere asistencia",bg="red",fg="white",font=("Times New Roman",14))
#     radiuobutton=tk.Radiobutton(window_record,text="asistencia",bg="red",fg="white",variable=attendance,value="requiere",activebackground="green",font=("Times New Roman",14))
#     radiuobutton1=tk.Radiobutton(window_record,text="no asistencia",bg="red",fg="white",variable=attendance,value="no requiere",font = ("Times New Roman",14))
#     #boton de enviar
#     button_send=tk.Button(window_record,text="enviar",bg="red",fg="white",command=lambda:record_condition(gender.get(),entry_name.get(),entry_lastname.get(),entry_id.get(),entry_telephone.get(),entry_nationality.get(),entry_email.get(),entry_birthday.get(),attendance.get()),activebackground="green",font=("Times New Roman",14))
#     button_back = tk.Button(window_record,text="volver",bg="red",fg="white",command=lambda:return_menu(window_record),width=9,height=2,activebackground="green",font=("Times New Roman",14))
#     #eventos para teclas
#     #____________________________________________________________________________
#     window_record.bind("<Return>",lambda e:record_condition(gender.get(),entry_name.get(),entry_lastname.get(),entry_id.get(),entry_telephone.get(),entry_nationality.get(),entry_email.get(),entry_birthday.get(),attendance.get()))
#     window_record.bind("<Escape>",lambda e:return_menu(window_record))
# #_______________________________________________________________________________-
#     # darle posicion a los elementos de la pantalla de registro
#     label_gender.grid(row=0,column=0,padx=10,pady=10)
#     checkbox.grid(row=0,column=1,padx=10,pady=10)
#     checkbox1.grid(row=0,column=2,padx=10,pady=10)
#     label_name.grid(row=1,column=0,padx=10,pady=10)
#     entry_name.grid(row=1,column=1,padx=10,pady=10)
#     label_lastname.grid(row=1,column=2,padx=10,pady=10)
#     entry_lastname.grid(row=1,column=3,padx=10,pady=10)
#     label_id.grid(row=2,column=0,padx=10,pady=10)
#     entry_id.grid(row=2,column=1,padx=10,pady=10)
#     label_telephone.grid(row=2,column=2,padx=10,pady=10)
#     entry_telephone.grid(row=2,column=3,padx=10,pady=10)
#     label_nationality.grid(row=3,column=0,padx=10,pady=10)
#     entry_nationality.grid(row=3,column=1,padx=10,pady=10)
#     label_email.grid(row=3,column=2,padx=10,pady=10)
#     entry_email.grid(row=3,column=3,padx=10,pady=10)
#     button_send.grid(row=7,column=0,padx=10,pady=10)
#     label_birthday.grid(row=4,column=0,padx=10,pady=10)
#     entry_birthday.grid(row=4,column=1,padx=10,pady=10)
#     label_attendance.grid(row=5,column=0,padx=10,pady=10)
#     radiuobutton.grid(row=6,column=0,padx=10,pady=10)
#     radiuobutton1.grid(row=6,column=1,padx=10,pady=10)
#     button_back.grid(row=7,column=1,padx=10,pady=10)
#     window_record.mainloop()


# #_______________________________________________________________________________________________________________________
# def login_condition(id,email):
#     if c.condition_login(id,email):
#         s.login_base(id,email)
#_______________________________________________________________________________________________________________________
# funcion  para iniciar sesion

# def login(window):
#     window.destroy()
#     window_login=ctk.CTk()
#     window_login.title("iniciar sesion")
#     window_login.geometry()
#     label_id=ctk.CTkLabel(window_login,text="identificacion")
#     entry_id=ctk.CTkEntry(window_login)
#     label_email=ctk.CTkLabel(window_login,text="correo")
#     entry_email=ctk.CTkEntry (window_login)
#     button_back = ctk.CTkButton(window_login,text="volver",command=lambda:return_menu(window_login),width=9,height=2)
#     button_send=ctk.CTkButton(window_login,text="enviar",command=lambda:login_condition(entry_id.get(),entry_email.get()),width=9,height=2)
#     # darle posicion a los elementos de la pantalla de inicio de sesion
#     #atajos de teclas
#     window_login.bind("<Return>",lambda e:login_condition(entry_id.get(),entry_email.get()))
#     window_login.bind("<Escape>",lambda e:return_menu(window_login))
#     #____________________________________________________________________________
    
#     label_id.grid(row=0,column=0,padx=10,pady=10)
#     entry_id.grid(row=0,column=1,padx=10,pady=10)
#     label_email.grid(row=1,column=0,padx=10,pady=10)
#     entry_email.grid(row=1,column=1,padx=10,pady=10)
#     button_send.grid(row=2,column=0,padx=10,pady=10)
#     button_back.grid(row=2,column=1,padx=10,pady=10)
#     window_login.mainloop()

# # Funcion del menu
# def menu():
#     window_menu=ctk.CTk()
#     window_menu.title("menu")
#     window_menu.config(bg="white")
#     window_menu.geometry()
#     label=ctk.CTkLabel(window_menu,text="Menu")
#     #____________________________________________________________________________________
#     #creacion de botones
#     button_record=ctk.CTkButton(window_menu,text="registrarse",command=lambda:record(window_menu),width=9,height=2)
#     button_login=ctk.CTkButton(window_menu,text="iniciar sesion",command=lambda:login(window_menu),width=9,height=2)
#     button_out=ctk.CTkButton(window_menu,text="salir",command=lambda:window_menu.destroy(),width=9,height=2)
#     #___________________________________________________________________________________
#     #darle posicion a los botones y elementos de la pantalla de menu
#     #eventos de teclas
#     window_menu.bind("<Control_L>",lambda e:record(window_menu)) 
#     window_menu.bind("<Return>",lambda e:login(window_menu))
#     window_menu.bind("<Escape>",lambda e:window_menu.destroy())
#     #____________________________________________________________________________
#     label.grid(row=0,column=0)
#     button_record.grid(row=2,column=0,padx=30,pady=15)
#     button_login.grid(row=3,column=0,padx=30,pady=15)
#     button_out.grid(row=4,column=0,padx=30,pady=15)
#     window_menu.mainloop()



if __name__=='__main__':
    fly()

    
    # menu()