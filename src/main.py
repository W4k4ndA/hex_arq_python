from flask import Flask
from libs.Clients.infraestructure.FlaskClientController import FlaskClientController

#incorporamos el controlador http de Flask para gestionar las peticiones
controller = FlaskClientController()

app = Flask(__name__)

app.add_url_rule("/clients", view_func=controller.get_all, methods=["GET"])
app.add_url_rule("/clients", view_func=controller.create, methods=["POST"])
app.add_url_rule("/clients/<string:id>", view_func=controller.get_one_by_id, methods=["GET"])
app.add_url_rule("/clients/<string:id>", view_func=controller.edit, methods=["PUT"])
app.add_url_rule("/clients/<string:id>", view_func=controller.delete, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)
