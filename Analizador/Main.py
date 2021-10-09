from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Text
from Automata import Automata


class Main:

    def __init__(self):
        self.ventana = Tk()
        self.automata = Automata()
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
        self.barra()
        self.editor()
        self.consola()

    def barra(self):
        menu = Menu(self.ventana)  # -----> Creando la barra de opciones

        cargar = Menu(menu)  # -----> Creando las opciones para la barra
        analizar = Menu(menu)
        reportes = Menu(menu)

        cargar.add_command(label='1. Cargar archivo', command=self.cargar_archivo)  # -----> Creando las acciones
        analizar.add_command(label='1. Analizar archivo', command=self.analizar_archivo)
        reportes.add_command(label='1. Reporte de errores', command=self.reportes_errores)
        reportes.add_command(label='2. Reportes de tokens', command=self.reportes_tokens)
        reportes.add_command(label='3. Grafica de árbol', command=self.grafica_arbol)

        menu.add_cascade(label='Cargar', menu=cargar)  # -----> Agregando las opciones a la barra
        menu.add_cascade(label='Analizar', menu=analizar)
        menu.add_cascade(label='Reportes', menu=reportes)

        self.ventana.config(menu=menu)  # -----> Agregando la barra de opciones al contenedor

    def editor(self):
        self.area_texto.configure(width=70, height=30)
        self.area_texto.place(x=25, y=80)

    def consola(self):
        self.area_consola.configure(bg='black', fg='white', width=40, height=30)
        self.area_consola.place(x=605, y=80)

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
            self.area_consola.delete(1.0, END)
            self.area_consola.insert(1.0, self.automata.resultados())
            self.archivo_analizado = True
            messagebox.showinfo('Información', 'Archivo analizado con exito')

    def reportes_errores(self):
        pass

    def reportes_tokens(self):
        pass

    def grafica_arbol(self):
        pass


app = Main()
app.ventana_principal()
