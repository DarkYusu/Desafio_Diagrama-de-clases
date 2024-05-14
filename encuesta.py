class Encuesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []
        self.listados_de_respuestas = []

    def consultar_nombre(self):
        return self.nombre

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def mostrar_encuesta(self):
        resultado = f"Nombre de la encuesta: {self.nombre}"
        for pregunta in self.preguntas:
            resultado += f"\nPregunta: {pregunta.mostrar_pregunta()}"
        return resultado

    def agregar_listado_de_respuestas(self, nuevo_listado):
        self.listados_de_respuestas.append(nuevo_listado)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def modificar_edad_minima(self, nueva_edad_minima):
        self.edad_minima = nueva_edad_minima

    def modificar_edad_maxima(self, nueva_edad_maxima):
        self.edad_maxima = nueva_edad_maxima

    def agregar_listado_de_respuestas(self, nuevo_listado):
        if self.edad_minima <= nuevo_listado.usuario.edad <= self.edad_maxima:
            super().agregar_listado_de_respuestas(nuevo_listado)

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones):
        super().__init__(nombre)
        self.regiones = regiones

    def modificar_regiones(self, nuevas_regiones):
        self.regiones = nuevas_regiones

    def agregar_listado_de_respuestas(self, nuevo_listado):
        if nuevo_listado.usuario.region in self.regiones:
            super().agregar_listado_de_respuestas(nuevo_listado)
