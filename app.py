# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("index.html")



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



# Este bloque se ejecuta solo si corremos `python app.py` desde la terminal.
if __name__ == "__main__":
    # `debug=True` sirve en desarrollo porque reinicia el servidor
    # cuando detecta cambios y muestra errores con mas detalle.
    app.run(debug=True)
