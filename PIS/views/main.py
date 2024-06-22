import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.usuarios.docenteDaoControl import DocenteControl

from controls.usuarios.estudianteDaoControl import EstudianteControl
from controls.login.cuentaDaoControl import CuentaDaoControl
from controls.academico.mallaCurricularControl import MallaCurricularControl
from controls.academico.cicloControl import CicloControl



dc = DocenteControl()
ec = EstudianteControl()
cc = CuentaDaoControl()
cic = CicloControl()
mcc = MallaCurricularControl()

try:
   
   cic._ciclo._descripcion = 'Ciclo 1'
   cic._ciclo._vigencia = True
   cic._ciclo._malla_curricular = 1
   cic.save
   
   
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

   # ec._estudiante._nota = '10'
   # ec._estudiante._asistencia = '100%'
   # ec._estudiante._colegioProcedencia = 'Daniel Alvarez Burneo'
   # ec.save

   # ec._estudiante._nota = '9'
   # ec._estudiante._asistencia = '90%'
   # ec._estudiante._colegioProcedencia = 'San Jose'
   # ec.save
   
except Exception as error:
   print(error)


