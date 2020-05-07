from aplicacao import app
from flask import render_template

@app.route('/')
def index():
    contexto = {'titulo':'index',
    'mensagens': ['usuario1: olá', 'usuario2: olá']}
    return render_template('index.html', **contexto)

@app.route('/enviar')
def enviar():
    contexto = {'titulo':'Enviar mensagem'}
    return render_template('mensagens.html', **contexto)

app.run(debug=True)


