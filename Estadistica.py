import pandas as pd
from tkinter import *
import tkinter as tk

def preguntaCalcular():
    print('0. Minimo \n 1. Maximo \n 2. Media aritmetica \n 3. desviacion tipica \n 4. Cerrar')
    valor = int(input("Que deseas calcular?: "))
    return valor

def preguntaVariable():
    valor = input('De cual variable quieres calcular los datos: ')
    return valor

def calcularEstadisticos(datos, variable, operacion):
    calcular = pd.Series(datos[variable])
    estadisticos = {}
    if (operacion == 0):
        estadisticos[f'Minimo de {variable}'] = [calcular.min()]
    elif operacion == 1:
        estadisticos[f'Maximo de {variable}'] = [calcular.max()]
    elif operacion == 2:
        estadisticos[f'Media de {variable}'] = [calcular.mean()]
    elif operacion == 3:
        estadisticos[f'Desviación típica de {variable}'] = [calcular.std()]
    else:
        return 0
    return estadisticos

def calcularMin(datos, variable):
    calcular = pd.Series(datos[variable])
    estadisticos = {}
    estadisticos[f'Minimo de {variable}'] = [calcular.min()]
    return estadisticos

def calcularMax(datos, variable):
    calcular = pd.Series(datos[variable])
    estadisticos = {}
    estadisticos[f'Maximo de {variable}'] = [calcular.max()]
    return estadisticos

def calcularMedia(datos, variable):
    calcular = pd.Series(datos[variable])
    estadisticos = {}
    estadisticos[f'Media de {variable}'] = [calcular.mean()]
    return estadisticos

def calcularDvst(datos, variable):
    calcular = pd.Series(datos[variable])
    estadisticos = {}
    estadisticos[f'Desviación típica de {variable}'] = [calcular.std()]
    return estadisticos

def printDataFrame(datos):
    tabla = pd.DataFrame(datos)
    print(tabla)

def cambiarMax():
    variable = Etabla.get()
    newtable = calcularMax(datos,variable)
    pdnewtable = pd.DataFrame(newtable)
    table.insert(tk.INSERT, '\n' + pdnewtable.to_string())

def cambiarMin():
    variable = Etabla.get()
    newtable = calcularMin(datos,variable)
    pdnewtable = pd.DataFrame(newtable)
    table.insert(tk.INSERT,'\n' + pdnewtable.to_string())

def cambiarMedia():
    variable = Etabla.get()
    newtable = calcularMedia(datos,variable)
    pdnewtable = pd.DataFrame(newtable)
    table.insert(tk.INSERT, '\n' + pdnewtable.to_string())

def cambiarDvst():
    variable = Etabla.get()
    newtable = calcularDvst(datos,variable)
    pdnewtable = pd.DataFrame(newtable)
    table.insert(tk.INSERT,'\n' + pdnewtable.to_string())

datos =pd.DataFrame( {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas': [
    30500, 35600, 28300, 33900], 'Gastos': [22000, 23400, 18100, 20700]})

gui = tk.Tk()
Ltabla=Label(gui,text="Digite la columna de la cual desea obtener los datos")
Etabla=Entry(gui,width=10)
BMax=Button(gui,text="Calcular Max",command=cambiarMax)
Bmin=Button(gui,text="Calcular Min",command=cambiarMin)
Bmedia=Button(gui,text="Calcular Media",command=cambiarMedia)
Bdvst=Button(gui,text="Calcular Desviación tipica",command=cambiarDvst)

table = tk.Text(gui)
table.insert(tk.INSERT, datos.to_string())

table.pack()
datext = tk.Text(gui)
Ltabla.pack()
Etabla.pack()
BMax.pack()
Bmin.pack()
Bmedia.pack()
Bdvst.pack()
gui.mainloop()