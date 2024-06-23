from controls.tda.linked.linkedList import Linked_List
from models.rol import Rol
class Persona:
    def __init__(self):
        self.__id = 0
        self.__dni = ""
        self.__nombre = ""
        self.__apellido = ""
        self.__fechaNacimiento = ""
        self.__numTelefono = ""
        self.__idCuenta = 0
        self.__roles = Linked_List()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _fechaNacimiento(self):
        return self.__fechaNacimiento

    @_fechaNacimiento.setter
    def _fechaNacimiento(self, value):
        self.__fechaNacimiento = value

    @property
    def _numTelefono(self):
        return self.__numTelefono

    @_numTelefono.setter
    def _numTelefono(self, value):
        self.__numTelefono = value

    @property
    def _idCuenta(self):
        return self.__idCuenta

    @_idCuenta.setter
    def _idCuenta(self, value):
        self.__idCuenta = value

    @property
    def _roles(self):
        return self.__roles

    @_roles.setter
    def _roles(self, value):
        self.__roles = value


    @property
    def serializable(self):
        return {
            "id": self.__id,
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "fechaNacimiento": self.__fechaNacimiento,
            "numTelefono": self.__numTelefono,
            "idCuenta": self.__idCuenta,
            "roles": self.__roles.serializable
        }
    

    @classmethod
    def deserializar(self, data):
        persona = Persona()
        persona._id = data["id"]
        persona._dni = data["dni"]
        persona._nombre = data["nombre"]
        persona._apellido = data["apellido"]
        persona._fechaNacimiento = data["fechaNacimiento"]
        persona._numTelefono = data["numTelefono"]
        persona._idCuenta = data["idCuenta"]
        clase = Rol()
        persona._roles = Linked_List().deserializar(data["roles"], clase)
        return persona
    
    def __str__(self):
        return f"{self.__id} - {self.__nombre} {self.__apellido}"
