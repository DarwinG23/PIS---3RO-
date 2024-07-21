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
from controls.connection.connection import Connection

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
con = Connection()

try:
   # pc._persona._apellido = "Andrade"
   # pc._persona._nombre = "Manuel"
   # pc._persona._dni = "1104526352"
   # pc._persona._fechaNacimiento = "10/10/1994"
   # pc._persona._numTelefono = "0987654321"
   # pc._persona._idCuenta = 2
   # pc.save
   # # cc._cuenta._correo = "jorge.granda@unl.edu.ec"
   # cc._cuenta._contrasenia = "1234"
   # cc._cuenta._idPersona = pc._persona._id
   # cc._cuenta._estado = True
   # cc.save
   # cc._cuenta = None
   # pc._persona = None
   
   # lista = pc._list()
   # print("^^^^^^^^^^^^^^^^^^^^^^^^^")
   # lista.print
   # persona = lista.binary_search_models("2", "_id")
   # print("ROLES DE LA PERSONA")
   # persona._roles.print
   # print(lista._length)
   
   #ARREGLAR DESERIALIZAR CUENTA
   # listaCuenta = cc._list()
   # listaCuenta.print
   
   #EDITANDO PERSONA
   pc._persona._apellido = "Torres"
   pc._persona._nombre = "Alejandro"
   pc._persona._dni = "1104526352"
   pc._persona._fechaNacimiento = "10/04/1994"
   pc._persona._numTelefono = "0987654321"
   pc._persona._idCuenta = 2
   pc._merge(pc._persona, 1)
   #lista.sort_models("_nombre", 1)
   #lista.print   
   # connection = Connection()
   # connection.connect("USUARIO_DBA", "1104753890", "XE")


except Exception as error:
   print(error)