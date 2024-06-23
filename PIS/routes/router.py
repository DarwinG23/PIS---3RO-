from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response, url_for, flash, Flask
from flask_cors import CORS
from controls.login.cuentaDaoControl import CuentaDaoControl

from controls.usuarios.docenteDaoControl import DocenteControl
from controls.usuarios.estudianteDaoControl import EstudianteControl
from controls.login.personaDaoControl import PersonaDaoControl
from controls.seguimiento.asignacionControl import AsignacionDaoControl
from controls.academico.materiaControl import MateriaControl
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
        docente = roles.binary_search_models("Docente", "_nombre")
        
        if docente == -1:
            return render_template('header.html', idPersona=persona._id)
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
            
            
            return render_template('vista_docente/materias.html', lista=mc.to_dic_lista(listaMaterias), idPersona=persona._id)
    else:
        flash('Contraseña incorrecta', 'error')
        return redirect(url_for('router.inicio'))
    
 
@router.route('/home')
def home():
    return render_template('header.html')

#/home/{{idPersona}}/{{lista}}
@router.route('/home/<idPersona>')
def home_id(idPersona):
    return render_template('header.html', idPersona=idPersona)


@router.route('/home/materias/<idPersona>')
def home_materias(idPersona):
    pc = PersonaDaoControl()
    listaPersonas = pc._list()
    persona = listaPersonas.binary_search_models(int(idPersona), "_id")
    roles = persona._roles
    docente = roles.binary_search_models("Docente", "_nombre")
        
    if docente == -1:
        return render_template('header.html', idPersona=persona._id)
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
    
    return render_template('vista_docente/materias.html', lista = pc.to_dic_lista(listaMaterias),idPersona=idPersona)

#VISTA DEL DOCENTE MATERIAS
@router.route('/home/materias')
def ver_materias():
    return render_template('vista_docente/materias.html')


#/home/materias/estudiantes/{{ materia.id }}


@router.route('/home/materias/estudiantes/<idMateria>/<idPersona>')
def ver_estudiantes(idMateria, idPersona):
    ac = AsignacionDaoControl()
    asignacion = ac._list().binary_search_models(int(idMateria), "_id_materia")
    
    if asignacion != -1:
        alumnos = Linked_List()
        ec = EstudianteControl()
        estudiantes = ec._list().toArray
        #recorre a los estudiantes
        for i in range(0, len(estudiantes)):
            cursas = estudiantes[i]._cursas
            cursa = cursas.binary_search_models(int(asignacion._id), "_asignacion")
            
            if cursa != -1:
                alumnos.addNode(estudiantes[i])
          
        return render_template('vista_docente/alumnos.html', lista=ec.to_dic_lista(alumnos), idPersona=idPersona)
    else:
        return render_template('login/login.html')
    
    


#---------------------------------------------Usuarios-----------------------------------------------------#
@router.route('/home/personas')
def lista_docente():
    dc = DocenteControl()
    list = dc._list()
    return render_template('usuarios/guardarFomulario.html', lista=dc.to_dic_lista(list))




# @router.route('home/estudiantes')
# def lista_docente():
#     dc = EstudianteControl()
#     list = dc._list()
#     return render_template('usuarios/guardarFormularioE.html', lista=dc.to_dic(list))


# @router.route('/formularios/modificar', methods=["POST"])
# def modificar_docentes():
#     dc = DocenteControl()
#     data = request.form
#     pos = data["id"]
#     docente = dc._list().getData(int(pos)-1)   
    
#     if not "apellidos" in data.keys():
#         abort(400)
        
#     TODO ...Validar

#     dc._docente = docente
#     dc._docente._nombre = data["nombre"]
#     dc._docente._apellidos = data["apellidos"]
#     dc._docente._cedula = data["cedula"]
#     dc._docente._email = data["email"]
#     dc._docente._telefono = data["telefono"]

#     dc.merge(int(pos)-1)

#     return redirect("home/docentes", code=302)
