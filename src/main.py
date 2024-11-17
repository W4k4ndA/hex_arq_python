from flask import Flask, request

from libs.Clients.infraestructure.FlaskClientController import FlaskClientController

app = Flask(__name__)

app.add_url_rule("/clients", view_func=lambda: FlaskClientController().get_all(request), methods=["GET"])
# app.add_url_rule("/clients", view_func=FlaskClientController().get_all, methods=["GET"])
app.add_url_rule("/clients", view_func=FlaskClientController().create, methods=["POST"])
app.add_url_rule("/clients/<id>", view_func=FlaskClientController().get_one_by_id, methods=["GET"])
app.add_url_rule("/clients/<id>", view_func=FlaskClientController().edit, methods=["PUT"])
app.add_url_rule("/clients/<id>", view_func=FlaskClientController().delete, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)
