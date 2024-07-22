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
        self.conn = conexion.connect("USUARIO_DBA", "2001", "XE")
      
      
    def _list(self) -> T:
        tabla = self.atype.__name__.lower()
        print(tabla)
        lista = Linked_List()
        cur = self.conn._db.cursor()
        cur.execute(f"SELECT * FROM {tabla}")
        # Obtener los nombres de las columnas
        columns = [col[0].lower() for col in cur.description]
        rows = cur.fetchall()
        dict_rows = [dict(zip(columns, row)) for row in rows]
        print(dict_rows)
        for row in dict_rows:
            a = self.atype.deserializar(row)
            print(row)
            lista.addNode(a, lista._length)
        cur.close()
        return lista


    def _save(self, data) -> T:
        tabla = self.atype.__name__.lower()
        aux = data.serializable
        columns = ""
        data_values = ""
        for key, value in aux.items():
            if key == "roles" or key == "id":  # Omitir el campo 'roles'
                continue  # Omitir el campo 'roles'
            if len(str(value)) > 0:
                columns += key + ","
                if "fecha" in key:
                    # Asegurarse de que la fecha esté en el formato correcto
                    print(aux["fechaNacimiento"])
                    value = datetime.strptime(value, "%d/%m/%Y").strftime("%d-%b-%Y").upper()
                    print(value)
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
            print("Se ha guardado el registro")
        except Exception as e:
            print("Error al hacer comit:", e)
            self.conn._db.rollback()
        finally:
            cur.close()
            print("Se ha cerrado la conexión")
    
    
    def _merge(self, data: T, pos) -> T:
        tabla = self.atype.__name__.lower()
        aux = data.serializable
        update_pairs = []  # Usar una lista para almacenar pares de columna=valor

        for key, value in aux.items():
            if key == "roles"  or key == "id":  # Omitir el campo 'roles'
                continue  # Omitir el campo 'roles'
            if len(str(value)) > 0:
                if "fecha" in key:
                    # Asegurarse de que la fecha esté en el formato correcto
                    print(aux["fechaNacimiento"])
                    value = datetime.strptime(value, "%d/%m/%Y").strftime("%d-%b-%Y").upper()
                    print(value)
                if isinstance(value, (int, float, bool)):
                    update_pairs.append(f"{key} = {value}")
                else:
                    value = str(value).replace("'", "''")  # Escapar comillas simples
                    update_pairs.append(f"{key} = '{value}'")
        
        update_str = ", ".join(update_pairs)  # Construir la cadena de actualización correctamente

        sql = f"UPDATE {tabla} SET {update_str} WHERE id = {pos}"
        cur = self.conn._db.cursor()
        print("LOG:" + sql)
        cur.execute(sql)
        self.conn._db.commit()
