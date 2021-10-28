class Reporte:

    def __init__(self):
        self.r_tokens = []
        self.r_errores = []

    def reporte_tokens(self, tokens):
        self.r_tokens = tokens

        with open('archivos_creados/tokens.html', mode='w') as HTML:  # -----> Crea un archivo.html en modo escritura
            HTML.write('<!DOCTYPE html>\n')
            HTML.write('<html>\n')
            HTML.write('    <head>\n')
            HTML.write('        <title>Reporte de Tokens</title>\n')
            HTML.write('        <meta charset="utf-8">\n')
            HTML.write('        <link rel="stylesheet" type="text/css" href="../archivos/estilo.css">\n')
            HTML.write('        <link rel="icon" href="../archivos/icono.png">\n')
            HTML.write('    </head>\n')
            HTML.write('    <body>\n')
            HTML.write('        <header>\n')
            HTML.write('            <center><h2>Reporte de Tokens</h2></center>\n')
            HTML.write('        </header>\n')
            HTML.write('        <br>\n')
            HTML.write('        <section>\n')
            HTML.write('            <br>\n')

            for i in self.r_tokens:
                token = i
                HTML.write('            <p style="text-align:center">' + token + '</p>\n')

            HTML.write('        </section>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <hr>\n')
            HTML.write('        <footer>LFP, Proyecto 2</footer>\n')
            HTML.write('    </body>\n')
            HTML.write('</html>')

    def reporte_errores(self, errores):
        self.r_errores = errores

        with open('archivos_creados/errores.html', mode='w') as HTML:  # -----> Crea un archivo.html en modo escritura
            HTML.write('<!DOCTYPE html>\n')
            HTML.write('<html>\n')
            HTML.write('    <head>\n')
            HTML.write('        <title>Reporte de Errores</title>\n')
            HTML.write('        <meta charset="utf-8">\n')
            HTML.write('        <link rel="stylesheet" type="text/css" href="../archivos/estilo.css">\n')
            HTML.write('        <link rel="icon" href="../archivos/icono.png">\n')
            HTML.write('    </head>\n')
            HTML.write('    <body>\n')
            HTML.write('        <header>\n')
            HTML.write('            <center><h2>Reporte de Errores</h2></center>\n')
            HTML.write('        </header>\n')
            HTML.write('        <br>\n')
            HTML.write('        <section>\n')
            HTML.write('            <br>\n')

            for i in self.r_errores:
                error = i
                HTML.write('            <p style="text-align:center">' + error + '</p>\n')

            HTML.write('        </section>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <br>\n')
            HTML.write('        <hr>\n')
            HTML.write('        <footer>LFP, Proyecto 2</footer>\n')
            HTML.write('    </body>\n')
            HTML.write('</html>')
