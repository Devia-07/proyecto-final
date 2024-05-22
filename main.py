import tkinter as tk 
from tkinter import messagebox as mb
from tkinter import ttk
import pandas as pd 
import os 
import PIL as pil
import conditions as c 
import  save as s
import datetime 
from tkcalendar import Calendar


def return_menu(window):
    window.destroy()
    menu()








def conditions_searchs(destination,origin,passenger):
    indices=[]
    if c.conditions_search(destination,origin,passenger)==True:
        mb.showinfo("info","datos correctos")
        indices=c.search(destination,origin)
        search_fly(indices)
    else:
        mb.showerror("error","datos incorrectos")


def fly():
    origen=[]
    destino=[]
    fecha=[]
    origen,destino,fecha =c.lista_vuelos(origen,destino,fecha)
    window_fly=tk.Tk()
    window_fly.title("menu fly")
    window_fly.config(bg="white")
    window_fly.geometry()
    label=tk.Label(window_fly,text="Menu",bg="red",fg="white")
    # crear una lista de dias de junio
    dates_june = [f"2024-06-{day:02d}" for day in range(1, 31)]
    going = tk.StringVar()

# creacion de elementos de la pantalla de menu fly

#____________________________________________________________________________________
    label_passenger = tk.Label(window_fly,text="numero de pasajeros",bg="red",fg="white",font=("Times New Roman", 14))
    entry_passenger = tk.Entry(window_fly,font=("Times New Roman", 14))
#____________________________________________________________________________________
    only_going = tk.Radiobutton(window_fly, text="solo ida", variable=going,value = "solo ida", bg="red", fg="white", font=("Times New Roman", 12))
#____________________________________________________________________________________
    cities_origin = ttk.Combobox(window_fly,values=origen,state="readonly") # steate readonly para que no se pueda escribir
    cities_origin.set("Ciudad de origen")  # coloca un texto por defecto
#____________________________________________________________________________________
    cities_destination = ttk.Combobox(window_fly,values=destino,state="readonly")  # steate readonly para que no se pueda escribir
    cities_destination.set("Ciudad de destino")  # coloca un texto por defecto
#____________________________________________________________________________________
    list_going = ttk.Combobox(window_fly,values = dates_june,state="readonly")  # steate readonly para que no se pueda escribir
    list_going.set("ida")  # coloca un texto por defecto
    
#____________________________________________________________________________________
    button_search = tk.Button(window_fly,text="buscar",bg="red",fg="white",command=lambda:conditions_searchs(cities_destination.get(),cities_origin.get(),entry_passenger.get()),width=9,height=2,activebackground="green")
#____________________________________________________________________________________
#____________________________________________________________________________________
    # dar posicion a los elementos de la pantalla de menu fly
    cities_origin.grid(row=8,column=0)
    cities_destination.grid(row=8,column=1)
    list_going.grid(row=8,column=2,padx=10,pady=10)
    only_going.grid(row=0,column=0)
    button_search.grid(row=9,column=0,padx=10,pady=10)
    label_passenger.grid(row=1,column=5,padx=10,pady=10)
    entry_passenger.grid(row=1,column=6,padx=10,pady=10)

    window_fly.mainloop()
#_______________________________________________________________________________________________________________________
#funcion para buscar vuelos disponibles
def search_fly(indices):
    df=pd.read_csv("dato_vuelo.csv")
    window_search=tk.Tk()
    window_search.title("busqueda de vuelos")
    window_search.config(bg="white")
    window_search.geometry()
    label=tk.Label(window_search,text="busqueda de vuelos",bg="red",fg="white")
#____________________________________________________________________________________
    #creacion de botones
    botones=[]
    for i in range(len(indices)-1):
        button_see=tk.Button(window_search,text=f"{df["Fecha"].values[indices[i]]} {df["ValorMedio"].values[indices[i]]}",bg="red",fg="white",activebackground="green")
        button_see.grid(row=0,column=i,padx=10,pady=10)
        botones.append(button_see)
        
        
    
#___________________________________________________________________________________
    #darle posicion a los botones y elementos de la pantalla de busqueda de vuelos






#verifica los datos del registro
def record_condition(gender,name,lastname,id,telephone,nationality,email,birthday,attendance):
    if c.conditions_record(gender,name,lastname,id,telephone,nationality,email,birthday,attendance)==True:
        s.record_base(gender,name,lastname,id,telephone,nationality,email,birthday,attendance)
#_______________________________________________________________________________________________________________________
# funcion para el registro

def record(window):
    global checkbox,checkbox1,radiuobutton,radiuobutton1
    window.destroy()
    window_record=tk.Tk()
    window_record.title("registro")
    window_record.config(bg="black")
    window_record.geometry()
    gender=tk.StringVar()  # variable para almacenar el genero
    label_gender=tk.Label(window_record,text="genero", bg="red",fg="white",font=("Times New Roman",14))
    checkbox=tk.Radiobutton(window_record,text="masculino",bg=f"red",fg="white",variable=gender,value="masculino",font=("Times New Roman",14))
    checkbox1=tk.Radiobutton(window_record,text="femenino",bg=f"red",fg="white",variable=gender,value="femenino", font =("Times New Roman",14))
    label_name=tk.Label(window_record,text="nombre",bg="red",fg="white", font= ("Times New Roman",14))
    entry_name=tk.Entry(window_record,font=("Times New Roman",14))
    label_lastname=tk.Label(window_record,text="apellido",bg="red",fg="white",font=("Times New Roman",14))
    entry_lastname=tk.Entry(window_record,font=("Times New Roman",14))
    label_id=tk.Label(window_record,text="identificacion",bg="red",fg="white",font=("Times New Roman",14))
    entry_id=tk.Entry(window_record,font=("Times New Roman",14))
    label_telephone=tk.Label(window_record,text="telefono",bg="red",fg="white",font=("Times New Roman",14))
    entry_telephone=tk.Entry(window_record,font=("Times New Roman",14))
    label_nationality=tk.Label(window_record,text="nacionalidad",bg="red",fg="white",font=("Times New Roman",14))
    entry_nationality=tk.Entry(window_record,font=("Times New Roman",14))
    label_email=tk.Label(window_record,text="correo",bg="red",fg="white",font=("Times New Roman",14))
    entry_email=tk.Entry(window_record,font=("Times New Roman",14))
    label_birthday=tk.Label(window_record,text="fecha de nacimiento",bg="red",fg="white",font=("Times New Roman",14))
    entry_birthday=tk.Entry(window_record,font=("Times New Roman",14))#fuente de letra
    attendance=tk.StringVar()
    label_attendance=tk.Label(window_record,text="requiere asistencia",bg="red",fg="white",font=("Times New Roman",14))
    radiuobutton=tk.Radiobutton(window_record,text="asistencia",bg="red",fg="white",variable=attendance,value="requiere",activebackground="green",font=("Times New Roman",14))
    radiuobutton1=tk.Radiobutton(window_record,text="no asistencia",bg="red",fg="white",variable=attendance,value="no requiere",font = ("Times New Roman",14))
    #boton de enviar
    button_send=tk.Button(window_record,text="enviar",bg="red",fg="white",command=lambda:record_condition(gender.get(),entry_name.get(),entry_lastname.get(),entry_id.get(),entry_telephone.get(),entry_nationality.get(),entry_email.get(),entry_birthday.get(),attendance.get()),activebackground="green",font=("Times New Roman",14))
    button_back = tk.Button(window_record,text="volver",bg="red",fg="white",command=lambda:return_menu(window_record),width=9,height=2,activebackground="green",font=("Times New Roman",14))
    #eventos para teclas
    #____________________________________________________________________________
    window_record.bind("<Return>",lambda e:record_condition(gender.get(),entry_name.get(),entry_lastname.get(),entry_id.get(),entry_telephone.get(),entry_nationality.get(),entry_email.get(),entry_birthday.get(),attendance.get()))
    window_record.bind("<Escape>",lambda e:return_menu(window_record))
#_______________________________________________________________________________-
    # darle posicion a los elementos de la pantalla de registro
    label_gender.grid(row=0,column=0,padx=10,pady=10)
    checkbox.grid(row=0,column=1,padx=10,pady=10)
    checkbox1.grid(row=0,column=2,padx=10,pady=10)
    label_name.grid(row=1,column=0,padx=10,pady=10)
    entry_name.grid(row=1,column=1,padx=10,pady=10)
    label_lastname.grid(row=1,column=2,padx=10,pady=10)
    entry_lastname.grid(row=1,column=3,padx=10,pady=10)
    label_id.grid(row=2,column=0,padx=10,pady=10)
    entry_id.grid(row=2,column=1,padx=10,pady=10)
    label_telephone.grid(row=2,column=2,padx=10,pady=10)
    entry_telephone.grid(row=2,column=3,padx=10,pady=10)
    label_nationality.grid(row=3,column=0,padx=10,pady=10)
    entry_nationality.grid(row=3,column=1,padx=10,pady=10)
    label_email.grid(row=3,column=2,padx=10,pady=10)
    entry_email.grid(row=3,column=3,padx=10,pady=10)
    button_send.grid(row=7,column=0,padx=10,pady=10)
    label_birthday.grid(row=4,column=0,padx=10,pady=10)
    entry_birthday.grid(row=4,column=1,padx=10,pady=10)
    label_attendance.grid(row=5,column=0,padx=10,pady=10)
    radiuobutton.grid(row=6,column=0,padx=10,pady=10)
    radiuobutton1.grid(row=6,column=1,padx=10,pady=10)
    button_back.grid(row=7,column=1,padx=10,pady=10)
    window_record.mainloop()


#_______________________________________________________________________________________________________________________
def login_condition(id,email):
    if c.condition_login(id,email)==True:
        s.login_base(id,email)
#_______________________________________________________________________________________________________________________
# funcion  para iniciar sesion

def login(window):
    window.destroy()
    window_login=tk.Tk()
    window_login.title("iniciar sesion")
    window_login.config(bg="white")
    window_login.geometry()
    label_id=tk.Label(window_login,text="identificacion",bg="red",fg="white")
    entry_id=tk.Entry(window_login)
    label_email=tk.Label(window_login,text="correo",bg="red",fg="white")
    entry_email=tk.Entry (window_login)
    button_back = tk.Button(window_login,text="volver",bg="red",fg="white",command=lambda:return_menu(window_login),width=9,height=2,activebackground="green")
    button_send=tk.Button(window_login,text="enviar",bg="red",fg="white",command=lambda:login_condition(entry_id.get(),entry_email.get()),width=9,height=2,activebackground="green")
    # darle posicion a los elementos de la pantalla de inicio de sesion
    #atajos de teclas
    window_login.bind("<Return>",lambda e:login_condition(entry_id.get(),entry_email.get()))
    window_login.bind("<Escape>",lambda e:return_menu(window_login))
    #____________________________________________________________________________
    
    label_id.grid(row=0,column=0,padx=10,pady=10)
    entry_id.grid(row=0,column=1,padx=10,pady=10)
    label_email.grid(row=1,column=0,padx=10,pady=10)
    entry_email.grid(row=1,column=1,padx=10,pady=10)
    button_send.grid(row=2,column=0,padx=10,pady=10)
    button_back.grid(row=2,column=1,padx=10,pady=10)
    window_login.mainloop()

# Funcion del menu
def menu():
    window_menu=tk.Tk()
    window_menu.title("menu")
    window_menu.config(bg="white")
    window_menu.geometry()
    label=tk.Label(window_menu,text="Menu",bg="red",fg="white")
    #____________________________________________________________________________________
    #creacion de botones
    button_record=tk.Button(window_menu,text="registrarse",bg="red",fg="white",command=lambda:record(window_menu),width=9,height=2,activebackground="green")
    button_login=tk.Button(window_menu,text="iniciar sesion",bg="red",fg="white",command=lambda:login(window_menu),width=9,height=2,activebackground="green")
    button_out=tk.Button(window_menu,text="salir",bg="red",fg="white",command=lambda:window_menu.destroy(),width=9,height=2,activebackground="green")
    #___________________________________________________________________________________
    #darle posicion a los botones y elementos de la pantalla de menu
    #eventos de teclas
    window_menu.bind("<Control_L>",lambda e:record(window_menu)) 
    window_menu.bind("<Return>",lambda e:login(window_menu))
    window_menu.bind("<Escape>",lambda e:window_menu.destroy())
    #____________________________________________________________________________
    label.grid(row=0,column=0)
    button_record.grid(row=2,column=0,padx=30,pady=15)
    button_login.grid(row=3,column=0,padx=30,pady=15)
    button_out.grid(row=4,column=0,padx=30,pady=15)
    window_menu.mainloop()



if __name__=='__main__':
    fly()
    # menu()