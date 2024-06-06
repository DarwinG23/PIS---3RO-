class PeriodoAcademico:
    def __init__(self):
        self.__id = 0
        self.__fecha_inicio = None
        self.__fecha_fin = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_fin(self):
        return self.__fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, value):
        self.__fecha_fin = value
        
    @property
    def serializable(self):
        return{
            "id": self.__id,
            "fecha_inicio": str(self.__fecha_inicio),
            "fecha_fin": str(self.__fecha_fin)
        }
    @classmethod
    def deserializar(data):
        periodo_academico = PeriodoAcademico()
        periodo_academico.id = data["id"]
        periodo_academico.fecha_inicio = data["fecha_inicio"]
        periodo_academico.fecha_fin = data["fecha_fin"]
        return periodo_academico
    
    def __str__(self) -> str:
        return  f"Fecha de inicio: {self.__fecha_inicio}, Fecha de fin: {self.__fecha_fin}"
        
