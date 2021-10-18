from Reportes import Reporte


class Automata:

    def __init__(self):
        self.reporte = Reporte()
        self.contenido = ''
        self.caracter = ''
        self.comando = ''
        self.parametro = ''
        self.cadena = ''
        self.numero = 0
        self.estado = 0
        self.lista_registros = []
        self.registro = []
        self.claves = []
        self.lista_comandos = []
        self.lista_parametros = []
        self.parametros = []
        self.lista_tokens = []
        self.r_tokens = []
        self.r_errores = []

    def letra(self, caracter):  # -----> Método para saber si el carácter es una letra
        L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if caracter.lower() in L:
            return True
        else:
            return False

    def digito(self, caracter):  # -----> Método para saber si el carácter es un digito
        D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if caracter in D:
            return True
        else:
            return False

    def reservada(self, id):  # -----> Método para saber si la cadena es una palabra reservada
        R = ['Claves', 'Registros', 'imprimir', 'imprimirln', 'conteo', 'promedio', 'contarsi',
             'datos', 'max', 'min', 'exportarReporte']
        if id in R:
            return True
        else:
            return False

    def leer_archivo(self, contenido):
        self.contenido = contenido

        posicion = 0
        f = 1
        c = 1
        while posicion < len(self.contenido):
            self.caracter = self.contenido[posicion]

            if self.estado == 0:  # -----------------------------------> Estado 0
                if self.letra(self.caracter):
                    self.estado = 1
                    self.comando = self.comando + self.caracter
                    self.r_tokens.append(f'Cadena encontrada en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == '#':
                    self.estado = 26
                    c = c + 1
                elif self.caracter == "'":
                    self.estado = 29
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                    c = 1
                else:
                    self.estado = 0
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 1:  # -----------------------------------> Estado 1
                if self.letra(self.caracter):
                    self.estado = 1
                    self.comando = self.comando + self.caracter
                    c = c + 1
                elif self.caracter == '=':
                    if self.reservada(self.comando):
                        self.estado = 2
                        self.lista_tokens.append(self.comando)
                        self.lista_comandos.append(self.comando)
                        self.lista_parametros.append('None')
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.comando = ''
                        c = c + 1
                    else:
                        self.estado = 36
                        c = c + 1
                elif self.caracter == '(':
                    if self.reservada(self.comando):
                        self.estado = 15
                        self.lista_tokens.append(self.comando)
                        self.lista_comandos.append(self.comando)
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.comando = ''
                        c = c + 1
                    else:
                        self.estado = 36
                        c = c + 1
                elif self.caracter == ' ':
                    self.estado = 1
                    c = c + 1
                else:
                    self.estado = 1
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 2:  # -----------------------------------> Estado 2
                if self.caracter == '[':
                    self.estado = 3
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 2
                    c = c + 1
                else:
                    self.estado = 2
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 3:  # -----------------------------------> Estado 3
                if self.caracter == '"':
                    self.estado = 4
                elif self.caracter == '{':
                    self.estado = 7
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 3
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 3
                    c = c + 4
                else:
                    self.estado = 3
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 4:  # -----------------------------------> Estado 4
                if self.caracter != '"':
                    self.estado = 5
                    self.cadena = self.cadena + self.caracter
                elif self.caracter == '"':
                    pass

            posicion = posicion + 1

    def resultados(self):
        resultado = self.contenido
        return resultado

    def generar_reportes(self):
        pass
