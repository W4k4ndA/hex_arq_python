from flask import Request, Response, jsonify

from Clients.domain.ClientNotFoundError import ClientNotFoundError
from Shared.infrastructure import ServiceContainer

class FlaskClientController:

    def __init__(self):
        pass

    def get_all(self, request: Request) -> Response:
        users = ServiceContainer["client"]["get_all"].run()
        
        return jsonify(users)

    def get_one_by_id(self, request: Request) -> Response:
        id = request.args.get("id")
        if not id:
            return jsonify({}), 400
        try:
            user = ServiceContainer["client"]["get_one_by_id"].run(id)
            return jsonify(user)        
        except Exception as e:
            if isinstance(e, ClientNotFoundError):
                return jsonify({"message": e.message}), 404    
            else:
                raise e


    def create(self, request: Request) -> Response:
        body = request.get_json()
        id = body["id"]
        type = body["type"]
        name = body["name"]
        email = body["email"]
        address = body["address"]
        phone = body["phone"]
        
        ServiceContainer["client"]["create"].run(id, type, name, email, address, phone)
        return jsonify({}), 201

    def edit(self, request: Request) -> Response:
        body = request.get_json()
        id = body["id"]
        type = body["type"]
        name = body["name"]
        email = body["email"]
        address = body["address"]
        phone = body["phone"]
        created_at = body["created_at"]
        is_active = body["is_active"]
        
        ServiceContainer["client"]["edit"].run(id, type, name, email, address, phone, created_at, is_active)
        return jsonify({}), 204

    def delete(self, request: Request) -> Response:
        id = request.args.get("id")        
        ServiceContainer["client"]["delete"].run(id)
        return jsonify({}), 204