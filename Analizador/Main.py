from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Text
from Automata import Automata
from Operaciones import Operaciones
import webbrowser
import os


class Main:

    def __init__(self):
        self.ventana = Tk()
        self.automata = Automata()
        self.operaciones = Operaciones()
        self.area_texto = Text(self.ventana)
        self.area_consola = Text(self.ventana)
        self.archivo_analizado = False
        self.ruta = ''
        self.contenido = ''

    def ventana_principal(self):
        self.ventana.title('4N4L!Z4DOR')
        self.centrar_ventana()
        self.ventana.resizable(False, False)
        self.componentes()
        self.ventana.mainloop()

    def centrar_ventana(self):
        w, h = 950, 600
        w_pantalla = self.ventana.winfo_screenwidth()
        h_pantalla = self.ventana.winfo_screenheight()
        x = ((w_pantalla / 2) - (w / 2))
        y = ((h_pantalla / 2) - (h / 2)) - 50
        self.ventana.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

    def componentes(self):
        self.botones()
        self.editor()
        self.consola()

    def botones(self):
        cargar = Button(self.ventana, text='Cargar', width=10, height=2, command=self.cargar_archivo)
        cargar.place(x=410, y=20)

        analizar = Button(self.ventana, text='Analizar', width=10, height=2, command=self.analizar_archivo)
        analizar.place(x=495, y=20)

        token = Button(self.ventana, text='Reporte de tokens', width=15, height=2, command=self.reporte_tokens)
        token.place(x=580, y=20)

        error = Button(self.ventana, text='Reporte de errores', width=15, height=2, command=self.reporte_errores)
        error.place(x=700, y=20)

        grafica = Button(self.ventana, text='Arbol de derivación', width=15, height=2, command=self.grafica)
        grafica.place(x=820, y=20)

    def editor(self):
        self.area_texto.configure(width=55, height=30)
        self.area_texto.place(x=25, y=80)

    def consola(self):
        self.area_consola.configure(bg='black', fg='white', width=55, height=30)
        self.area_consola.place(x=490, y=80)

    def cargar_archivo(self):  # -----> Método para la busqueda de archivos (lfp)
        respaldo_ruta = self.ruta
        respaldo_contenido = self.area_texto.get(1.0, 'end-1c')
        self.ruta = ''
        self.contenido = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos LFP', '*.lfp'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo_ruta
            self.contenido = respaldo_contenido
            messagebox.showinfo('Información', 'No se cargo ningun archivo')
        else:
            self.area_texto.delete(1.0, END)
            self.area_consola.delete(1.0, END)
            self.archivo_analizado = False
            with open(self.ruta, mode='r') as archivo:
                self.contenido = archivo.read()
            self.area_texto.insert(1.0, self.contenido)
            messagebox.showinfo('Información', 'Archivo cargado con exito')

    def analizar_archivo(self):  # -----> Método para empezar con el analisis del archivo
        contenido = self.area_texto.get(1.0, 'end-1c')
        if contenido == '':
            messagebox.showinfo('Información', 'No hay código lfp para analizar')
        else:
            self.automata.leer_archivo(contenido)
            self.automata.generar_reporte_tokens()
            self.automata.generar_reporte_errores()
            self.automata.analizar_datos()
            self.area_consola.delete(1.0, END)
            self.area_consola.insert(1.0, self.operaciones.resultados())
            self.archivo_analizado = True
            messagebox.showinfo('Información', 'Archivo analizado con exito')

    def reporte_errores(self):
        if self.archivo_analizado:
            chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            errores = 'file:///' + os.getcwd() + '/' + 'archivos_creados/errores.html'

            webbrowser.get(chromedir).open_new_tab(errores)
        else:
            messagebox.showinfo('Información', 'No se ha analizado el archivo')

    def reporte_tokens(self):
        if self.archivo_analizado:
            chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            tokens = 'file:///' + os.getcwd() + '/' + 'archivos_creados/tokens.html'

            webbrowser.get(chromedir).open_new_tab(tokens)
        else:
            messagebox.showinfo('Información', 'No se ha analizado el archivo')

    def grafica(self):
        if self.archivo_analizado:
            messagebox.showinfo('Información', 'Pendiente!!!!!')
        else:
            messagebox.showinfo('Información', 'No se ha analizado el archivo')


app = Main()
app.ventana_principal()
