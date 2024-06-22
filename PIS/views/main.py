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
from models.persona import Persona

dc = DocenteControl()
ec = EstudianteControl()
cc = CuentaDaoControl()
mc = MallaCurricularControl()
cic = CicloControl()
pc = PersonaDaoControl()  # Instanciar correctamente
rc = RolDaoControl()

try:
   listaRoles = rc._list()

   # Crear y configurar una instancia de Persona
   persona = Persona()
   persona._dni = '1106006123'
   persona._nombre = 'Darwin'
   persona._apellido = 'Granda'
   persona._fechaNacimiento = '1997-05-25'
   persona._numTelefono = '0979411882'
   persona._idCuenta = 1
   persona._roles = listaRoles
   
   # Asignar la persona al controlador y guardar
   pc._persona = persona
   pc.save  # Acceder a la propiedad save

except Exception as error:
   print(error)