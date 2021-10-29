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
        cadena = ''
        mensaje = ''
        posicion = 0

        while posicion < len(self.lista_de_comandos):
            if self.lista_de_comandos[posicion] == 'Claves':  # -------------------------------> claves
                cadena = ''
            elif self.lista_de_comandos[posicion] == 'Registros':  # --------------------------> registros
                cadena = ''
            elif self.lista_de_comandos[posicion] == 'imprimir':  # ---------------------------> imprimir
                if cadena == '':
                    mensaje = mensaje + '\n\n'
                    cadena = cadena + f'{self.lista_de_parametros[posicion]}'
                    mensaje = mensaje + f'>>> {cadena}'
                else:
                    cadena = ''
                    cadena = cadena + f' {self.lista_de_parametros[posicion]}'
                    mensaje = mensaje + f'{cadena}'
            elif self.lista_de_comandos[posicion] == 'imprimirln':  # -------------------------> imprimirln
                cadena = ''
                mensaje = mensaje + '\n\n'
                mensaje = mensaje + f'>>> {self.lista_de_parametros[posicion]}'
            elif self.lista_de_comandos[posicion] == 'conteo':  # -----------------------------> conteo
                cadena = ''
                mensaje = mensaje + '\n\n'
                mensaje = mensaje + f'>>> {len(self.lista_de_registros)}'
            elif self.lista_de_comandos[posicion] == 'promedio':  # ---------------------------> promedio
                cadena = ''
                clave = self.lista_de_parametros[posicion]
                if clave in self.lista_de_claves:
                    p = self.lista_de_claves.index(clave)
                    suma = 0
                    n = 0

                    while n < len(self.lista_de_registros):
                        suma = suma + float(self.lista_de_registros[n][p])
                        n = n + 1

                    promedio = suma / len(self.lista_de_registros)
                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> {promedio}'
                else:
                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> Clave no declarada'
            elif self.lista_de_comandos[posicion] == 'contarsi':  # ---------------------------> contarsi
                cadena = ''
                parametro = self.lista_de_parametros[posicion]
                clave = parametro[0]
                valor = float(parametro[1])
                if clave in self.lista_de_claves:
                    p = self.lista_de_claves.index(clave)
                    contador = 0
                    n = 0

                    while n < len(self.lista_de_registros):
                        if float(self.lista_de_registros[n][p]) == valor:
                            contador = contador + 1
                        n = n + 1

                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> {contador}'
                else:
                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> Clave no declarada'
            elif self.lista_de_comandos[posicion] == 'max':  # --------------------------------> max
                cadena = ''
                clave = self.lista_de_parametros[posicion]
                if clave in self.lista_de_claves:
                    p = self.lista_de_claves.index(clave)
                    maximo = float(self.lista_de_registros[0][p])
                    n = 0

                    while n < len(self.lista_de_registros):
                        if float(self.lista_de_registros[n][p]) > maximo:
                            maximo = float(self.lista_de_registros[n][p])
                        n = n + 1

                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> {maximo}'
                else:
                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> Clave no declarada'
            elif self.lista_de_comandos[posicion] == 'min':  # --------------------------------> min
                cadena = ''
                clave = self.lista_de_parametros[posicion]
                if clave in self.lista_de_claves:
                    p = self.lista_de_claves.index(clave)
                    minimo = float(self.lista_de_registros[0][p])
                    n = 0

                    while n < len(self.lista_de_registros):
                        if float(self.lista_de_registros[n][p]) < minimo:
                            minimo = float(self.lista_de_registros[n][p])
                        n = n + 1

                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> {minimo}'
                else:
                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> Clave no declarada'
            elif self.lista_de_comandos[posicion] == 'sumar':  # ------------------------------> sumar
                cadena = ''
                clave = self.lista_de_parametros[posicion]
                if clave in self.lista_de_claves:
                    p = self.lista_de_claves.index(clave)
                    suma = 0
                    n = 0

                    while n < len(self.lista_de_registros):
                        suma = suma + float(self.lista_de_registros[n][p])
                        n = n + 1

                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> {suma}'
                else:
                    mensaje = mensaje + '\n\n'
                    mensaje = mensaje + f'>>> Clave no declarada'
            elif self.lista_de_comandos[posicion] == 'datos':  # ------------------------------> datos
                cadena = ''
                n = 0
                f = 0

                while n < len(self.lista_de_claves):
                    if cadena == '':
                        mensaje = mensaje + '\n\n'
                        cadena = cadena + f'{self.lista_de_claves[n]}'
                        mensaje = mensaje + f'>>> {cadena}'
                    else:
                        cadena = ''
                        cadena = cadena + f'  |  {self.lista_de_claves[n]}'
                        mensaje = mensaje + f'{cadena}'
                    n = n + 1

                while f < len(self.lista_de_registros):
                    cadena = self.lista_de_registros[f]
                    mensaje = mensaje + '\n'
                    mensaje = mensaje + f'>>> {cadena}'
                    f = f + 1
            elif self.lista_de_comandos[posicion] == 'exportarReporte':  # --------------------> Exportar
                cadena = ''

            posicion = posicion + 1

        return mensaje
