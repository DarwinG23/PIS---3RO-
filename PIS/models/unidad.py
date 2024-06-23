class Unidad:
    def __init__(self):
        self.__id = 0
        self.__nota = ' '
        self.__estado = False
        self.__fecha_inicio = ''
        self.__fecha_limite = ''
        self.__asignacion = 0
        self.__nombre = ''

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value


    @property
    def _asignacion(self):
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def _fecha_inicio(self):
        return self.__fecha_inicio

    @_fecha_inicio.setter
    def _fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def _fecha_limite(self):
        return self.__fecha_limite

    @_fecha_limite.setter
    def _fecha_limite(self, value):
        self.__fecha_limite = value


    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "nota": self.__nota,
            "estado": self.__estado,
            "fecha_inicio": self.__fecha_inicio,
            "fecha_limite": self.__fecha_limite,
            "asignacion": self.__asignacion,
            "nombre": self.__nombre
        }
        
    @classmethod
    def deserializar(self, data):
        unidad = Unidad()
        unidad._id = data["id"]
        unidad._nota = data["nota"]
        unidad._estado = data["estado"]
        unidad._fecha_inicio = data["fecha_inicio"]
        unidad._fecha_limite = data["fecha_limite"]
        unidad._asignacion = data["asignacion"]
        unidad._nombre = data["nombre"]
        return unidad
    
    def _str_(self) -> str:
        return self.__nombre