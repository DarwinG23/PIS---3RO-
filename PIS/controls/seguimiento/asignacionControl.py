from controls.dao.daoAdapter import DaoAdapter
from models.seguimiento.asignacion import Asignacion

class AsignacionControl(DaoAdapter):
    def _init_(self):
        super()._init_(Asignacion)
        self.__asignacion = None

    @property
    def _asignacion(self):
        if self.__asignacion is None:
            self.__asignacion = Asignacion()
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value

    def _lista(self):
        return self._list()

    @property
    def save(self):

        self._save(self._asignacion)

    def merge(self, pos):
        self._merge(self._asignacion, pos)