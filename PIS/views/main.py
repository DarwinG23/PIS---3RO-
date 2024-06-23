import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.usuarios.docenteDaoControl import DocenteControl

from controls.usuarios.estudianteDaoControl import EstudianteControl
from controls.login.cuentaDaoControl import CuentaDaoControl

from controls.administrativo.cursaControl import CursaControl


dc = DocenteControl()
ec = EstudianteControl()

ca= CursaControl()

cc = CuentaDaoControl()

try:
   # listaInt = Linked_List()
   
   # for i in range(0, 10):
   #    listaInt.addNode(i)
      
   # listaInt.print

   # print(listaInt.binary_search(22))
   
   # cc._list().print
   
   # print(cc._list().binary_search_models("darwin.sarango@unl.edu.ec", "_correo"))
   
   
   # cc._cuenta._correo = "darwin.sarango@unl.edu.ec"
   # cc._cuenta._contrasenia = "0987"
   # cc._cuenta._estado = True
   # cc.save
   # cc._cuenta = None
   
   
   # dc._docente._titulo = 'Magister'
   # dc._docente._cubiculo = 'A-1'
   # dc._docente._idiomas = 'Ingles'
   # dc._docente._tipoContrato = 'Tiempo Completo'
   # dc.save

   # dc._docente._titulo = 'Doctor'
   # dc._docente._cubiculo = 'B-1'
   # dc._docente._idiomas = 'Frances'
   # dc._docente._tipoContrato = 'Medio Tiempo'
   # dc.save

   # dc._docente._titulo = 'Ingeniero'
   # dc._docente._cubiculo = 'C-1'
   # dc._docente._idiomas = 'Aleman'
   # dc._docente._tipoContrato = 'Por horas'
   # dc.save

   # ec._estudiante._nota = '10'
   # ec._estudiante._asistencia = '100%'
   # ec._estudiante._colegioProcedencia = 'Daniel Alvarez Burneo'
   # ec.save

   # ec._estudiante._nota = '9'
   # ec._estudiante._asistencia = '90%'
   # ec._estudiante._colegioProcedencia = 'San Jose'
   # ec.save

   # ec._estudiante._nota = '8'
   # ec._estudiante._asistencia = '80%'
   # ec._estudiante._colegioProcedencia = 'Bernardo Valdiviezo'
   # ec.save

   # ca._cursa._paralelo = 'b'
   # ca.save
   # lista = Linked_List()
   # lista.addNode(ca)

   # ec._estudiante._nota = '9'
   # ec._estudiante._asistencia = '96%'
   # ec._estudiante._colegioProcedencia = 'Daniel Alvarez Burneo'
   # ec._estudiante._cursas = lista
   # ec.save

   
   

   


   
except Exception as error:
   print(error)


