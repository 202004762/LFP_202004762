import tkinter as tk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4




def generarDOT():

    dot = Digraph('AFD', filename='AFDPRUEBA', format = 'png')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('B')
    dot.attr('node', shape='circle')
    dot.node('A')
    dot.edge('A', 'B', label='a')
    dot.render('AFDPRUEBA', view=False)

def mostrarDOT():

    webbrowser.open_new_tab('AFDPRUEBA.png')

def generarPDF():

    w, h = A4
    pdf = canvas.Canvas("Reporte.pdf", pagesize = A4)
    pdf.setTitle("Reporte")
    text = pdf.beginText(50, h - 50)
    text.setFont("Times-Roman", 12)
    text.textLine("AFD")
    text.textLine("Alfabeto: 1")
    text.textLine("Estados: A, B")
    text.textLine("Estado inicial: A")
    text.textLine("Estado de aceptacion: B")
    text.textLine("Transiciones: A,1;B")
    text.textLine("AFD graphviz")
    pdf.drawText(text)
    pdf.drawInlineImage("AFDPRUEBA.png", 100, 0, width = 200, height = 200, preserveAspectRatio = True)
    pdf.save()
    webbrowser.open_new_tab('Reporte.pdf')

def mostrarVentanaPrincipal():

    ventanaPrincipal.deiconify()
    ventanaSecundaria.withdraw()

def mostrarVentanaSecundaria():

    ventanaPrincipal.withdraw()
    ventanaSecundaria.deiconify()

ventanaPrincipal = tk.Tk()
ventanaSecundaria = tk.Toplevel(ventanaPrincipal)

ventanaPrincipal.title("Proyecto 1")
btnImprimir = tk.Button(ventanaPrincipal, text = "Imprimir grafo", command = mostrarDOT)
btnImprimir.pack()

btnMostrarDatos = tk.Button(ventanaPrincipal, text = "Mostrar datos", command = mostrarVentanaSecundaria)
btnMostrarDatos.pack()

btnGenerarPDF = tk.Button(ventanaPrincipal, text = "Generar PDF", command = generarPDF)
btnGenerarPDF.pack()

generarDOT()

ventanaSecundaria.title("Ventana secundaria")
btnRegresar = tk.Button(ventanaSecundaria, text = "Regresar", command = mostrarVentanaPrincipal)
btnRegresar.pack()

txtValores = tk.Text(ventanaSecundaria, width = 40, height = 10)
txtValores.pack()

txtValores.insert(tk.END, "Angel Arreaga\n202004762")
txtValores.configure(state = 'disabled')

ventanaSecundaria.withdraw()
ventanaPrincipal.mainloop()