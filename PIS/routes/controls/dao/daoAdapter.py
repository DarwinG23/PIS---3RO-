from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import os.path

import json
import os
from controls.connection.connection import Connection

T = TypeVar('T')
class DaoAdapter(Generic[T]):
    atype: T

    def __init__(self, atype: T):
        self.atype = atype
        conexion = Connection()
        self.conn = conexion.connect("USUARIO_DBA", "1104753890", "XE")
      
        
        #self.lista = Linked_List()
        #self.file = atype.__name__.lower()+".json"
        #self.URL = os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) + "/data/"

    def _list(self) -> T:
        lista = Linked_List()
        print("LISTAR")
        cur = self.conn._db.cursor()
        print(type(cur))
        tabla = "Persona"
        cur.execute(f"SELECT * FROM {tabla}")
        for row in cur.fetchall():
            print(row)
        return lista

    # def __transform__(self):
    #     aux = "["
    #     for i in range(0, self.lista._length):
    #         if i < self.lista._length - 1:
    #             aux += str(json.dumps(self.lista.getData(i).serializable)) + ","
    #         else:
    #             aux += str(json.dumps(self.lista.getData(i).serializable))
    #     aux += "]"

    #     return aux
    
    # def to_dic_lista(self, lista):
    #     aux = []
    #     arreglo = lista.toArray
    #     for i in range(0, lista._length):
    #         aux.append(arreglo[i].serializable)
    #     return aux
        
        
    # def _get(self, id):
    #     list = self._list()
    #     array = list.toArray
    #     for i in range(0, len(array)):
    #         if array[i]._id == id:
    #             return array[i]
    #     return None
    
    # def to_dic(self):
    #     aux = []
    #     self._list()
    #     for i in range(0, self.lista._length):
    #         aux.append(self.lista.getNode(i).serializable)

    #     return aux
    
    # def _save_json(self, data):
    #     name = self.atype.__name__
    #     with open("../files/"+ name + ".json", "w") as outfile:
    #         json.dump(data, outfile, indent=4)

    # def read_json(self):
    #     if os.path.exists("../files/persona.json"): #si existe el archivo
    #         with open("../files/persona.json") as file: #abrir archivo
    #             data = json.load(file)
    #             self.lista = None
    #             return self.lista.dicToList(data)
    #     else:
    #        return self.__lista

    

    # def _save(self, data) -> T:
    #     self._list()
    #     self.lista.addNode(data, self.lista._length) 
    #     data._id = self.lista._length
    #     a = open(self.URL+self.file, "w")
    #     a.write(self.__transform__())
    #     a.close()

    # def _delete(self, pos) -> T:
    #     self._list()
    #     self.lista.delete(pos)
    #     self.lista.print
    #     a = open(self.URL+self.file, "w")
    #     a.write(self.__transform__())
    #     a.close()


    # def _merge(self, data: T, pos) -> T:
    #     data = self.lista.getData(pos)  #para obtener el id
    #     self._list()
    #     self.lista.edit(data, pos)
    #     a = open(self.URL+self.file, "w")
    #     a.write(self.__transform__())
    #     a.close()
     