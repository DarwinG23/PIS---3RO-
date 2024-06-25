from controls.tda.linked.linkedList import Linked_List
from models.cursa import Cursa
from models.persona import Persona
from models.rol import Rol

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
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
        data = super().serializable
        
        data.update({
            "nota": self.__nota,
            "asistencia": self.__asistencia,
            "colegioProcedencia": self.__colegioProcedencia,
            "cursas": self.__cursas.serializable
        })
        return data
    
    def deserializar(data):
        estudiante = Estudiante()
        estudiante._id = data["id"]
        estudiante._dni = data["dni"]
        estudiante._nombre = data["nombre"]
        estudiante._apellido = data["apellido"]
        estudiante._fechaNacimiento = data["fechaNacimiento"]
        estudiante._numTelefono = data["numTelefono"]
        estudiante._idCuenta = data["idCuenta"]
        clase = Rol()
        estudiante._roles = Linked_List().deserializar(data["roles"], clase)
        estudiante._nota = data["nota"]
        estudiante._asistencia = data["asistencia"]
        estudiante._colegioProcedencia = data["colegioProcedencia"]
        clase = Cursa()
        estudiante._cursas = Linked_List().deserializar(data["cursas"], clase)
        return estudiante
    
    
    def __str__(self) -> str:
        return str(super()._id) + " " + super()._nombre 



