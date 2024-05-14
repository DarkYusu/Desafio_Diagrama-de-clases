from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def consultar_correo(self):
        return self.correo

    def modificar_correo(self, nuevo_correo):
        self.correo = nuevo_correo

    def consultar_edad(self):
        return self.edad

    def modificar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def consultar_region(self):
        return self.region

    def modificar_region(self, nueva_region):
        self.region = nueva_region

    def contestar_encuesta(self, encuesta):
        listado_respuestas = ListadoRespuestas(self)
        encuesta.agregar_listado_de_respuestas(listado_respuestas)
