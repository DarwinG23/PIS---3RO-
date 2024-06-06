from flask import Blueprint, jsonify, abort , request, render_template, redirect, make_response
from flask import flash
from flask_cors import CORS
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

@router.route('/') #SON GETS
def home():
    return render_template('index.html')


