from flask import Flask 
app=Flask(__name__)
@app.route("/hola")
def hello ():
    return "Hello world"
@app.route("/chau")
def goodbye ():
    return "goodbye"
app.run()