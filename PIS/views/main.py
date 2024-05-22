import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.seguimiento.asignacionControl import AsignacionControl
from controls.seguimiento.unidadControl import UnidadControl 

#dc = DocenteControl()
#ec = EstudianteControl()
ac = AsignacionControl()
uc = UnidadControl()
try:
   ac._asignacion._numero_unidades= 0
   ac._asignacion._cedula_docente= '1104527284'
   ac.save
   uc._unidad._nota= 0.0
   uc._unidad._estado= false
   uc._unidad._fecha_inicio='02/05/2001'
   uc._unidad.__fecha_limite='02/05/2001' 
   uc.save 
#    dc._docente._nombre = 'Juan'
#    dc._docente._titulo = 'Magister'
#    dc._docente._cubiculo = 'A-1'
#    dc._docente._idiomas = 'Ingles'
#    dc._docente._tipoContrato = 'Tiempo Completo'
#    dc.save

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