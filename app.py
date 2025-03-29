from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', nav_title="inicio")

@app.route('/contactame')
def contact():
    return render_template('contactame.html', nav_title="contacto")


@app.route('/proyetos')
def proyectos():
    return render_template('proyectos.html', nav_title="proyectos")


@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html', nav_title="lenguajes")


@app.route('/AcercaDe')
def acerca_de():
    return render_template('Acerca_de.html', nav_title="acerca de")


if __name__=='__main__':
    app.run(debug=True)