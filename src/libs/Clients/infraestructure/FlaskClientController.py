from datetime import datetime
from flask import Request, Response, jsonify
from ..domain.ClientNotFoundError import ClientNotFoundError
from ...Shared.infrastructure.ServiceContainer import ServiceContainer

class FlaskClientController:

    def __init__(self):
        """
        Initializes a new instance of the FlaskClientController class.

        This class provides methods that act as Flask endpoints to manage the
        clients of the application. The methods of this class are intended to be
        used as callbacks for Flask routes.

        """
        pass

    def get_all(self, request: Request) -> Response:
        """
        Retrieves all clients from the repository.

        Args:
            request (Request): The request object generated by Flask.

        Returns:
            Response: A JSON response containing a list of client objects.

        """
        clients = ServiceContainer.client.get_all.run()
        
        # La funcion jsonify de flask utiliza json.dumps internamente para 
        # serializar el objeto que se le pasa como parametro. Sin embargo, la funcion
        # json.dumps no serializa correctamente objetos que contienen atributos 
        # que son objetos de tipo datetime o atributos que asu vez son objetos con
        # atributos, por lo que se utiliza el metodo to_dict (que se crea manualmente)
        # de la clase Client que devuelve un diccionario con los atributos de la
        # clase (valores de los atributos son strings en formato ISO 8601
        # para las fechas y horas). Ademas, el metodo to_dict permite poder
        # obtener automanticamente los valores de los atributos de la clase sin tener
        # que tiparlos manualmene y convertirlos automaticamente en un diccionario.
        # Diccionario que luego es el que serializa 
        response = [client.to_dict() for client in clients]
        return jsonify(response), 200

    def get_one_by_id(self, request: Request) -> Response:
        """
        Retrieves a client from the repository using the provided client ID.

        Args:
            request (Request): The request object generated by Flask.

        Returns:
            Response: A JSON response containing a client object if the client
                exists, otherwise a 404 response.

        """
        id = request.view_args.get("id")
        if not id:
            return jsonify({"message": "id is required"}), 400
        try:
            client = ServiceContainer.client.get_one_by_id.run(id)
            response = client.to_dict()
            return jsonify(response)        
        except Exception as e:
            if isinstance(e, ClientNotFoundError):
                return jsonify({"message": e.message}), 404    
            else:
                raise e

    def create(self, request: Request) -> Response:
        """
        Creates a new client using the provided request data.

        Args:
            request (Request): The request object containing JSON data for the new client.
                Expected JSON fields include:
                - id (str): The unique identifier for the client.
                - type (int): The type of client (0 for False, 1 for True).
                - name (str): The name of the client.
                - email (str): The email address of the client.
                - address (str): The address of the client.
                - phone (str): The phone number of the client.
                - created_at (str): The creation date of the client in "YYYYMMDD HH:MM:SS" format.
                - is_active (int): The active status of the client (0 for False, 1 for True).

        Returns:
            Response: A JSON response with status code 201 indicating successful creation.
        """
        #debido a que el objeto client recibe un tipo boleano, se utiliza un diccionario
        #para convertir los enteros 0 y 1 en booleanos
        cast_boolean_field = {
            0:  False,
            1:  True,
        }
        
        body = request.get_json()
        id = body["id"]
        type = cast_boolean_field.get(body["type"])
        name = body["name"]
        email = body["email"]
        address = body["address"]
        phone = body["phone"]
        created_at = datetime.strptime(body["created_at"], "%Y%m%d %H:%M:%S") 
        is_active = cast_boolean_field.get(body["is_active"])
                
        ServiceContainer.client.create.run(id, type, name, email, address, phone, created_at, is_active)
        return jsonify({}), 201

    def edit(self, request: Request) -> Response:
        """
        Updates an existing client with the provided request data.

        Args:
            request (Request): The request object containing JSON data for the updated client.
                Expected JSON fields include:
                - id (str): The unique identifier for the client.
                - type (int): The type of client (0 for False, 1 for True).
                - name (str): The name of the client.
                - email (str): The email address of the client.
                - address (str): The address of the client.
                - phone (str): The phone number of the client.
                - created_at (str): The creation date of the client in "YYYYMMDD HH:MM:SS" format.
                - is_active (int): The active status of the client (0 for False, 1 for True).

        Returns:
            Response: A JSON response with status code 204 indicating successful update.
        """
        cast_boolean_field = {
            0:  False,
            1:  True,
        }
        
        body = request.get_json()
        id = body["id"]
        type = cast_boolean_field.get(body["type"])
        name = body["name"]
        email = body["email"]
        address = body["address"]
        phone = body["phone"]
        created_at = datetime.strptime(body["created_at"], "%Y%m%d %H:%M:%S") 
        is_active = cast_boolean_field.get(body["is_active"])
        
        ServiceContainer.client.edit.run(id, type, name, email, address, phone, created_at, is_active)
        return jsonify({}), 204

    def delete(self, request: Request) -> Response:
        """
        Deletes a client from the repository using the provided client ID.

        Args:
            request (Request): The request object generated by Flask.

        Returns:
            Response: A JSON response with status code 204 indicating successful deletion.
        """
        id = request.view_args.get("id")
        ServiceContainer.client.delete.run(id)
        return jsonify({}), 204
    
    
    