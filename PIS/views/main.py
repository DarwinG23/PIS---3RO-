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

# [
#     {
#         "id": 1,
#         "numero_unidades": 2,
#         "cedula_docente": "1106006123",
#         "id_materia": 1,
#         "id_cursa": 1,
#         "unidades": [
#             {
#                 "id": 1,
#                 "codigo": "3412",
#                 "estado": true,
#                 "fecha_inicio": "2021-06-01",
#                 "fecha_limite": "2021-06-30",
#                 "asignacion": 1,
#                 "nombre": "Listas-Pilas-Colas"
#             },
#             {
#                 "id": 2,
#                 "codigo": "1551",
#                 "estado": true,
#                 "fecha_inicio": "2021-06-01",
#                 "fecha_limite": "2021-06-30",
#                 "asignacion": 1,
#                 "nombre": "Metodos de Ordenacion y Busqueda"
#             }
#         ],
#         "reportes": [
#             {
#                 "id": 1,
#                 "cedulaEstudiante": "1104526322",
#                 "nota": 7.22,
#                 "asistencia": 0.85,
#                 "codigoUnidad": "3412",
#                 "codigoMateria": "123",
#                 "numMatricula": 1
#             },
#             {
#                 "id": 2,
#                 "cedulaEstudiante": "1104526322",
#                 "nota": 8.23,
#                 "asistencia": 0.85,
#                 "codigoUnidad": "1551",
#                 "codigoMateria": "123",
#                 "numMatricula": 1
#             }
#         ]
#     },
   #  {
   #      "id": 2,
   #      "numero_unidades": 2,
   #      "cedula_docente": "1106006123",
   #      "id_materia": 2,
   #      "id_cursa": 1,
   #      "unidades": [
   #          {
   #              "id": 1,
   #              "codigo": "2022",
   #              "estado": true,
   #              "fecha_inicio": "2021-06-01",
   #              "fecha_limite": "2021-06-30",
   #              "asignacion": 1,
   #              "nombre": "Modelo Relacional"
   #          },
   #          {
   #              "id": 2,
   #              "codigo": "1010",
   #              "estado": true,
   #              "fecha_inicio": "2021-06-01",
   #              "fecha_limite": "2021-06-30",
   #              "asignacion": 1,
   #              "nombre": "Normalizacion"
   #          }
   #      ],
   #      "reportes":[]
   #  }
# ]


try:
   # pc._persona._apellido = "Poma"
   # pc._persona._nombre = "Jorge"
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
   
   lista = pc._list("PERSONA")
   print("^^^^^^^^^^^^^^^^^^^^^^^^^")
   
   persona = lista.binary_search_models("0", "_id")
   print("ROLES DE LA PERSONA")
   persona._roles.print
   print(lista._length)
   #lista.sort_models("_nombre", 1)
   #lista.print   
   # connection = Connection()
   # connection.connect("USUARIO_DBA", "1104753890", "XE")


except Exception as error:
   print(error)