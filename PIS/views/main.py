import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.usuarios.docenteDaoControl import DocenteControl
from controls.usuarios.estudianteDaoControl import EstudianteControl
from controls.login.cuentaDaoControl import CuentaDaoControl
from controls.academico.mallaCurricularControl import MallaCurricularControl
from controls.academico.cicloControl import CicloControl
from controls.login.personaDaoControl import PersonaDaoControl
from controls.login.rolDaoControl import RolDaoControl
from controls.seguimiento.asignacionControl import AsignacionDaoControl
from controls.academico.materiaControl import MateriaControl
from controls.seguimiento.unidadControl import UnidadControl
from controls.administrativo.cursaControl import CursaControl
from controls.administrativo.periodoAcademicoControl import PeriodoAcademicoControl
from models.persona import Persona

dc = DocenteControl()
ec = EstudianteControl()
cc = CuentaDaoControl()
mc = MallaCurricularControl()
cic = CicloControl()
pc = PersonaDaoControl()  # Instanciar correctamente
rc = RolDaoControl()
mac = MateriaControl()
ac = AsignacionDaoControl()
uc = UnidadControl()
pac = PeriodoAcademicoControl()
cuc = CursaControl()

# [
#     {
#         "titulo": "Magister",
#         "cubiculo": "A-1",
#         "idiomas": "Ingles",
#         "tipoContrato": "Tiempo Completo"
#     },
#     {
#         "titulo": "Doctor",
#         "cubiculo": "B-1",
#         "idiomas": "Frances",
#         "tipoContrato": "Medio Tiempo"
#     },
#     {
#         "titulo": "Ingeniero",
#         "cubiculo": "C-1",
#         "idiomas": "Aleman",
#         "tipoContrato": "Por horas"
#     }
# ]

try:
   
   listaPersonas = pc._list()
   
   persona = listaPersonas.binary_search_models(1, "_id")
   
   
   dc._docente._dni = "1104754521"
   dc._docente._nombre = "Mario"
   dc._docente._apellido = "Zambrano"
   dc._docente._fechaNacimiento = "1999-12-12"
   dc._docente._numTelefono = "0987655772"
   dc._docente._idCuenta = " "
   dc._docente._roles = persona._roles
   
   dc._docente._titulo = "Ingeniero"
   dc._docente._cubiculo = "C-1"
   dc._docente._idiomas = "Espaniol"
   dc._docente._tipoContrato = "Por horas"
   dc.save
   
   
 
   
   
   
except Exception as error:
   print(error)