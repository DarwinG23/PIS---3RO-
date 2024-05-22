import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.usuarios.docenteDaoControl import DocenteControl

from controls.usuarios.estudianteDaoControl import EstudianteControl


dc = DocenteControl()
ec = EstudianteControl()

try:
   dc._docente._titulo = 'Magister'
   dc._docente._cubiculo = 'A-1'
   dc._docente._idiomas = 'Ingles'
   dc._docente._tipoContrato = 'Tiempo Completo'
   dc.save

   dc._docente._titulo = 'Doctor'
   dc._docente._cubiculo = 'B-1'
   dc._docente._idiomas = 'Frances'
   dc._docente._tipoContrato = 'Medio Tiempo'
   dc.save

   ec._estudiante._nota = '10'
   ec._estudiante._asistencia = '100%'
   ec._estudiante._colegioProcedencia = 'Daniel Alvarez Burneo'
   ec.save

   ec._estudiante._nota = '9'
   ec._estudiante._asistencia = '90%'
   ec._estudiante._colegioProcedencia = 'San Jose'
   ec.save
   
except Exception as error:
   print(error)


