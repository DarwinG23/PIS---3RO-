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

try:
   
   listaPersonas = pc._list()
   
   persona = listaPersonas.binary_search_models(2, "_id")
   
   
   listaCursas = cuc._list()
   ec._estudiante._id = persona._id
   ec._estudiante._dni = persona._dni
   ec._estudiante._nombre = persona._nombre
   ec._estudiante._apellido = persona._apellido
   ec._estudiante._fechaNacimiento = persona._fechaNacimiento
   ec._estudiante._numTelefono = persona._numTelefono
   ec._estudiante._idCuenta = persona._idCuenta
   ec._estudiante._roles = persona._roles
   ec._estudiante._nota = 7.8
   ec._estudiante._colegioProcedencia = "Julio Isacc"
   ec._estudiante._asistencia = "94%"
   ec._estudiante._cursas = listaCursas
   ec.save
   
   
   
 
   
   
   
except Exception as error:
   print(error)