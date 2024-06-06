class Asignacion:
    def __init__(self):
        self.__id = 0
        self.__numero_unidades = 0
        self.__cedula_docente = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def numero_unidades(self):
        return self.__numero_unidades

    @numero_unidades.setter
    def numero_unidades(self, value):
        self.__numero_unidades = value

    @property
    def cedula_docente(self):
        return self.__cedula_docente

    @cedula_docente.setter
    def cedula_docente(self, value):
        self.__cedula_docente = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "numero_unidades": self.__numero_unidades,
            "cedula_docente": self.__cedula_docente
        }


    def deserializar(data):
        asignacion = Asignacion()
        asignacion._id = data["id"]
        asignacion._numero_unidades = data["numero_unidades"]
        asignacion._cedula_docente = data["cedula_docente"]
        return asignacion
    
    def _str_(self) -> str:
        return f'{self.__id} {self.__numero_unidades} {self.__cedula_docente}'