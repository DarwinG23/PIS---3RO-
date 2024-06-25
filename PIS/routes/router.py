from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response, url_for, flash, Flask
from flask_cors import CORS
from controls.login.cuentaDaoControl import CuentaDaoControl
from controls.administrativo.cursaControl import CursaControl
from controls.usuarios.docenteDaoControl import DocenteControl
from controls.academico.mallaCurricularControl import MallaCurricularControl
from controls.usuarios.estudianteDaoControl import EstudianteControl
from controls.login.personaDaoControl import PersonaDaoControl
from controls.seguimiento.asignacionControl import AsignacionDaoControl
from controls.academico.materiaControl import MateriaControl
from controls.academico.cicloControl import CicloControl
from controls.seguimiento.reporteControl import ReporteControl
from controls.login.rolDaoControl import RolDaoControl
from controls.seguimiento.unidadControl import UnidadControl
from controls.tda.linked.linkedList import Linked_List
import time
router = Blueprint('router', __name__)




#CORS(api)
cors = CORS(router, resource={
    r"/*":{
        "origins":"*"
    }
})

#GET: PARA PRESENTAR DATOS
#POST: GUARDA DATOS, MODIFICA DATOS Y EL INICIO DE SESION, EVIAR DATOS AL SERVIDOR

@router.route('/', ) #SON GETS
def inicio():
    return render_template('login/login.html')

@router.route('/login',  methods=["POST"])
def login():
    
    data = request.form
    cc = CuentaDaoControl()
    cuenta = cc._list().binary_search_models(data["correo"], "_correo")
                       
    if cuenta == -1:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('router.inicio'))
    elif cuenta._contrasenia == data["contrasenia"]:
        pc = PersonaDaoControl()
        listaPersonas = pc._list()
        persona = listaPersonas.binary_search_models(cuenta._idPersona, "_id")
        roles = persona._roles
        
        admin = roles.binary_search_models("Administrador", "_nombre")
        docente = roles.binary_search_models("Docente", "_nombre")
        
        if docente == -1:
            if admin != -1:
                return render_template('header.html', idPersona=persona._id, admin = "admin", docente = "no es")
            return render_template('header.html', idPersona=persona._id, docente = "no es", admin = " ")
        else:
            ac = AsignacionDaoControl()
            listaAsignaciones = ac._list()
            arrayasignaciones = listaAsignaciones.lineal_binary_search_models(persona._dni, "_cedula_docente").toArray
            mc = MateriaControl()
            listaMaterias = Linked_List()
            #recooremos el array de asignaciones
            for i in range(0, len(arrayasignaciones)):
                
                idMateria = arrayasignaciones[i]._id_materia
  
                materia = mc._list().binary_search_models(idMateria, "_id")

                if materia != -1:
                    listaMaterias.addNode(materia)
            
            if admin != -1:
                return render_template('vista_docente/materias.html', lista = pc.to_dic_lista(listaMaterias), idPersona=persona._id, admin = "admin", docente = "docente")
            
            
            return render_template('vista_docente/materias.html', lista=mc.to_dic_lista(listaMaterias), idPersona=persona._id, admin = "no es", docente = "docente")
    else:
        flash('Contraseña incorrecta', 'error')
        return redirect(url_for('router.inicio'))
    
 
@router.route('/home')
def home():
    return render_template('header.html')

#/home/{{idPersona}}/{{lista}}
@router.route('/home/<idPersona>/<docente>/<admin>')
def home_id(idPersona, docente, admin):
    print("**********************************")
    print(docente, admin)
    return render_template('header.html', idPersona=idPersona, docente = docente, admin = admin)


@router.route('/home/materias/<idPersona>/<docente>/<admin>')
def home_materias(idPersona, docente, admin):
    pc = PersonaDaoControl()
    listaPersonas = pc._list()
    persona = listaPersonas.binary_search_models(int(idPersona), "_id")
    roles = persona._roles
    docente = roles.binary_search_models("Docente", "_nombre")
        
    if docente == -1:
        return render_template('header.html', idPersona=persona._id,docente = docente, admin = admin)
    else:
        ac = AsignacionDaoControl()
        listaAsignaciones = ac._list()
        arrayasignaciones = listaAsignaciones.lineal_binary_search_models(persona._dni, "_cedula_docente").toArray
        mc = MateriaControl()
        listaMaterias = Linked_List()
        #recooremos el array de asignaciones
        for i in range(0, len(arrayasignaciones)):
                
            idMateria = arrayasignaciones[i]._id_materia
  
            materia = mc._list().binary_search_models(idMateria, "_id")

            if materia != -1:
                listaMaterias.addNode(materia)
            
        listaMaterias.print
    
    return render_template('vista_docente/materias.html', lista = pc.to_dic_lista(listaMaterias),idPersona=idPersona, docente = docente, admin = admin)

#VISTA DEL DOCENTE MATERIAS
@router.route('/home/materias')
def ver_materias():
    return render_template('vista_docente/materias.html')


#/home/materias/estudiantes/{{ materia.id }}


@router.route('/home/materias/estudiantes/<idMateria>/<idPersona>')
def ver_estudiantes(idMateria, idPersona):
    ac = AsignacionDaoControl()
    asignacion = ac._list().binary_search_models(int(idMateria), "_id_materia") #puede ser lineal
    
    if asignacion != -1:
        alumnos = Linked_List()
        ec = EstudianteControl()
        estudiantes = ec._list().toArray
        #recorre a los estudiantes
        for i in range(0, len(estudiantes)):
            cursas = estudiantes[i]._cursas
            cursa = cursas.binary_search_models(int(asignacion._id), "_asignacion")
            #print(estudiantes[i]._id)
            if cursa != -1:
                alumnos.addNode(estudiantes[i])
        print("#########################")
        print(idPersona)
        return render_template('vista_docente/alumnos.html', lista=ec.to_dic_lista(alumnos), idPersona=idPersona, idMateria=idMateria)
    else:
        return render_template('login/login.html')
    
@router.route('/home/materias/estudiantes/seguimiento/<idMateria>/<idEstudiante>/<idPersona>')
def seguimiento(idMateria, idEstudiante, idPersona):
    
    ec = EstudianteControl()
    estudiante = ec._list().binary_search_models(int(idEstudiante), "_id")
    mt = MateriaControl()
    materia = mt._list().binary_search_models(int(idMateria), "_id")
    ac = AsignacionDaoControl()
    asignacion = ac._list().binary_search_models(int(idMateria), "_id_materia")
    
    asignacion._reportes.print
    reportes = Linked_List()
    aprobar = 0
    reprobar = 0
    promedio = 0
    
    if asignacion != -1:
        reportes = asignacion._reportes
        if reportes._length != 0:
            reportes = reportes.lineal_binary_search_models(estudiante._dni, "_cedulaEstudiante")
            if reportes._length != 0:
                array = reportes.toArray
                for i in range(0, len(array)):
                    promedio += array[i]._nota
                    promedio = promedio / len(array)
        
                falta = 21 - promedio
        
                if falta <= 0:
                    aprobar = 1.0  # Ya has alcanzado o superado el promedio necesario
                else:
                    prob_aprobar = 0.0
                    for nota in range(7, 10):  # Probabilidad de obtener 8, 9 o 10
                        if nota <= falta:
                            prob_aprobar += 1 / 10  # Distribución uniforme
                    aprobar = prob_aprobar

                reprobar = 1 - aprobar 
                
                aprobar = round(aprobar * 100, 2)
                reprobar = round(reprobar * 100, 2)
                return render_template('vista_docente/seguimiento.html', idEstudiante=idEstudiante, lista = ec.to_dic_lista(reportes), paprobar = aprobar, preprobar = reprobar, idPersona = idPersona)
            else:
                return render_template('login/login.html')
        else:
            return render_template('login/login.html')
        
        
#VER LAS UNIDADES DE LA MATERIA DEL DOCENTE
@router.route('/home/materias/estudiantes/unidades/<idMateria>/<idDocente>')
def ver_unidades_docente(idMateria, idDocente):
    mt = MateriaControl()
    materia = mt._list().binary_search_models(int(idMateria), "_id")
    pc = PersonaDaoControl()
    persona = pc._list().binary_search_models(int(idDocente), "_id")
    cedulaDocente = persona._dni
    dc = DocenteControl()
    docente = dc._list().binary_search_models(cedulaDocente, "_dni")
    asignacion = materia._asignaciones.binary_search_models(docente._dni, "_cedula_docente")
    unidades = asignacion._unidades
    return render_template('vista_docente/unidades.html', lista=mt.to_dic_lista(unidades), idMateria=idMateria, idPersona=idDocente)
    
    


#---------------------------------------------Usuarios-----------------------------------------------------#
 
#Lista Docentes
@router.route('/home/docentes')
def lista_docente():
    dc = DocenteControl()
    list = dc._list()
    list.print
    return render_template('usuarios/guardarFormularioD.html', lista=dc.to_dic_lista(list))


#Lista Estudiantes
@router.route('/home/estudiantes/<idPersona>/<docente>/<admin>')
def lista_estudiante(idPersona, docente, admin):
    ec = EstudianteControl()
    list = ec._list()
    return render_template('usuarios/guardarFormularioE.html', lista=ec.to_dic_lista(list), idPersona=idPersona, docente = docente, admin = admin)


#---------------------------------------------Ordenar Usuarios------------------------------------------------------#

@router.route('/home/docentes/<tipo>/<attr>/<metodo>') 
def lista_personas_ordenar_docentes(tipo, attr, metodo):
    dc = DocenteControl()
    
    # E y D - Ordenar
    lista_docentes = dc._list()
    #-----------------------------------------------------#
    lista_docentes.sort_models(attr, int(tipo), int(metodo))
    
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": dc.to_dic_lista(lista_docentes)}),
        200
    )


#---------------------------------------------Busqueda Usuarios------------------------------------------------------#
#"http://localhost:5000/home/docentes/busqueda/"+valor+"/"+atributo

@router.route('/home/docentes/busqueda/<data>/<attr>')
def buscar_docente(data, attr):
    print("**********************************")
    print(data, attr)
    dc = DocenteControl()
    list = Linked_List()
    
    if attr == "_nombre" or attr == "_apellido" or attr == "_dni" or attr == "_titulo" or attr == "_cubiculo" or attr == "_idiomas" or attr == "_tipoContrato":
        list = dc._list().lineal_binary_search_models(data, attr)
    else:
        docente = dc._list().binary_search_models(data, attr)
        list.addNode(docente)
    
    
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": dc.to_dic_lista(list)}),
        200
    )

#--------------------------------------------- Modulo - Asignación------------------------------------------------------#
@router.route('/home/asignacion')
def lista_asignacion():
    ac  = AsignacionDaoControl()
    list = ac._list()
    list.print
    return render_template('seguimiento/listaAsignacion.html', lista=ac.to_dic_lista(list))


@router.route('/seguimiento/unidades/<pos>')
def ver_unidades(pos):
    ac = AsignacionDaoControl()
    unidades = ac._list().getData(int(pos)-1)._unidades
    return render_template("seguimiento/unidades.html",  lista = unidades.serializable, idUnidad = pos) 

#Ordenar Asignaciones
@router.route('/home/asignacion/<tipo>/<attr>/<metodo>')
def lista_asignacion_ordenar(tipo, attr, metodo):
    ac = AsignacionDaoControl()
    
    # E y D - Ordenar
    lista_asignaciones = ac._list()
    #-----------------------------------------------------#
    lista_asignaciones.sort_models(attr, int(tipo), int(metodo))
    
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": ac.to_dic_lista(lista_asignaciones)}),
        200
    )
#Buscar Asignaciones
@router.route('/home/asignacion/busqueda/<data>/<attr>')
def buscar_asignacion(data, attr):
    ac = AsignacionDaoControl()
    list = Linked_List()
    
    if attr == "_id_materia" or attr == "_cedula_docente" or attr == "_id":
        asignacion = ac._list().binary_search_models(data, attr)
        list.addNode(asignacion)
    else:
        list = ac._list().lineal_binary_search_models(data, attr)
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": ac.to_dic_lista(list)}),
        200
    )


#------------------------------------------------ Cursa-------------------------------------------------------------#

@router.route('/home/cursa')
def lista_cursa():
    cc  = CursaControl()
    list = cc._list()
    list.print
    return render_template('administrativo/cursa.html', lista=cc.to_dic_lista(list))



#--------------------------------------------- Malla - Curricular--------------------------------------------------#

@router.route('/home/malla')
def lista_malla():
    mcc = MallaCurricularControl()
    list = mcc._list()
    list.print
    return render_template('academico/malla.html', lista=mcc.to_dic_lista(list))


@router.route('/academico/ciclos/<pos>')
def ver_ciclos(pos):
    cc = CicloControl()
    ciclos = cc._list().getData(int(pos)-1)._ciclos
    return render_template("academico/ciclos.html",  lista = ciclos.serializable, idCiclos = pos) 


#Ordenar Malla Curricular
@router.route('/home/malla/<tipo>/<attr>/<metodo>')
def lista_malla_ordenar(tipo, attr, metodo):
    mcc = MallaCurricularControl()
    
    # E y D - Ordenar
    lista_malla = mcc._list()
    #-----------------------------------------------------#
    lista_malla.sort_models(attr, int(tipo), int(metodo))
    
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": mcc.to_dic_lista(lista_malla)}),
        200
    )
#Buscar Malla Curricular
@router.route('/home/malla/busqueda/<data>/<attr>')
def buscar_malla(data, attr):
    print(data, attr)
    mcc = MallaCurricularControl()
    list = Linked_List()
   
    if attr == "_nombre" or attr == "_descripcion" or attr == "_vigencia":
        malla = mcc._list().binary_search_models(data, attr)
        list.addNode(malla)
    else:
        list = mcc._list().lineal_binary_search_models(data, attr)
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": mcc.to_dic_lista(list)}),
        200
    )

#---------------------------------------------Ordenar -  Materia--------------------------------------------------#

@router.route('/home/materia')
def lista_materia():
    mc  = MateriaControl()
    list = mc._list()
    list.print
    return render_template('academico/materia.html', lista=mc.to_dic_lista(list))


#----------------------------------------------  Rol --------------------------------------------------#

@router.route('/home/rol/<idPersona>/<docente>/<admin>')
def lista_rol(idPersona, docente, admin):
    rdc = RolDaoControl()
    list = rdc._list()
    list.print
    return render_template('login/rol.html', lista=rdc.to_dic_lista(list), idPersona=idPersona, docente = docente, admin = admin)

#Ordenar
@router.route('/home/rol/<tipo>/<attr>/<metodo>')
def lista_rol_ordenar(tipo, attr, metodo):
    rdc = RolDaoControl()
    
    # E y D - Ordenar
    lista_roles = rdc._list()
    #-----------------------------------------------------#
    lista_roles.sort_models(attr, int(tipo), int(metodo))
    
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": rdc.to_dic_lista(lista_roles)}),
        200
    )

#Buscar
@router.route('/home/rol/busqueda/<data>/<attr>')
def buscar_rol(data, attr):
    rdc = RolDaoControl()
    list = Linked_List()
    
    if attr == "_nombre" or attr == "_descripcion" or attr == "_estado":
        list = rdc._list().lineal_binary_search_models(data, attr)
    else:
        rol = rdc._list().binary_search_models(data, attr)
        list.addNode(rol)
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": rdc.to_dic_lista(list)}),
        200
    )


#---------------------------------------------Ordenar -  Unidad--------------------------------------------------------#

@router.route('/home/unidad')
def lista_unidad():
    uc = UnidadControl()
    list = uc._list()
    list.print
    return render_template('usuarios/guardarFormularioE.html', lista=uc.to_dic_lista(list))


@router.route('/home/personas/agregar/<idPersona>/<docente>/<admin>')
def ver_personas(idPersona, docente, admin):
    return render_template('usuarios/personas.html', idPersona=idPersona, docente = docente, admin = admin)


@router.route('/home/personas/formularios/guardar', methods=["POST"])
def guardar_registro():
    pc = PersonaDaoControl()
    dc = DocenteControl()
    ec = EstudianteControl()
    data = request.form
    
    if not "apellidos" in data.keys():
        abort(400)
        
    # Validar y guardar datos comunes a todas las personas
    pc._persona._dni = data["dni"]
    pc._persona._nombre = data["nombre"]
    pc._persona._apellido = data["apellido"]
    pc._persona._fechaNacimiento = data["fechaNacimiento"]
    pc._persona._numTelefono = data["numTelefono"]
    pc.save()

    # Guardar datos específicos dependiendo del rol
    if data["rol"] == "docente":
        dc._docente._titulo = data["titulo"]
        dc._docente._cubiculo = data["cubiculo"]
        dc._docente._idiomas = data["idiomas"]
        dc._docente._tipoContrato = data["tipoContrato"]
        dc.save()

    elif data["rol"] == "estudiante":
        ec._estudiante._nota = data["nota"]
        ec._estudiante._asistencia = data["asistencia"]
        ec._estudiante._colegioProcedencia = data["colegioProcedencia"]
        ec.save()

    # Redireccionar según el rol
    if data["rol"] == "docente":
        return redirect("/usuarios/guardarFormulariosD", code=302)
    elif data["rol"] == "estudiante":
        return redirect("/usuarios/guardarFormulariosE", code=302)
    else:
        abort(400) 



@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pc = PersonaDaoControl()
    dc = DocenteControl()
    ec = EstudianteControl()

    data = request.form
    pos = data["id"]
    personas = pc._list().get(int(pos)-1)
    if not "apellido" in data.keys():
        abort(400)
        
    # Validaciones básicas
    if "rol" not in data:
        abort(400)

    # Actualizar datos comunes a todas las personas
    pc._persona = personas
    pc._persona._dni = data["cedula"]
    pc._persona._nombre = data["nombre"]
    pc._persona._apellido = data["apellido"]
    pc._persona._fechaNacimiento = data["fechaNacimiento"]
    pc._persona._numTelefono = data["numTelefono"]
    pc.merge(int(pos)-1)

    # Actualizar datos específicos dependiendo del rol
    role = data["rol"]
    if role == "Docente":
        dc._docente = personas
        dc._docente._titulo = data["titulo"]
        dc._docente._cubiculo = data["cubiculo"]
        dc._docente._idiomas = data["idiomas"]
        dc._docente._tipoContrato = data["tipoContrato"]
        dc.merge(int(pos)-1)

    
    elif role == "Estudiante":
        ec._estudiante = personas
        ec._estudiante._nota = data["nota"]
        ec._estudiante._asistencia = data["asistencia"]
        ec._estudiante._colegioProcedencia = data["colegioProcedencia"]
        ec.merge(int(pos)-1)
    
    return redirect("/personas", code=302)


@router.route('/personas/eliminar', methods=["POST"])
def eliminar_personas():
    pc = PersonaDaoControl()
    pos = request.form["id"]
    pc._delete(int(pos)-1)

    dc = DocenteControl()
    dc._delete(int(pos)-1)

    ec = EstudianteControl()
    ec._delete(int(pos)-1)


    return redirect("/personas", code=302)



