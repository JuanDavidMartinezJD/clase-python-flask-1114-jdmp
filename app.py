# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template, request


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("index.html")

#MIS RUTAS POR JUAN DAVID MARTINEZ PERDOMO

@app.route("/ruta1")
def route1():
    return render_template("route1.html")


@app.route("/ruta2")
def route2():
    return render_template("route2.html")



@app.route("/ruta3")
def route3():
    return render_template("route3.html")


@app.route("/ruta4")
def route4():
    return render_template("route4.html")


@app.route("/acerca")
def acerca():
    return render_template("acerca.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")



@app.route("/recursos")
def recursos():

    recursos_clase = [
        "Entorno virtual",
        "Rutas en Flask",
        "Plantillas HTML",
        "Variables con Jinja"
    ]

    return render_template("recursos.html", recursos=recursos_clase)



@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    mensaje = None
    
    if request.method == "POST":
        # El usuario envio el formulario
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        programa = request.form.get("programa")
        
        # Validacion basica
        if nombre and email and programa:
            mensaje = f"Bienvenido {nombre}! Te hemos registrado."
        else:
            mensaje = "Por favor completa todos los campos."
    
    return render_template("inscripcion.html", mensaje=mensaje)
  


# Este bloque se ejecuta solo si corremos `python app.py` desde la terminal.
if __name__ == "__main__":
    # `debug=True` sirve en desarrollo porque reinicia el servidor
    # cuando detecta cambios y muestra errores con mas detalle.
    app.run(debug=True)
