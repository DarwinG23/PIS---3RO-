from controls.tda.linked.linkedList import Linked_List
from models.unidad import Unidad

class Asignacion:
    def __init__(self):
        self.__id = 0
        self.__numero_unidades = 0
        self.__cedula_docente = ""
        self.__id_materia = 0
        self.__id_cursa = 0
        self.__unidades = Linked_List()

    @property
    def _unidades(self):
        return self.__unidades

    @_unidades.setter
    def _unidades(self, value):
        self.__unidades = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _numero_unidades(self):
        return self.__numero_unidades

    @_numero_unidades.setter
    def _numero_unidades(self, value):
        self.__numero_unidades = value

    @property
    def _cedula_docente(self):
        return self.__cedula_docente

    @_cedula_docente.setter
    def _cedula_docente(self, value):
        self.__cedula_docente = value

    @property
    def _id_materia(self):
        return self.__id_materia

    @_id_materia.setter
    def _id_materia(self, value):
        self.__id_materia = value

    @property
    def _id_cursa(self):
        return self.__id_cursa

    @_id_cursa.setter
    def _id_cursa(self, value):
        self.__id_cursa = value


    @property
    def serializable(self):
        return {
            "id": self.__id,
            "numero_unidades": self.__numero_unidades,
            "cedula_docente": self.__cedula_docente,
            "id_materia": self.__id_materia,
            "id_cursa": self.__id_cursa,
            "unidades": self.__unidades.serializable  
        }

    @classmethod
    def deserializar(self, data):
        asignacion = Asignacion()
        asignacion._id = data["id"]
        asignacion._numero_unidades = data["numero_unidades"]
        asignacion._cedula_docente = data["cedula_docente"]
        asignacion._id_materia = data["id_materia"]
        asignacion._id_cursa = data["id_cursa"]
        clase = Unidad()
        asignacion._unidades = Linked_List().deserializar(data["unidades"], clase)
        return asignacion
    
    
    
    def __str__(self):
        return self._cedula_docente