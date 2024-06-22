from controls.dao.daoAdapter import DaoAdapter
from models.seguimiento.cursa import Cursa

class CursaControl(DaoAdapter):
    def __init__(self):
        super().__init__(Cursa)
        self.__cursa = None

    @property
    def cursa(self):
        if self.__cursa is None:
            self.__cursa = Cursa()
        return self.__cursa

    @cursa.setter
    def cursa(self, value):
        self.__cursa = value

    def lista(self):
        return self._list()

    def save(self):
        self._save(self.cursa)

    def merge(self, pos):
        self._merge(self.cursa, pos)
