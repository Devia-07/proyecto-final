import pandas as pd

import random as rd

import os

for i in range(50):
    money = rd.randint(3000000, 20000000)
    code= rd.randint(100,999)
    f_name_list = ["sebastian","nicolas","pepe","dorian","simon","camilo"]
    l_name_list = ["rubio","devia","perez","navarrete","tarazona","melo"]
    num_tarjeta=rd.randint(1000000000000000,9999999999999999)
    #tarjeta poner
    data={"tarjeta":[num_tarjeta],"codigo":[code],"nombre":[rd.choice(f_name_list)],"apellido":[rd.choice(l_name_list)]}
    df=pd.DataFrame(data)
    if os.path.exists("tarjetas.csv"):
        df.to_csv("tarjetas.csv",mode="a",sep=",", header=False,index=False)
    else:
        df.to_csv("tarjetas.csv",mode="a",sep=",",index=False)
print(df)