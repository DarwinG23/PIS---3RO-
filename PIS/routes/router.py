from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response, url_for, flash, Flask
from flask_cors import CORS
from controls.login.cuentaDaoControl import CuentaDaoControl

from controls.usuarios.docenteDaoControl import DocenteControl
from controls.usuarios.estudianteDaoControl import EstudianteControl
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
@router.route('/home/personas')
def lista_docente():
    dc = DocenteControl()
    list = dc._list()
    return render_template('usuarios/guardarFomulario.html', lista=dc.to_dict(list))




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
