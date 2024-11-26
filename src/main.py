from flask import Flask
from libs.Clients.infraestructure.ClientsControllers import get_all, get_one_by_id, create, edit, delete
# from libs.Clients.infraestructure.FlaskClientController import FlaskClientController

app = Flask(__name__)

# app.add_url_rule("/clients", view_func=FlaskClientController().get_all, methods=["GET"])
app.add_url_rule("/clients", view_func=get_all, methods=["GET"])
app.add_url_rule("/clients", view_func=create, methods=["POST"])
app.add_url_rule("/clients/<string:id>", view_func=get_one_by_id, methods=["GET"])
app.add_url_rule("/clients/<string:id>", view_func=edit, methods=["PUT"])
app.add_url_rule("/clients/<string:id>", view_func=delete, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)
