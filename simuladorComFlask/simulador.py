from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/resultado')
def resultado():
    return render_template("resultado.html")

if __name__ == '__main__':
    app.run(debug=True)