class Docente:
    def __init__(self):
        self.__titulo = ""
        self.__cubiculo = ""
        self.__idiomas = ""
        self.__tipoContrato = ""

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
    def _idiomas(self):
        return self.__idiomas

    @_idiomas.setter
    def _idiomas(self, value):
        self.__idiomas = value

    @property
    def _tipoContrato(self):
        return self.__tipoContrato

    @_tipoContrato.setter
    def _tipoContrato(self, value):
        self.__tipoContrato = value

    @property
    def serializable(self):
        return {
            "titulo": self.__titulo,
            "cubiculo": self.__cubiculo,
            "idiomas": self.__idiomas,
            "tipoContrato": self.__tipoContrato
        }
    
    def deserializar(data):
        docente = Docente()
        docente._titulo = data["titulo"]
        docente._cubiculo = data["cubiculo"]
        docente._idiomas = data["idiomas"]
        docente._tipoContrato = data["tipoContrato"]
        return docente
    
    def __str__(self) -> str:
        return f'{self.__titulo} {self.__cubiculo} {self.__idiomas} {self.__tipoContrato}'



