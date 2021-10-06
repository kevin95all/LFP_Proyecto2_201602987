from tkinter import *
#  from tkinter import filedialog
from Automata import Automata


class Main:

    def __init__(self):
        self.ventana = Tk()
        self.automata = Automata()
        self.archivo_analizado = False
        self.ruta = ''

    def ventana_principal(self):
        self.ventana.title('4N4L!Z4DOR')
        self.centrar_ventana()
        self.ventana.resizable(False, False)
        self.componentes()
        self.ventana.mainloop()

    def centrar_ventana(self):
        w, h = 850, 600
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
        pass

    def editor(self):
        pass

    def consola(self):
        pass


app = Main()
app.ventana_principal()
