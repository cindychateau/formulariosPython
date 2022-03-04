from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave super secreta" #Establecemos una clave secreta para dar más seguridad a las cookies

#En nuestra ruta raíz quiero que se muestre un formulario
@app.route("/")
def formulario():
    return render_template("index.html")

#Ponemos action a nuestro formulario
@app.route("/success", methods=['POST', 'GET'])
def crea_user():
    print(request.form)

    #Guardamos info en sesión
    session['usuario'] = request.form['nombre'] #Está obteniendo desde atributo NAME de mi input
    session['email'] = request.form['email']

    #Usamos redirect para evitar el reenvío del formulario
    return redirect('/procesado')

@app.route("/procesado")
def procesado():
    return render_template("procesado.html")
    

if __name__ == "__main__":
    app.run(debug=True)