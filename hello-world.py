import os
from flask import Flask, Blueprint

# defino las rutas en un componente separado en Blueprint
main_router = Blueprint("main", __name__)

@main_router.route("/")
def hola_mundo():
    """Ejemplo de ruta 'Hola Mundo' usando variables de entorno (.env)"""
    name = os.environ.get("name", "Mundo")
    return f"¡Hola {name}!"

# Función fábrica para inicializar y configurar la app
def create_app():
    app = Flask(__name__)
    
    # Registramos el Blueprint en la aplicación principal
    app.register_blueprint(main_router)
    
    return app

if __name__ == "__main__":
    # Creo la app y ejecuto
    app = create_app()
    
    port_env = os.environ.get("port", "3030")
    app.run(
        debug=True, 
        host="0.0.0.0", 
        port=int(port_env)
    )
