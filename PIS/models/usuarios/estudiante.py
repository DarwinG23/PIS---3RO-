class Estudiante:
    def __init__(self):
        self.__id = 0
        self.__colegioProcedencia = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _colegioProcedencia(self):
        return self.__colegioProcedencia

    @_colegioProcedencia.setter
    def _colegioProcedencia(self, value):
        self.__colegioProcedencia = value
    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "colegioProcedencia": self.__colegioProcedencia
        }
    
    def deserializar(data):
        estudiante = Estudiante()
        estudiante._id = data["id"]
        estudiante._colegioProcedencia = data["colegioProcedencia"]
        return estudiante
    
    def __str__(self) -> str:
        return f'{self.__id} - {self.__colegioProcedencia}'


