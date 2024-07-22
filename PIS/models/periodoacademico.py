from controls.tda.linked.linkedList import Linked_List
from models.cursa import Cursa  

class PeriodoAcademico:
    def __init__(self):
        self.__id = 0
        self.__fecha_inicio = " "
        self.__fecha_fin = " "
        self.__cursas = Linked_List()

    @property
    def _cursas(self):
        return self.__cursas

    @_cursas.setter
    def _cursas(self, value):
        self.__cursas = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha_inicio(self):
        return self.__fecha_inicio

    @_fecha_inicio.setter
    def _fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def _fecha_fin(self):
        return self.__fecha_fin

    @_fecha_fin.setter
    def _fecha_fin(self, value):
        self.__fecha_fin = value
        
    @property
    def serializable(self):
        return{
            "id": self.__id,
            "fecha_inicio": self.__fecha_inicio,
            "fecha_fin": self.__fecha_fin,
            "cursas": self.__cursas.serializable
        }
    @classmethod
    def deserializar(self, data):
        periodo_academico = PeriodoAcademico()
        periodo_academico._id = data["id"]
        periodo_academico._fecha_inicio = data["fecha_inicio"]
        periodo_academico._fecha_fin = data["fecha_fin"]
        clase = Cursa()
        periodo_academico._cursas = Linked_List().deserializar(data["cursas"], clase)
        return periodo_academico
    
    def __str__(self) -> str:
        return  f"Fecha de inicio: {self.__fecha_inicio}, Fecha de fin: {self.__fecha_fin}"
        
