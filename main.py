from flask import Flask 
app=Flask(__name__)
@app.route("/hola")
def hello ():
    return "Hello world"
@app.route("/chau")
def goodbye ():
    return "goodbye"
@app.route('/saludo/<nombre>')
def hola(nombre):
    return f'Saludos, {nombre}!'
@app.route('/LucioManitta/<nombre>/<apellido>')
def saludo(nombre, apellido):
    return f'Saludos, {nombre}, {apellido}'
app.run()