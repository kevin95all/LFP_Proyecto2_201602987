from Reportes import Reporte


class Automata:

    def __init__(self):
        self.reporte = Reporte()
        self.contenido = ''
        self.caracter = ''
        self.comando = ''
        self.cadena = ''
        self.numero = ''
        self.estado = 0
        self.claves = []
        self.lista_registros = []
        self.registro = []
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
                    self.estado = 23
                    c = c + 1
                elif self.caracter == "'":
                    self.estado = 24
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
                        self.estado = 30
                        self.r_errores.append(f'Comando "{self.comando}" no valido en la fila: {f} y columna: {c}')
                        self.comando = ''
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
                        self.estado = 30
                        self.r_errores.append(f'Comando "{self.comando}" no valido en la fila: {f} y columna: {c}')
                        self.comando = ''
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
                    c = c + 1
                elif self.caracter == '{':
                    self.estado = 7
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 3
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
                if self.caracter == '"':
                    self.estado = 6
                    self.lista_tokens.append('None')
                    self.claves.append('None')
                    c = c + 1
                else:
                    self.estado = 5
                    self.cadena = self.cadena + self.caracter
                    self.r_tokens.append(f'Cadena encontrada en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 5:  # -----------------------------------> Estado 5
                if self.caracter == '"':
                    self.estado = 6
                    self.lista_tokens.append(self.cadena)
                    self.claves.append(self.cadena)
                    self.cadena = ''
                    c = c + 1
                else:
                    self.estado = 5
                    self.cadena = self.cadena + self.caracter
                    c = c + 1
            elif self.estado == 6:  # -----------------------------------> Estado 6
                if self.caracter == ',':
                    self.estado = 3
                    c = c + 1
                elif self.caracter == ']':
                    self.estado = 0
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 6
                    f = f + 1
                    c = 1
                else:
                    self.estado = 6
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 7:  # -----------------------------------> Estado 7
                if self.caracter == '+' or self.caracter == '-':
                    self.estado = 8
                    self.numero = self.numero + self.caracter
                    self.r_tokens.append(f'Número encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.digito(self.caracter):
                    self.estado = 9
                    self.numero = self.numero + self.caracter
                    self.r_tokens.append(f'Número encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == '"':
                    self.estado = 12
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 7
                    c = c + 1
                else:
                    self.estado = 7
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 8:  # -----------------------------------> Estado 8
                if self.digito(self.caracter):
                    self.estado = 9
                    self.numero = self.numero + self.caracter
                    c = c + 1
                else:
                    self.estado = 8
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 9:  # -----------------------------------> Estado 9
                if self.digito(self.caracter):
                    self.estado = 9
                    self.numero = self.numero + self.caracter
                    c = c + 1
                elif self.caracter == '.':
                    self.estado = 10
                    self.numero = self.numero + self.caracter
                    c = c + 1
                elif self.caracter == ',':
                    self.estado = 7
                    self.lista_tokens.append(self.numero)
                    self.registro.append(self.numero)
                    self.numero = ''
                    c = c + 1
                elif self.caracter == '}':
                    self.registro.append(self.numero)
                    if len(self.registro) == len(self.claves):
                        self.estado = 11
                        self.lista_tokens.append(self.numero)
                        self.lista_registros.append(self.registro)
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.numero = ''
                        self.registro = []
                        c = c + 1
                    else:
                        self.estado = 11
                        self.lista_tokens.append(self.numero)
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.r_errores.append(f'Registro "{self.registro}" no valido')
                        self.numero = ''
                        self.registro = []
                        c = c + 1
                elif self.caracter == ')':
                    self.estado = 20
                    self.lista_tokens.append(self.numero)
                    self.parametros.append(self.numero)
                    self.lista_parametros.append(self.parametros)
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    self.numero = ''
                    self.parametros = []
                    c = c + 1
                else:
                    self.estado = 9
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 10:  # -----------------------------------> Estado 10
                if self.digito(self.caracter):
                    self.estado = 10
                    self.numero = self.numero + self.caracter
                    c = c + 1
                elif self.caracter == ',':
                    self.estado = 7
                    self.lista_tokens.append(self.numero)
                    self.registro.append(self.numero)
                    self.numero = ''
                    c = c + 1
                elif self.caracter == '}':
                    self.registro.append(self.numero)
                    if len(self.registro) == len(self.claves):
                        self.estado = 11
                        self.lista_tokens.append(self.numero)
                        self.lista_registros.append(self.registro)
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.numero = ''
                        self.registro = []
                        c = c + 1
                    else:
                        self.estado = 11
                        self.lista_tokens.append(self.numero)
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.r_errores.append(f'Registro "{self.registro}" no valido')
                        self.numero = ''
                        self.registro = []
                        c = c + 1
                elif self.caracter == ')':
                    self.estado = 20
                    self.lista_tokens.append(self.numero)
                    self.parametros.append(self.numero)
                    self.lista_parametros.append(self.parametros)
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    self.numero = ''
                    self.parametros = []
                    c = c + 1
                else:
                    self.estado = 9
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 11:  # -----------------------------------> Estado 11
                if self.caracter == '\n':
                    self.estado = 11
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 11
                    c = c + 4
                elif self.caracter == '{':
                    self.estado = 7
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == ']':
                    self.estado = 0
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                else:
                    self.estado = 11
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 12:  # -----------------------------------> Estado 12
                if self.caracter == '"':
                    self.estado = 14
                    self.lista_tokens.append('None')
                    self.registro.append('None')
                    c = c + 1
                else:
                    self.estado = 13
                    self.cadena = self.cadena + self.caracter
                    self.r_tokens.append(f'Cadena encontrada en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 13:  # -----------------------------------> Estado 13
                if self.caracter == '"':
                    self.estado = 14
                    self.lista_tokens.append(self.cadena)
                    self.registro.append(self.cadena)
                    self.cadena = ''
                    c = c + 1
                else:
                    self.estado = 13
                    self.cadena = self.cadena + self.caracter
                    c = c + 1
            elif self.estado == 14:  # -----------------------------------> Estado 14
                if self.caracter == ',':
                    self.estado = 7
                    c = c + 1
                elif self.caracter == '}':
                    if len(self.registro) == len(self.claves):
                        self.estado = 11
                        self.lista_registros.append(self.registro)
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.registro = []
                        c = c + 1
                    else:
                        self.estado = 11
                        self.lista_tokens.append(self.caracter)
                        self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                        self.r_errores.append(f'Registro "{self.registro}" no valido')
                        self.registro = []
                        c = c + 1
                else:
                    self.estado = 14
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 15:  # -----------------------------------> Estado 15
                if self.caracter == '"':
                    self.estado = 16
                    c = c + 1
                elif self.caracter == ')':
                    self.estado = 21
                    self.lista_tokens.append('None')
                    self.lista_parametros.append('None')
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                else:
                    self.estado = 15
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 16:  # -----------------------------------> Estado 16
                if self.caracter == '"':
                    self.estado = 18
                    self.lista_tokens.append('None')
                    self.lista_parametros.append('None')
                    c = c + 1
                else:
                    self.estado = 17
                    self.cadena = self.cadena + self.caracter
                    self.r_tokens.append(f'Cadena encontrada en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 17:  # -----------------------------------> Estado 17
                if self.caracter == '"':
                    self.estado = 18
                    c = c + 1
                else:
                    self.estado = 17
                    self.cadena = self.cadena + self.caracter
                    c = c + 1
            elif self.estado == 18:  # -----------------------------------> Estado 18
                if self.caracter == ',':
                    self.estado = 19
                    self.lista_tokens.append(self.cadena)
                    self.parametros.append(self.cadena)
                    self.cadena = ''
                    c = c + 1
                elif self.caracter == ')':
                    self.estado = 22
                    self.lista_tokens.append(self.cadena)
                    self.lista_parametros.append(self.cadena)
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    self.cadena = ''
                    c = c + 1
                else:
                    self.estado = 18
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 19:  # -----------------------------------> Estado 19
                if self.caracter == '+' or self.caracter == '-':
                    self.estado = 8
                    self.numero = self.numero + self.caracter
                    self.r_tokens.append(f'Número encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.digito(self.caracter):
                    self.estado = 9
                    self.numero = self.numero + self.caracter
                    self.r_tokens.append(f'Número encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 19
                    c = c + 1
                else:
                    self.estado = 19
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 20:  # -----------------------------------> Estado 20
                if self.caracter == ';':
                    self.estado = 0
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                else:
                    self.estado = 20
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 21:  # -----------------------------------> Estado 21
                if self.caracter == ';':
                    self.estado = 0
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                else:
                    self.estado = 21
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 22:  # -----------------------------------> Estado 22
                if self.caracter == ';':
                    self.estado = 0
                    self.lista_tokens.append(self.caracter)
                    self.r_tokens.append(f'Signo encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
                else:
                    self.estado = 22
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 23:  # -----------------------------------> Estado 23
                if self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 23
                    c = c + 4
                else:
                    self.estado = 23
                    c = c + 1
            elif self.estado == 24:  # -----------------------------------> Estado 24
                if self.caracter == "'":
                    self.estado = 25
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 24
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 24
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 24
                    c = c + 4
                else:
                    self.estado = 24
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 25:  # -----------------------------------> Estado 25
                if self.caracter == "'":
                    self.estado = 26
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 25
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 25
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 25
                    c = c + 4
                else:
                    self.estado = 25
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 26:  # -----------------------------------> Estado 26
                if self.caracter == "'":
                    self.estado = 27
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 26
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 26
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 26
                    c = c + 4
                else:
                    self.estado = 26
                    c = c + 1
            elif self.estado == 27:  # -----------------------------------> Estado 27
                if self.caracter == "'":
                    self.estado = 28
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 27
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 27
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 27
                    c = c + 4
                else:
                    self.estado = 27
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 28:  # -----------------------------------> Estado 28
                if self.caracter == "'":
                    self.estado = 29
                    c = c + 1
                elif self.caracter == ' ':
                    self.estado = 28
                    c = c + 1
                elif self.caracter == '\n':
                    self.estado = 28
                    f = f + 1
                    c = 1
                elif self.caracter == '\t':
                    self.estado = 28
                    c = c + 4
                else:
                    self.estado = 28
                    self.r_errores.append(f'Error lexico "{self.caracter}" encontrado en la fila: {f} y columna: {c}')
                    c = c + 1
            elif self.estado == 29:  # -----------------------------------> Estado 29
                if self.caracter == '\n':
                    self.estado = 0
                    f = f + 1
                    c = 1
                else:
                    self.estado = 29
                    c = c + 1
            elif self.estado == 30:  # -----------------------------------> Estado 30
                if self.caracter == ']':
                    self.estado = 0
                elif self.caracter == '\n':
                    self.estado = 30
                    f = f + 1
                    c = 1
                else:
                    self.estado = 30

            posicion = posicion + 1

    def resultados(self):
        resultado = self.lista_tokens
        return resultado

    def generar_reportes(self):
        pass
