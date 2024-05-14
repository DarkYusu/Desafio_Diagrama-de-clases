class Pregunta:
    def __init__(self, enunciado, ayuda=None, es_requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas if alternativas else []

    def consultar_enunciado(self):
        return self.enunciado

    def modificar_enunciado(self, nuevo_enunciado):
        self.enunciado = nuevo_enunciado

    def consultar_ayuda(self):
        return self.ayuda

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda

    def consultar_es_requerida(self):
        return self.es_requerida

    def modificar_es_requerida(self, es_requerida):
        self.es_requerida = es_requerida

    def consultar_alternativas(self):
        return self.alternativas

    def mostrar_pregunta(self):
        resultado = f"Enunciado: {self.enunciado}"
        if self.ayuda:
            resultado += f", Ayuda: {self.ayuda}"
        resultado += f", Requerida: {self.es_requerida}"
        for alt in self.alternativas:
            resultado += f"\nAlternativa: {alt.mostrar_alternativa()}"
        return resultado
