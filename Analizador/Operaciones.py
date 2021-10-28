class Operaciones:

    def __init__(self):
        self.lista_de_claves = []
        self.lista_de_registros = []
        self.lista_de_comandos = []
        self.lista_de_parametros = []

    def cargar_datos(self, claves, registros, comandos, parametros):
        self.lista_de_claves = claves
        self.lista_de_registros = registros
        self.lista_de_comandos = comandos
        self.lista_de_parametros = parametros

    def resultados(self):
        pass
