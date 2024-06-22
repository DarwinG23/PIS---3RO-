class Rol:
    def __init__(self):
        self.__id = 0
        self.__nombre = ""
        self.__descripcion = ""
        self.__estado = False


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _description(self, value):
        self.__descripcion= value

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "descripcion": self.__descripcion,
            "estado": self.__estado
        }
    

    @classmethod
    def deserializar(cls, dic):
        rol = Rol()
        rol._id = dic["id"]
        rol._nombre = dic["nombre"]
        rol._descripcion = dic["descripcion"]
        rol._estado = dic["estado"]
        return rol
    
    def __str__(self):
        return f"{self.__nombre} - {self.__descripcion}"

    
