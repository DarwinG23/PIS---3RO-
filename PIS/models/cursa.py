class Cursa:
    def __init__(self):
        self.__id = 0
        self.__paralelo = ''
        self.__cedula_docente = ''


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value

    @property
    def _cedula_docente(self):
        return self.__cedula_docente

    @_cedula_docente.setter
    def _cedula_docente(self, value):
        self.__cedula_docente = value

   
    @property
    def serializable(self):
        return{
            "id": self.__id,
            "paralelo": self.__paralelo,
            "cedula_docente": self.__cedula_docente
        }
    
    @classmethod
    def deserializar(data):
        cursa = Cursa()
        cursa._id = data["id"]
        cursa._paralelo = data["paralelo"]
        cursa._cedula_docente = data["cedula_docente"]
        return cursa
    def __str__(self) -> str:
        return f"Paralelo: {self.__paralelo}, Docente: {self.__cedula_docente}"
    
        