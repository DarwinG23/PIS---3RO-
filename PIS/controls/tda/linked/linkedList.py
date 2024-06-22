from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException
#from controls.tdaArray import TDAArray
from numbers import Number
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.insercion import Insercion

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
    

    @property
    def _atype(self):
        return self.__atype

    @_atype.setter
    def _atype(self, value):
        self.__atype = value


    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value
 
        
    @property    
    def isEmpty(self):
        return self.__head == None or self._length == 0
    
    def _getFirst_(self, poss):
        if not self.isEmpty:
            return self.__head
        else:
            return "List is Empty"
    
    def _getLast_(self, poss):
        if not self.isEmpty:
            return self.__last
        else:
            return "List is Empty"
        
    def getData(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head._data
        elif poss == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node._data
        

    def getNode(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head
        elif poss == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node
            
        
    
    def addFirst(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            headOld = self.__head #guarada toda la lista hara ahora
            node = Node(data, headOld)  
            self.__head = node
            self.__length += 1

    def addLast(self, data):
        if self.isEmpty:
            self.addFirst(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    
    def addNode(self, data, poss = 0):
       
        if poss == 0:
            self.addFirst(data)
        elif poss == self.__length:
            self.addLast(data)
        else:
            node_preview = self.getNode(poss - 1)
            node_actuality = node_preview._next
            node = Node(data, node_actuality)
            node_preview._next = node
            self.__length += 1


    def edit (self, data, poss = 0):
        if poss == 0:
            print("entro en 0 en edit")
            print(data)
            self.__head._data = data
        elif poss == (self.__length - 1):
            self.__last._data = data
        else:
            node = self.getNode(poss)
            node._data = data


    @property
    def toArray (self):
        array = []
        node = self.__head
        while node != None:
            array.append(node._data)
            node = node._next
        return array
    
    def toList(self, array):
        for i in array:
            self.addLast(i)


    def dicToListLast(self, array_dict):
        for i in range(0, len(array_dict)):
            #data = Atencion().deserializar(array_dict[i])                
            #self.addLast(data)
            pass #QUITAR CUANDO SE DESCOMENTE EL CODIGO DE ARRIBA

    def dicToListFirst(self, array_dict):
        for i in range(0, len(array_dict)):
            # a = Atencion().deserializar(array_dict[i])           
            # self.addFirst(a)
            pass #QUITAR CUANDO SE DESCOMENTE EL CODIGO DE ARRIBA
            
    
    def delete(self, poss = 0 ):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            node = self.__head._next
            del self.__head
            self.__head = node
            self.__length -= 1
        elif poss == (self.__length - 1):
            print("entro en el ultimo")
            node = self.getNode(self.__length - 2)
            node._next = None
            del self.__last
            self.__last = node
            self.__length -= 1
            print(self.__length)
        else:
            node_previous = self.getNode(poss-1)
            node_next = node_previous._next._next
            node_previous._next = node_next
            self.__length -= 1
        
        

    #serializable
    @property
    def serializable(self):
        array = self.toArray 
        array_dict = []
        for i in range(0, len(array)): 
            array_dict.append(array[i].serializable) 
        return array_dict
    

    @classmethod
    def deserializar(self, array_dict):
        linked = Linked_List()
        linked.dicToListLast(array_dict)
        return linked
    
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def __str__(self) -> str: #metodo toString    #cometar ctrl+k+c   / ctrl+k+u
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " -> "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None :
            data += str(node._data) + "   "
            node = node._next
        print("Lista de datos")
        print(data)
        
    
              
    def sort(self, type = 1):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            self.clear
            #datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                #order = Burbuja()
                order = Insercion()
                if type == 1:
                    #array = order.sort_burbuja_number_ascent(array)
                    array = order.sort_primitive_ascent(array)
                else:
                    #array = order.sort_burbuja_number_descent(array)
                    array = order.sort_primitive_descent(array)
          
            self.toList(array)
            
    def  sort_models(self, atribute ,type = 1 ):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            self.clear
            if isinstance(array[0], object): 
                #order = Burbuja()
                order = Insercion()
                if type == 1:                  
                    #array = order.sort_burbuja_atribute_ascent(array, atribute)
                    array = order.sort_models_ascent(array, atribute)
                else:
                    #array = order.sort_burbuja_atribute_descent(array, atribute)
                    array = order.sort_models_descent(array, atribute)
            self.toList(array)
        return self
      
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:  
            array = self.toArray
            for i in range(0, len(array)):
                if array[i].lower().__contains__(data.lower()):  # < > <= >= !=  == startswith() endswith()
                    list.addNode(array[i], list._length)
        return list  
    
    def binary_search(self, data):
        self.sort(1)
        self.print
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == data:
                return arr[mid] 
            elif arr[mid] < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1 
    
    # def sort_models_ascent(self, array, atribute):
        
    #     for i in range(1, len(array)):
    #         j =  i -1 
    #         t = array[i]
    #         while j>=0 and getattr(t, atribute) < getattr(array[j], atribute):
    #             array[j+1] = array[j]
    #             j = j - 1
    #         array[j+1] = t
    #     return array
    
    def binary_search_models(self, data, atribute):
        self.sort_models(atribute)
        arr = self.toArray
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if getattr(arr[mid], atribute) == data:
                return arr[mid] 
            elif getattr(arr[mid], atribute) < data:
                left = mid + 1
            else:
                right = mid - 1
        return -1   
   
    