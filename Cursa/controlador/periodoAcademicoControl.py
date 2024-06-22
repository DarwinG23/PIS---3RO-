from controls.dao.daoAdapter import DaoAdapter
from models.seguimiento.periodoAcademico import PeriodoAcademico

class PeriodoControl(DaoAdapter):
    def __init__(self):
        super().__init__(PeriodoAcademico)
        self.__periodo_academico = None

    @property
    def periodo_academico(self):
        if self.__periodo_academico is None:
            self.__periodo_academico = PeriodoAcademico()
        return self.__periodo_academico

    @periodo_academico.setter
    def periodo_academico(self, value):
        self.__periodo_academico = value

    def lista(self):
        return self._list()

    def save(self):
        self._save(self.periodo_academico)

    def merge(self, pos):
        self._merge(self.periodo_academico, pos)
