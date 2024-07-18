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


try:
  cursas = cuc._list()
  pac._periodo_academico._fecha_inicio = "2023-10-23"
  pac._periodo_academico._fecha_fin = "2024-3-30"
  pac._periodo_academico._cursas = cursas
  
  pac.save
   
   
 
   
   
   
except Exception as error:
   print(error)