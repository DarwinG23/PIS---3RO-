from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response, url_for, flash, Flask
from flask_cors import CORS
from controls.login.cuentaDaoControl import CuentaDaoControl

from controls.usuarios.docenteDaoControl import DocenteControl
from controls.usuarios.estudianteDaoControl import EstudianteControl
from controls.login.personaDaoControl import PersonaDaoControl

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
        return redirect('/home')
    else:
        flash('Contraseña incorrecta', 'error')
        return redirect(url_for('router.inicio'))
    
 
@router.route('/home')
def home():
    return render_template('index.html')


#---------------------------------------------Usuarios-----------------------------------------------------#
 
#Lista Docentes
@router.route('/home/personas')
def lista_docente():
    dc = DocenteControl()
    list = dc._list()
    return render_template('usuarios/guardarFormularioD.html', lista=dc.to_dic_lista(list))


#Lista Estudiantes
@router.route('/home/estudiantes')
def lista_estudiante():
    ec = EstudianteControl()
    list = ec._list()
    return render_template('usuarios/guardarFormularioE.html', lista=ec.to_dic_lista(list))


@router.route('/home/estudiantes/<tipo>/<attr>/<metodo>') 
def lista_personas_ordenar(tipo, attr, metodo):
    dc = DocenteControl()
    ec = EstudianteControl()
    
    # E y D - Ordenar
    lista_estudiantes = ec._list()
    lista_docentes = dc._list()
    #-----------------------------------------------------#
    lista_estudiantes.sort_models(attr, int(tipo), int(metodo))
    lista_docentes.sort_models(attr, int(tipo), int(metodo))
    
    lista_personas = lista_estudiantes + lista_docentes
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": dc.to_dic_lista(lista_personas)}),
        200
    )
    
@router.route('/home/busqueda/personas/<tipo>/<data>/<attr>')
def buscar_persona(tipo, data, attr):
    dc = DocenteControl()
    ec = EstudianteControl()

    if tipo == "1":
        list = ec._list().lineal_binary_search_models(data, attr)
        list = dc._list().lineal_binary_search_models(data, attr)
    elif tipo == "2":
        list = ec._list().binary_search_models(data, attr)
        list = dc._list().binary_search_models(data, attr)
    
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": dc.to_dic_lista(list)}),
        200
    )



@router.route('/home/personas/agregar')
def ver_personas():
    return render_template('usuarios/personas.html')


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



