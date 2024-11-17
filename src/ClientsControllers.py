from flask import request
from  libs.Clients.infraestructure.FlaskClientController import FlaskClientController

def get_all():
    controller = FlaskClientController()
    return controller.get_all(request)

