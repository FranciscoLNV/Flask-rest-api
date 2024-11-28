from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message



app = Flask(__name__)

# Configuración del correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'fpoloestrada@gmail.com'  # Nuevo correo personal
app.config['MAIL_PASSWORD'] = 'prqo uabt fcxx ordq'  # Contraseña de aplicación generada
app.config['MAIL_DEFAULT_SENDER'] = 'fpoloestrada@gmail.com'
mail = Mail(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        mensaje = request.form['mensaje']

        # Crear el mensaje de correo
        msg = Message('Nuevo mensaje de contacto', recipients=['fpoloestrada@gmail.com'])
        msg.body = f"""
        Has recibido un nuevo mensaje de contacto:
        
        Nombre: {nombre}
        Email: {email}
        Teléfono: {telefono}
        
        Mensaje:
        {mensaje}
        """
        try:
            # Enviar el correo
            mail.send(msg)
            # Redirigir a la página principal después de enviar el mensaje
            return redirect(url_for('home'))
        except Exception as e:
            # Si hay un error, mostrarlo
            return f"Error al enviar el mensaje: {str(e)}"

    return render_template('contacto.html')

if __name__ == "__main__":
    app.run(debug=True)