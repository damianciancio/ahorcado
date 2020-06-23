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

@app.route('/partida', methods=['GET'])
def partida():
    partida = Partida()
    partida.inicializar("hola")
    session["partida"] = partida.get_dict()
    session["mensaje"] = ""
    return render_template('jugar.html', partida=session["partida"],mensaje=session["mensaje"])


@app.route('/arriesgar', methods=['POST'])
def arriesgar():
    partida = Partida()
    partida.create_from_dictionary(session["partida"])
    if request.method == 'POST':
        letra_arriesgada = request.form['letra']
        if partida.arriesgar(letra_arriesgada):
            session["mensaje"] = "Muy bien!"
        else:
            session["mensaje"] = "Error"
        return redirect('/partida')

#app.run()

