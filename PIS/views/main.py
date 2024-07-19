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
from controls.seguimiento.reporteControl import ReporteControl
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
rec = ReporteControl()

# [
#     {
#         "id": 1,
#         "cedulaEstudiante": "1104526322",
#         "nota": 7.22,
#         "asistencia": 100,
#         "codigoUnidad": "3412",
#         "codigoMateria": "123",
#         "numMatricula": 1,
#         "idAsignacion": 1
#     },
#     {
#         "id": 2,
#         "cedulaEstudiante": "1104526322",
#         "nota": 8.23,
#         "asistencia": 95,
#         "codigoUnidad": "1551",
#         "codigoMateria": "123",
#         "numMatricula": 1,
#         "idAsignacion": 1
#     },
try:
  rec._reporte._cedulaEstudiante = "1106006123"
  rec._reporte._nota = 7.22
  rec._reporte._asistencia = 100
  rec._reporte._codigoUnidad = "3412"
  rec._reporte._codigoMateria = "442"
  rec._reporte._numMatricula = 1
  rec._reporte._idAsignacion = 1
  rec.save
   
   
 
   
   
   
except Exception as error:
   print(error)