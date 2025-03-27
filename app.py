from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def inicio():
    return render_template('index.html')

@app.route('/contactame')
def contact():
    return render_template('contactame.html')


@app.route('/proyetos')
def proyectos():
    return render_template('proyectos.html')


@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html')


@app.route('/AcercaDe')
def acerca_de():
    return render_template('Acerca_de.html')


if __name__=='__main__':
    app.run(debug=True)