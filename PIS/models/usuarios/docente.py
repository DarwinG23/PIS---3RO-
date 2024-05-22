class Docente:
    def __init__(self):
        self.__id = 0
        self.__titulo = ""
        self.__cubiculo = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _titulo(self):
        return self.__titulo

    @_titulo.setter
    def _titulo(self, value):
        self.__titulo = value

    @property
    def _cubiculo(self):
        return self.__cubiculo

    @_cubiculo.setter
    def _cubiculo(self, value):
        self.__cubiculo = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "cubiculo": self.__cubiculo
        }
    
    def deserializar(data):
        docente = Docente()
        docente._id = data["id"]
        docente._titulo = data["titulo"]
        docente._cubiculo = data["cubiculo"]
        return docente
    
    def __str__(self) -> str:
        return f'{self.__id} - {self.__titulo} - {self.__cubiculo}'



