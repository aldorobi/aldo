# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:04:02 2023

@author: Aldo
"""



import requests
from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from googletrans import Translator, LANGUAGES


TraductorChafa = Tk()
TraductorChafa.title("Traductor")
TraductorChafa.geometry("740x600")
TraductorChafa.configure(background = "thistle4")

label0 = Label(TraductorChafa,text = "traductor")
label0.place(relx = 0.475 , rely = 0.1 , anchor = CENTER)

label1 = Label(TraductorChafa,text = "entrada")
label1.place(relx = 0.2 , rely = 0.3 , anchor = CENTER)

label2 = Label(TraductorChafa,text = "salida")
label2.place(relx = 0.75 , rely = 0.3 , anchor = CENTER)


language = list(LANGUAGES.values())


Lisuegosos = ttk.Combobox(TraductorChafa,state = "readonly",font = ("Sans serif",10,"bold"),values = language)
Lisuegosos.place(relx = 0.2, rely = 0.35,anchor = CENTER)

Lisuegososos = ttk.Combobox(TraductorChafa,state = "readonly",font = ("Sans serif",10,"bold"),values = language)
Lisuegososos.place(relx = 0.75, rely = 0.35,anchor = CENTER)

pato = Text(TraductorChafa,width = 35, height = 1)
pato.place(relx = 0.2 , rely = 0.40 , anchor = CENTER)
 
ganso = Text(TraductorChafa,width = 35, height = 1)
ganso.place(relx = 0.75 , rely = 0.40 , anchor = CENTER)
 
def Traduce():
    Traductor = Translator()
    try:
        Intento1 = Traductor.translate(text = pato.get(1.0,END), src = Lisuegosos.get(), dest = Lisuegososos.get())
        ganso.delete(1.0,END)
        ganso.insert(END,Intento1.text)
    
    except:
        print('no')
        

boo = Button(TraductorChafa, text = "traducir/translate", command = Traduce)
boo.place(relx = 0.475 , rely = 0.40, anchor = CENTER)



     
TraductorChafa.mainloop()