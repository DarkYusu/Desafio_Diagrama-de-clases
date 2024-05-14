class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda
    
    def consultar_contenido(self):
        return self.contenido

    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido

    def consultar_ayuda(self):
        return self.ayuda

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda

    def mostrar_alternativa(self):
        if self.ayuda:
            return f"Contenido: {self.contenido}, Ayuda: {self.ayuda}"
        else:
            return f"Contenido: {self.contenido}"
