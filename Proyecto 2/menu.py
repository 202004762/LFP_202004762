from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lector import Lector
from procesador import Procesador
import time


filereader = Lector()
processor = Procesador()

glc_array = []
ap_array = []

def ventanaMain():
    global ventanaMain
    ventanaMain = Tk()
    ventanaMain.title("Welcome")

    screen_width = ventanaMain.winfo_screenwidth()
    screen_height = ventanaMain.winfo_screenheight()

    ventanaMain_width = 300
    ventanaMain_height = 100

    x = (screen_width - ventanaMain_width) // 2
    y = (screen_height - ventanaMain_height) // 2

    ventanaMain.geometry(f"{ventanaMain_width}x{ventanaMain_height}+{x}+{y}")
    ventanaMain.configure(bg="gray")

    Label(ventanaMain, text="Angel Guillermo Arreaga Barrientos", font=("Arial", 12), background = "gray").pack(padx=10, pady=10)
    Label(ventanaMain, text="202004762", font=("Arial", 12), background = "gray").pack(padx=10, pady=10)

    ventanaMain.after(5000, ventanaPrincipal)
    ventanaMain.after(5000, ventanaMain.withdraw)

    ventanaMain.mainloop()

def ventanaPrincipal():
    global ventanaPrincipal
    ventanaPrincipal = Tk()
    ventanaPrincipal.title("Menu Principal")

    screen_width = ventanaPrincipal.winfo_screenwidth()
    screen_height = ventanaPrincipal.winfo_screenheight()

    ventanaPrincipal_width = 300
    ventanaPrincipal_height = 300

    x = (screen_width - ventanaPrincipal_width) // 2
    y = (screen_height - ventanaPrincipal_height) // 2

    ventanaPrincipal.geometry(f"{ventanaPrincipal_width}x{ventanaPrincipal_height}+{x}+{y}")
    ventanaPrincipal.configure(bg="#37474f")

    Button(ventanaPrincipal, text="Gramatica libre de contexto", height="2", width="30", command = ventanaOFC).pack(padx=10, pady=10)
    Button(ventanaPrincipal, text="Automotas de pila", height="2", width="30", command = ventanaAP).pack(padx=10, pady=40)
    Button(ventanaPrincipal, text="Salir", height="2", width="30", command = salir).pack(padx=10, pady=40)

    ventanaPrincipal.mainloop()

def ventanaOFC():
    global ventanaOFC
    ventanaOFC = Toplevel(ventanaPrincipal)
    ventanaOFC.title("Gramatica Libre de Contexto")

    screen_width = ventanaOFC.winfo_screenwidth()
    screen_height = ventanaOFC.winfo_screenheight()

    ventanaOFC_width = 300
    ventanaOFC_height = 300

    x = (screen_width - ventanaOFC_width) // 2
    y = (screen_height - ventanaOFC_height) // 2

    ventanaOFC.geometry(f"{ventanaOFC_width}x{ventanaOFC_height}+{x}+{y}")
    ventanaOFC.configure(bg="#37474f")

    Button(ventanaOFC, text="Cargar archivo", height="2", width="30", command = lambda: upload_file(1, glc_array, ap_array)).pack(padx=10, pady=10)
    Button(ventanaOFC, text="Mostrar información general", height="2", width="30", command = ventanaInfoGeneral).pack(padx=10, pady=10)
    Button(ventanaOFC, text="Árbol de derivación", height="2", width="30").pack(padx=10, pady=10)
    Button(ventanaOFC, text="Regresar", height="2", width="30", command = volverMenuPrincipal1).pack(padx=10, pady=40)

    if(ventanaOFC):
        ventanaPrincipal.withdraw()

    ventanaOFC.mainloop()

def ventanaAP():
    global ventanaAP
    ventanaAP = Toplevel(ventanaPrincipal)
    ventanaAP.title("Automatas de Pila")

    screen_width = ventanaAP.winfo_screenwidth()
    screen_height = ventanaAP.winfo_screenheight()

    ventanaAP_width = 300
    ventanaAP_height = 500

    x = (screen_width - ventanaAP_width) // 2
    y = (screen_height - ventanaAP_height) // 2

    ventanaAP.geometry(f"{ventanaAP_width}x{ventanaAP_height}+{x}+{y}")
    ventanaAP.configure(bg="#37474f")

    Button(ventanaAP, text="Cargar archivo", height="2", width="30", command = lambda: upload_file(2, glc_array, ap_array)).pack(padx=10, pady=10)
    Button(ventanaAP, text="Mostrar información de autómata", height="2", width="30", command = ventanaMostrarInfo).pack(padx=10, pady=10)
    Button(ventanaAP, text="Validar una cadena", height="2", width="30").pack(padx=10, pady=10)
    Button(ventanaAP, text="Ruta de validación", height="2", width="30").pack(padx=10, pady=10)
    Button(ventanaAP, text="Recorrido paso a paso", height="2", width="30").pack(padx=10, pady=10)
    Button(ventanaAP, text="Validar cadena en una pasada", height="2", width="30").pack(padx=10, pady=10)
    Button(ventanaAP, text="Regresar", height="2", width="30", command = volverMenuPrincipal2).pack(padx=10, pady=40)

    if(ventanaAP):
        ventanaPrincipal.withdraw()

    ventanaAP.mainloop()

def ventanaInfoGeneral():
    global ventanaInfoGeneral
    ventanaInfoGeneral = Toplevel(ventanaOFC)
    ventanaInfoGeneral.title("Información General")

    screen_width = ventanaInfoGeneral.winfo_screenwidth()
    screen_height = ventanaInfoGeneral.winfo_screenheight()

    ventanaInfoGeneral_width = 800
    ventanaInfoGeneral_height = 500

    x = (screen_width - ventanaInfoGeneral_width) // 2
    y = (screen_height - ventanaInfoGeneral_height) // 2

    ventanaInfoGeneral.geometry(f"{ventanaInfoGeneral_width}x{ventanaInfoGeneral_height}+{x}+{y}")
    ventanaInfoGeneral.configure(bg="#37474f")

    table = ttk.Treeview(ventanaInfoGeneral)
    table.pack(padx=10, pady=10)
    table['columns'] = ('glc_nombre', 'glc_noTerminal', 'glc_terminal', 'glc_inicial', 'glc_produccion')

    table.column('#0', width=0, stretch=NO)
    table.column('glc_nombre', anchor=CENTER, width=75)
    table.column('glc_noTerminal', anchor=CENTER, width=100)
    table.column('glc_terminal', anchor=CENTER, width=75)
    table.column('glc_inicial', anchor=CENTER, width=50)
    table.column('glc_produccion', anchor=CENTER, width=400)

    table.heading('#0', text='', anchor=CENTER)
    table.heading('glc_nombre', text='Nombre', anchor=CENTER)
    table.heading('glc_noTerminal', text='No Terminales', anchor=CENTER)
    table.heading('glc_terminal', text='Terminales', anchor=CENTER)
    table.heading('glc_inicial', text='Inicial', anchor=CENTER)
    table.heading('glc_produccion', text='Producciones', anchor=CENTER)

    cont = 0
    for glc in glc_array:
        table.insert("", "end", iid=cont, text='',
        values=(glc.nombre, glc.noTerminal, glc.terminal, glc.inicial, glc.produccion))
        cont += 1

    Button(ventanaInfoGeneral, text="Regresar", height="2", width="30", command = regresarOFC).pack(padx=10, pady=40)

    if ventanaInfoGeneral:
        ventanaOFC.withdraw()
    
    ventanaInfoGeneral.mainloop()

def ventanaMostrarInfo():

    global ventanaMostrarInfo
    ventanaMostrarInfo = Toplevel(ventanaAP)
    ventanaMostrarInfo.title("Información de Autómata")

    screen_width = ventanaMostrarInfo.winfo_screenwidth()
    screen_height = ventanaMostrarInfo.winfo_screenheight()

    ventanaMostrarInfo_width = 800
    ventanaMostrarInfo_height = 500

    x = (screen_width - ventanaMostrarInfo_width) // 2
    y = (screen_height - ventanaMostrarInfo_height) // 2

    ventanaMostrarInfo.geometry(f"{ventanaMostrarInfo_width}x{ventanaMostrarInfo_height}+{x}+{y}")
    ventanaMostrarInfo.configure(bg="#37474f")

    table2 = ttk.Treeview(ventanaMostrarInfo)
    table2.pack(padx=10, pady=10)
    table2['columns'] = ('ap_nombre', 'ap_alfabeto', 'ap_simbolo', 'ap_estado', 'ap_eInicial', 'ap_eAceptacion', 'ap_transicion')

    table2.column('#0', width=0, stretch=NO)
    table2.column('ap_nombre', anchor=CENTER, width=75)
    table2.column('ap_alfabeto', anchor=CENTER, width=75)
    table2.column('ap_simbolo', anchor=CENTER, width=75)
    table2.column('ap_estado', anchor=CENTER, width=75)
    table2.column('ap_eInicial', anchor=CENTER, width=50)
    table2.column('ap_eAceptacion', anchor=CENTER, width=75)
    table2.column('ap_transicion', anchor=CENTER, width=400)

    table2.heading('#0', text='', anchor=CENTER)
    table2.heading('ap_nombre', text='Nombre', anchor=CENTER)
    table2.heading('ap_alfabeto', text='Alfabeto', anchor=CENTER)
    table2.heading('ap_simbolo', text='Simbolo', anchor=CENTER)
    table2.heading('ap_estado', text='Estados', anchor=CENTER)
    table2.heading('ap_eInicial', text='Inicial', anchor=CENTER)
    table2.heading('ap_eAceptacion', text='Aceptación', anchor=CENTER)
    table2.heading('ap_transicion', text='Transiciones', anchor=CENTER)

    cont2 = 0
    for ap in ap_array:
        table2.insert("", "end", iid=cont2, text='',
        values=(ap.nombre, ap.alfabeto, ap.simbolo, ap.estado, ap.eInicial, ap.eAceptacion, ap.transicion))
        cont2 += 1

    Button(ventanaMostrarInfo, text="Regresar", height="2", width="30", command = regresarAP).pack(padx=10, pady=40)

    if ventanaMostrarInfo:
        ventanaAP.withdraw()
    
    ventanaMostrarInfo.mainloop()

def volverMenuPrincipal1():
    ventanaPrincipal.iconify()
    ventanaPrincipal.deiconify()
    ventanaOFC.withdraw()

def volverMenuPrincipal2():
    ventanaPrincipal.iconify()
    ventanaPrincipal.deiconify()
    ventanaAP.withdraw()

def regresarOFC():
    ventanaOFC.iconify()
    ventanaOFC.deiconify()
    ventanaInfoGeneral.withdraw()

def regresarAP():
    ventanaAP.iconify()
    ventanaAP.deiconify()
    ventanaMostrarInfo.withdraw()

def salir():
    salida = messagebox.askokcancel(title = "Salir", message = "Desea salir del programa?")
    if salida == True:
        countdown(5)

def countdown(num_of_secs):
    while num_of_secs:
        time.sleep(1)
        num_of_secs -= 1
        #print(num_of_secs)

    ventanaMain.destroy()
    ventanaPrincipal.destroy()

def upload_file(case, glc_array, ap_array):

    type_file = ''
    # Lectura del archivo
    if (case == 1):
        type_file = '.glc'
    elif (case == 2):
        type_file = '.ap'

    data = filereader.file_reader(type_file)
    if data is None:
        print("- Ningun archivo seleccionado \n")
    else:
        processor.data_processor(data, case, glc_array, ap_array)
        #if case == 1:
            #for i in glc_array:
                #print(" Nombre: " + str(i.nombre))
                #print(" No terminales: " + str(i.noTerminal))
                #print(" Terminales: " + str(i.terminal))
                #print(" Inicial: " + str(i.inicial))
                #print(" Producciones: " + str(i.produccion))
                #print()
            #Procesador de datos
        #elif case == 2:
            #for i in ap_array:
                #print(" Nombre: " + str(i.nombre))
                #print(" Alfabeto: " + str(i.alfabeto))
                #print(" Simbolo: " + str(i.simbolo))
                #print(" Estado: " + str(i.estado))
                #print(" Estado inicial: " + str(i.eInicial))
                #print(" Estado aceptacion: " + str(i.eAceptacion))
                #print(" Trancisiones: " + str(i.transicion))
                #print()
            #Procesador de datos

        if (data is None):
            messagebox.showinfo('Mensaje', 'Error al cargar la información.')
        else:
            messagebox.showinfo('Mensaje', 'Información cargada exitosamente.')


ventanaMain()