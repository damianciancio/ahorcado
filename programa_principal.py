from ahorcado import Partida
from flask import Flask, session, render_template, request, redirect
import base64
from json import dumps
from flask_session import Session

app = Flask(__name__)
app.secret_key = "asdsadsadas"

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')

@app.route('/iniciar', methods=['GET'])
def iniciar():
    partida = Partida()
    partida.inicializar("hola")
    session["partida"] = partida.get_dict()
    session["mensaje"] = ""
    return render_template('jugar.html', partida=session["partida"],mensaje=session["mensaje"])

@app.route('/partida', methods=['GET'])
def partida():
    partida = Partida()
    partida.create_from_dictionary(session["partida"])
    mensaje = session["mensaje"]
    if partida.validar_terminado()==False:
        return render_template('jugar.html', partida=session["partida"],mensaje=session["mensaje"])
    elif partida.validar_terminado()=='perdio':
        return render_template('fin.html')
    elif partida.validar_terminado()=='gano':
        return render_template('gano.html')

@app.route('/arriesgar', methods=['POST'])
def arriesgar():
    print(session["partida"])
    partida = Partida()
    partida.create_from_dictionary(session["partida"])
    if request.method == 'POST':
        letra_arriesgada = request.form['letra']
        if partida.arriesgar(letra_arriesgada):
            session["mensaje"] = "Muy bien!"
        else:
            session["mensaje"] = "Error"
        session["partida"] = partida.get_dict()
        return redirect('/partida')

if __name__ == "__main__":
    app.run(debug=True) #El debug es para ver los errores
