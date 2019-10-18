from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variables_list = ['PH','Temperatura','Humedad Tierra','Humedad Aire','Distancia','Luz Solar']


@app.route('/')
def index():
    return '<h1>TIPOS DE SENSORES</h1><p>Con estos enpoints puedes crear y ver los tipos de sensores</p><br><p>/CrearSensor  y  /listarSensores</p>'

@app.route('/crearSensor',methods=['GET'])
def crearSensor():
    return render_template('crearSensor.html', variables=variables_list)

@app.route('/listarSensores',methods=['GET'])
def listarSensores():
    sensores_list = requests.get('https://api-tiposensores.azurewebsites.net/tipoSensores').json()
    return render_template('listarSensores.html', sensores=sensores_list)

@app.route('/guardarSensor',methods=['POST'])
def guardarSensor():
    sensor = dict(request.values)
    sensor['precio'] = int(sensor['precio'])
    requests.post('https://api-tiposensores.azurewebsites.net/tipoSensores',json=sensor)
    
    return listarSensores()
