import pandas as pd 
import os
from tkinter import messagebox as mb
import main as mn

def record_base(gender,name,lastname,id,telephone,nationality,email,birthday,attendance,window):

    # utiliza .strip() para eliminar espacios en blanco al inicio y al final de cada cadena y guardar los daots sin espacio
    
    data={"documento":[id.strip()],"nombre":[name.strip()],"apellido":[lastname.strip()],"telefono":[telephone.strip()],"nacionalidad":[nationality.strip()], "correo":[email.strip()],"fecha de nacimiento":[birthday.strip()],"genero":[gender.strip()],"asistencia":[attendance.strip()]}
    df=pd.DataFrame(data)
    if not os.path.isfile("registro_usuarios.csv"):
        df.to_csv("registro_usuarios.csv",index=False,header=True,mode="a",sep=";")
    else:
        df.to_csv("registro_usuarios.csv",index=False,header=False,mode="a",sep=";")
        mb.showinfo("registro","registro exitoso")
        mn.return_menu(window)

