import pandas as pd

import random as rd

import os

for i in range(50):
    plata = rd.randint(3000000, 20000000)
    codigo= rd.randint(100,999)
    nombres_lista = ["sebastian","nicolas","pepe","dorian","simon","camilo"]
    apellidos_list = ["rubio","devia","perez","navarrete","tarazona","melo"]
    num_tarjeta=rd.randint(1000000000000000,9999999999999999)
    #tarjeta poner
    data={"tarjeta":[num_tarjeta],"codigo":[codigo],"nombre":[rd.choice(nombres_lista)],"apellido":[rd.choice(apellidos_list)]}
    df=pd.DataFrame(data)
    if os.path.exists("tarjetas.csv"):
        df.to_csv("tarjetas.csv",mode="a",sep=",", header=False,index=False)
    else:
        df.to_csv("tarjetas.csv",mode="a",sep=",",index=False)
print(df)