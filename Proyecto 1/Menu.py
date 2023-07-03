import tkinter as tk
from tkinter import ttk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class Menu(tk.Tk):

    def __init__(self,*args,**kwargs):       

        super().__init__(*args,**kwargs)                #Heredar el tk.Tk

        self.configure(bg = "#37474f")
        self.title("Proyecto 1 - Angel Arreaga - 202004762")
        self.geometry("600x300")
        self.columnconfigure( 0, weight = 1 )
        self.rowconfigure(0, weight = 1)

        ventanaPrincipal = tk.Frame(self, bg = "#37474f")#00228E
        ventanaPrincipal.place(x = 0, y = 0, width = 600, height = 300)

        self.todos_los_frames = dict()

        for F in (Principal, pestañaAFD, pestañaAFN, pestañaOE, pestañaCA, CrearAFN, EvaluarAFN, CrearAFD, EvaluarAFD):
            frame = F( ventanaPrincipal , self)
            self.todos_los_frames[F] = frame
            frame.place(x = 0, y = 0, width = 850, height = 500)

        self.show_frame( Principal ) 

    def show_frame(self, ventanaLlamada):

        frame = self.todos_los_frames[ventanaLlamada]
        frame.tkraise()


class Principal(tk.Frame):

    def __init__(self, container, controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        botonAFD = ttk.Button( self, text = "Metodo AFN", command = lambda:controller.show_frame(pestañaAFN))
        botonAFD.place(x = 50, y = 25, width = 200, height = 50)

        botonAFN = ttk.Button( self, text = "Metodo AFD", command = lambda:controller.show_frame(pestañaAFD))
        botonAFN.place(x = 350, y = 25, width = 200, height = 50)

        botonOE = ttk.Button( self, text = "Optmizar Estados", command = lambda:controller.show_frame(pestañaOE))
        botonOE.place(x = 50, y = 125, width = 200, height = 50)

        botonCA = ttk.Button( self, text = "Cargar Archivos", command = lambda:controller.show_frame(pestañaCA))
        botonCA.place(x = 350, y = 125, width = 200, height = 50)

        botonSalir = ttk.Button( self, text = "Salir", command=self.salir)
        botonSalir.place(x = 200, y = 225, width = 200, height = 50)

    def salir(self):
        self.quit()


class pestañaAFN(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        botonAFD = ttk.Button( self, text = "Crear AFN", command = lambda:controller.show_frame(CrearAFN))
        botonAFD.place(x = 50, y = 25, width = 200, height = 50)

        botonAFN = ttk.Button( self, text = "Evaluar Cadena", command = lambda:controller.show_frame(EvaluarAFN))
        botonAFN.place(x = 350, y = 25, width = 200, height = 50)

        botonOE = ttk.Button( self, text = "Generar Reporte AFN")
        botonOE.place(x = 50, y = 125, width = 200, height = 50)

        botonCA = ttk.Button( self, text = "Ayuda")
        botonCA.place(x = 350, y = 125, width = 200, height = 50)

        botonRegresar = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(Principal))
        botonRegresar.place(x = 200, y = 225, width = 200, height = 50)


class CrearAFN(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        nombreAFN = tk.Label(self, text = "Ingrese el nombre del AFN: ", bg = "#37474f", fg = "white")
        nombreAFN.place(x = 10, y = 0, width = 150, height = 50)
        self.cuadroNombreAFN = tk.Entry(self)
        self.cuadroNombreAFN.place(x = 10, y = 35, width = 200, height = 20)

        estadosAFN = tk.Label(self, text = "Ingrese los estados: ", bg = "#37474f", fg = "white")
        estadosAFN.place(x = 300, y = 0, width = 150, height = 50)
        self.cuadroEstadosAFN = tk.Entry(self)
        self.cuadroEstadosAFN.insert(0, "A;B;C;D")
        self.cuadroEstadosAFN.place(x = 320, y = 35, width = 200, height = 20)

        alfabetoAFN = tk.Label(self, text = "Ingrese el alfabeto: ", bg = "#37474f", fg = "white")
        alfabetoAFN.place(x = -10, y = 55, width = 150, height = 50)
        self.cuadroAlfabetoAFN = tk.Entry(self)
        self.cuadroAlfabetoAFN.place(x = 10, y = 90, width = 200, height = 20)

        estadoInicialAFN = tk.Label(self, text = "Ingrese el estado inicial: ", bg = "#37474f", fg = "white")
        estadoInicialAFN.place(x = 310, y = 55, width = 150, height = 50)
        self.cuadroEstadoInicialAFN = tk.Entry(self)
        self.cuadroEstadoInicialAFN.place(x = 320, y = 90, width = 200, height = 20)

        estadosAceptacionAFN = tk.Label(self, text = "Ingrese los estados de aceptacion: ", bg = "#37474f", fg = "white")
        estadosAceptacionAFN.place(x = 5, y = 110, width = 200, height = 50)
        self.cuadroEstadosAceptacionAFN = tk.Entry(self)
        self.cuadroEstadosAceptacionAFN.insert(0, "A;B;C;D")
        self.cuadroEstadosAceptacionAFN.place(x = 10, y = 145, width = 200, height = 20)

        transicionesAFN = tk.Label(self, text = "Ingrese las transiciones: ", bg = "#37474f", fg = "white")
        transicionesAFN.place(x = 310, y = 110, width = 150, height = 50)
        self.cuadroTransicionesAFN = tk.Entry(self)
        self.cuadroTransicionesAFN.insert(0, "A,a,B;A,b,C;B,a,D;")
        self.cuadroTransicionesAFN.place(x = 320, y = 145, width = 200, height = 20)

        botonIngresar = ttk.Button( self, text = "Ingresar", command = lambda:recibirDatosAFN(self))
        botonIngresar.place(x = 310, y = 225, width = 200, height = 50)

        botonRegresar = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pestañaAFN))
        botonRegresar.place(x = 10, y = 225, width = 200, height = 50)

        def recibirDatosAFN(self):

            self.DatosAFN = []

            datos = {
                "Nombre": self.cuadroNombreAFN.get(),
                "Estados": self.cuadroEstadosAFN.get(),
                "Alfabeto": self.cuadroAlfabetoAFN.get(),
                "Estado Inicial": self.cuadroEstadoInicialAFN.get(),
                "Estados de Aceptacion": self.cuadroEstadosAceptacionAFN.get(),
                "Transiciones": self.cuadroTransicionesAFN.get()
            }

            self.DatosAFN.append(datos)
            print(self.DatosAFN)


class EvaluarAFN(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")



        botonValidarAFN = ttk.Button( self, text = "Solo Validar")
        botonValidarAFN.place(x = 70, y = 100, width = 200, height = 50)

        botonRutaAFN = ttk.Button( self, text = "Ruta")
        botonRutaAFN.place(x = 340, y = 100, width = 200, height = 50)

        botonRegresarAFN = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pestañaAFN))
        botonRegresarAFN.place(x = 200, y = 225, width = 200, height = 50)


class pestañaAFD(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        botonAFD = ttk.Button( self, text = "Crear AFD", command = lambda:controller.show_frame(CrearAFD))
        botonAFD.place(x = 50, y = 25, width = 200, height = 50)

        botonAFN = ttk.Button( self, text = "Evaluar Cadena", command = lambda:controller.show_frame(EvaluarAFD))
        botonAFN.place(x = 350, y = 25, width = 200, height = 50)

        botonOE = ttk.Button( self, text = "Generar Reporte AFD")
        botonOE.place(x = 50, y = 125, width = 200, height = 50)

        botonCA = ttk.Button( self, text = "Ayuda")
        botonCA.place(x = 350, y = 125, width = 200, height = 50)

        botonRegresar = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(Principal))
        botonRegresar.place(x = 200, y = 225, width = 200, height = 50)


class CrearAFD(tk.Frame):
        
    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        nombreAFD= tk.Label(self, text = "Ingrese el nombre del AFD: ", bg = "#37474f", fg = "white")
        nombreAFD.place(x = 10, y = 0, width = 150, height = 50)
        cuadroNombreAFD = tk.Entry(self)
        cuadroNombreAFD.place(x = 10, y = 35, width = 200, height = 20)

        estadosAFD = tk.Label(self, text = "Ingrese los estados: ", bg = "#37474f", fg = "white")
        estadosAFD.place(x = 300, y = 0, width = 150, height = 50)
        cuadroEstadosAFD = tk.Entry(self)
        cuadroEstadosAFD.insert(0, "A;B;C;D")
        cuadroEstadosAFD.place(x = 320, y = 35, width = 200, height = 20)

        alfabetoAFD = tk.Label(self, text = "Ingrese el alfabeto: ", bg = "#37474f", fg = "white")
        alfabetoAFD.place(x = -10, y = 55, width = 150, height = 50)
        cuadroAlfabetoAFD = tk.Entry(self)
        cuadroAlfabetoAFD.place(x = 10, y = 90, width = 200, height = 20)

        estadoInicialAFD = tk.Label(self, text = "Ingrese el estado inicial: ", bg = "#37474f", fg = "white")
        estadoInicialAFD.place(x = 310, y = 55, width = 150, height = 50)
        cuadroEstadoInicialAFD = tk.Entry(self)
        cuadroEstadoInicialAFD.place(x = 320, y = 90, width = 200, height = 20)

        estadosAceptacionAFD = tk.Label(self, text = "Ingrese los estados de aceptacion: ", bg = "#37474f", fg = "white")
        estadosAceptacionAFD.place(x = 5, y = 110, width = 200, height = 50)
        cuadroEstadosAceptacionAFD = tk.Entry(self)
        cuadroEstadosAceptacionAFD.insert(0, "A;B;C;D")
        cuadroEstadosAceptacionAFD.place(x = 10, y = 145, width = 200, height = 20)

        transicionesAFD = tk.Label(self, text = "Ingrese las transiciones: ", bg = "#37474f", fg = "white")
        transicionesAFD.place(x = 310, y = 110, width = 150, height = 50)
        cuadroTransicionesAFD = tk.Entry(self)
        cuadroTransicionesAFD.insert(0, "A,a,B;A,b,C;B,a,D;")
        cuadroTransicionesAFD.place(x = 320, y = 145, width = 200, height = 20)

        botonIngresar = ttk.Button( self, text = "Ingresar")
        botonIngresar.place(x = 310, y = 225, width = 200, height = 50)

        botonRegresar = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pestañaAFD))
        botonRegresar.place(x = 10, y = 225, width = 200, height = 50)

        def recibirDatosAFD(self):

                DatosAFD = []

                datos = {
                    "Nombre": cuadroNombreAFD.get(),
                    "Estados": cuadroEstadosAFD.get(),
                    "Alfabeto": cuadroAlfabetoAFD.get(),
                    "Estado Inicial": cuadroEstadoInicialAFD.get(),
                    "Estados de Aceptacion": cuadroEstadosAceptacionAFD.get(),
                    "Transiciones": cuadroTransicionesAFD.get()
                }

                DatosAFD.append(datos)
                print(DatosAFD)


class EvaluarAFD(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")



        botonValidarAFD = ttk.Button( self, text = "Solo Validar")
        botonValidarAFD.place(x = 70, y = 100, width = 200, height = 50)

        botonRutaAFD = ttk.Button( self, text = "Ruta")
        botonRutaAFD.place(x = 340, y = 100, width = 200, height = 50)

        botonRegresarAFD = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pestañaAFD))
        botonRegresarAFD.place(x = 200, y = 225, width = 200, height = 50)


class pestañaOE(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        botonAFD = ttk.Button( self, text = "Seleccinar AFD")
        botonAFD.place(x = 50, y = 25, width = 200, height = 50)

        botonOE = ttk.Button( self, text = "Generar Reporte OE")
        botonOE.place(x = 50, y = 125, width = 200, height = 50)

        botonCA = ttk.Button( self, text = "Ayuda")
        botonCA.place(x = 350, y = 25, width = 200, height = 50)

        botonRegresar = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(Principal))
        botonRegresar.place(x = 200, y = 225, width = 200, height = 50)


class pestañaCA(tk.Frame):

    def __init__(self, container,controller,*args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg = "#37474f")

        botonAFD = ttk.Button( self, text = "Cargar AFD")
        botonAFD.place(x = 50, y = 25, width = 200, height = 50)

        botonAFN = ttk.Button( self, text = "Cargar AFN")
        botonAFN.place(x = 350, y = 25, width = 200, height = 50)

        botonRegresar = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(Principal))
        botonRegresar.place(x = 200, y = 225, width = 200, height = 50)







#Se crea APP como tal (aprovechandonos de la clase creada)
root = Menu()

#Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas
root.mainloop()