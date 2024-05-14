class ListadoRespuestas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.respuestas = []

    def consultar_usuario(self):
        return self.usuario

    def consultar_respuestas(self):
        return self.respuestas
