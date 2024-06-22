from controls.tda.linked.linkedList import Linked_List
from models.cursa import Cursa

class Estudiante:
    def __init__(self):
        self.__nota = ""
        self.__asistencia = ""
        self.__colegioProcedencia = ""
        self.__cursas = Linked_List()

    @property
    def _cursas(self):
        return self.__cursas

    @_cursas.setter
    def _cursas(self, value):
        self.__cursas = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value

    @property
    def _asistencia(self):
        return self.__asistencia

    @_asistencia.setter
    def _asistencia(self, value):
        self.__asistencia = value

    @property
    def _colegioProcedencia(self):
        return self.__colegioProcedencia

    @_colegioProcedencia.setter
    def _colegioProcedencia(self, value):
        self.__colegioProcedencia = value
    
    @property
    def serializable(self):
        return {
            "nota": self.__nota,
            "asistencia": self.__asistencia,
            "colegioProcedencia": self.__colegioProcedencia,
            "cursas": self.__cursas.serializable
        }
    
    def deserializar(data):
        estudiante = Estudiante()
        estudiante._nota = data["nota"]
        estudiante._asistencia = data["asistencia"]
        estudiante._colegioProcedencia = data["colegioProcedencia"]
        clase = Cursa()
        estudiante._cursas = Linked_List().deserializar(data["cursas"], clase)
        return estudiante
    
    def __str__(self) -> str:
        return f'{self.__nota} {self.__asistencia} {self.__colegioProcedencia}'



