from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'CLAVE_SECRETA_0011'


@app.route('/')
def inicio():
    return render_template('index.html', nav_title="inicio")

@app.route('/contactame', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form.get('name')
        email = request.form.get('email')
        asunto = request.form.get('subject')
        mensaje = request.form.get('message')
        if not nombre or not email or not asunto or not mensaje:
            flash("Por favor completa todos los campos")
            return render_template('contactame.html', nav_title="contacto")
        else:
            flash("Mensaje enviado correctamente")
            print("Nombre: ", nombre)
            print("Email: ", email)
            print("Asunto: ", asunto)
            print("Mensaje: ", mensaje)
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