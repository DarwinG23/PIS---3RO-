class cursa:
    def __init__(self):
        self.__id = 0
        self.__paralelo = 0
        self.__cedula_docente = ""

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
