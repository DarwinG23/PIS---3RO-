class Cursa:
    def __init__(self):
        self.__id = 0
        self.__paralelo = ''
        self.__cedula_docente = ''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def paralelo(self):
        return self.__paralelo

    @paralelo.setter
    def paralelo(self, value):
        self.__paralelo = value

    @property
    def cedula_docente(self):
        return self.__cedula_docente

    @cedula_docente.setter
    def cedula_docente(self, value):
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
        cursa.id = data["id"]
        cursa.paralelo = data["paralelo"]
        cursa.cedula_docente = data["cedula_docente"]
        return cursa
    def __str__(self) -> str:
        return f"Paralelo: {self.__paralelo}, Docente: {self.__cedula_docente}"
    
        