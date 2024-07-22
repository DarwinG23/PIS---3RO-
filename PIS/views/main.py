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
   # mac._materia._nombre = "Base de Datos"
   # mac._materia._codigo = "2464"
   # mac._materia._horas = 275
   # mac.save
   
   ac._asignacion._numero_unidades = 3
   ac._asignacion._cedula_docente = "1106006123"
   ac._asignacion._id_materia = 1
   ac.save
   
   # pc._persona._apellido = "Granda"
   # pc._persona._nombre = "Darwin"
   # pc._persona._dni = "1106006123"
   # pc._persona._fechaNacimiento = "15/11/1994"
   # pc._persona._numTelefono = "0979411882"
   # #pc._persona._idCuenta = 2
   # pc.save

   # cc._cuenta._correo = "darwin.granda@unl.edu.ec"
   # cc._cuenta._contrasenia = "1234"
   # cc._cuenta._idPersona = pc._list()._length
   # cc._cuenta._estado = 1
   # cc.save
   # cc._cuenta = None
   # pc._persona = None
   
   # rc._rol._nombre = "Docente"
   # rc._rol._descripcion = "Rol de docente"
   # rc._rol._estado = 1
   # rc._rol._idPersona = pc._list()._length
   # rc.save
   
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
   # pc._persona._apellido = "Torres"
   # pc._persona._nombre = "Alejandro"
   # pc._persona._dni = "1104526352"
   # pc._persona._fechaNacimiento = "10/04/1994"
   # pc._persona._numTelefono = "0987654321"
   # pc._persona._idCuenta = 2
   # pc._merge(pc._persona, 1)
   #lista.sort_models("_nombre", 1)
   #lista.print   
   # connection = Connection()
   # connection.connect("USUARIO_DBA", "1104753890", "XE")


except Exception as error:
   print(error)