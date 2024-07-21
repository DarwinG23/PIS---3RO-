from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import os.path
from numbers import Number
import json
import os
from datetime import datetime
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
        cur = self.conn._db.cursor()
        tabla = "Persona"
        cur.execute(f"SELECT * FROM {tabla}")
        # Obtener los nombres de las columnas
        columns = [col[0].lower() for col in cur.description]
        rows = cur.fetchall()
        dict_rows = [dict(zip(columns, row)) for row in rows]
        for row in dict_rows:
            a = self.atype.deserializar(row)
            lista.addNode(a, lista._length)
        cur.close()
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

    

    def _save(self, data) -> T:
        tabla = "Persona"
        aux = data.serializable

        # Verificar que los campos obligatorios no estén vacíos
        if not aux["dni"]:
            raise ValueError("El campo 'dni' no puede estar vacío")
        if not aux["nombre"]:
            raise ValueError("El campo 'nombre' no puede estar vacío")
        if not aux["apellido"]:
            raise ValueError("El campo 'apellido' no puede estar vacío")
        if not aux["fechaNacimiento"]:
            raise ValueError("El campo 'fechaNacimiento' no puede estar vacío")
        if not aux["numTelefono"]:
            raise ValueError("El campo 'numTelefono' no puede estar vacío")
        if not aux["idCuenta"]:
            raise ValueError("El campo 'idCuenta' no puede estar vacío")

        # Excluir el campo 'roles' de la serialización
        columns = ""
        data_values = ""
        for key, value in aux.items():
            if key == "roles":
                continue  # Omitir el campo 'roles'
            if len(str(value)) > 0:
                columns += key + ","
                if key == "fechaNacimiento":
                    # Asegurarse de que la fecha esté en el formato correcto
                    value = datetime.strptime(value, "%d/%m/%Y").strftime("%Y-%m-%d")
                if isinstance(value, (int, float, bool)):
                    data_values += str(value) + ","
                else:
                    data_values += "'" + str(value).replace("'", "''") + "'" + ","

        columns = columns.rstrip(',')
        data_values = data_values.rstrip(',')

        sql = f"INSERT INTO {tabla} ({columns}) VALUES ({data_values})"
        cur = self.conn._db.cursor()
        print("LOG:" + sql)
        try:
            cur.execute(sql)
            self.conn._db.commit()
        except Exception as e:
            print("Error:", e)
            self.conn._db.rollback()
        finally:
            cur.close()


    
    def _merge(self, data: T, pos) -> T:
        tabla = "Persona"
        aux = data.serializable
        columns = ""
        for cont in aux:
            if len(str(aux[cont])) > 0:
                columns += cont + ","
        columns = columns.rstrip(columns[-1])
        data_values = ""
        for cont in aux:
            if len(str(aux[cont])) > 0:
                if isinstance(aux[cont], Number) or isinstance(aux[cont], bool):
                    data_values += str(aux[cont]) + "," 
                elif isinstance(aux[cont], list):
                    # Convertir la lista a cadena y asegurarse de usar comillas simples para valores de cadena
                    data_values += "'" + str(aux[cont]).replace("'", "''") + "'" + ","
                else:
                    # Usar comillas simples para valores de cadena
                    data_values += "'" + aux[cont].replace("'", "''") + "'" + ","
        data_values = data_values.rstrip(data_values[-1])
        sql = (f"UPDATE {tabla} SET "+columns+" = (" + data_values + ") WHERE id = {pos}")
        cur = self.conn._db.cursor()
        print("LOG:" + sql)
        cur.execute(sql)
        id = self.conn._db.commit()
        print(id)   
    #     data = self.lista.getData(pos)  #para obtener el id
    #     self._list()
    #     self.lista.edit(data, pos)
    #     a = open(self.URL+self.file, "w")
    #     a.write(self.__transform__())
    #     a.close()
     


        
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


     