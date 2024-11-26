from flask import request
from  libs.Clients.infraestructure.FlaskClientController import FlaskClientController

controller = FlaskClientController()


def get_all():
    """
    Retrieves all clients using the FlaskClientController.

    Returns:
        Response: A JSON response containing a list of client objects.
    """
    return controller.get_all(request)

def create():
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
    return controller.create(request)

def get_one_by_id(id: str):
    """
    Retrieves a client from the repository using the provided client ID.

    Args:
        id (str): The unique identifier of the client to be retrieved.

    Returns:
        Response: A JSON response containing a client object if the client
            exists, otherwise a 404 response.
    """
    return controller.get_one_by_id(request)

def edit(id: str):
    """
    Updates an existing client with the provided request data.

    Args:
        id (str): The unique identifier of the client to be updated.

    Returns:
        Response: A JSON response with status code 204 indicating successful update.
    """
    return controller.edit(request)

def delete(id: str):
    """
    Deletes a client from the repository using the provided client ID.

    Args:
        id (str): The unique identifier of the client to be deleted.

    Returns:
        Response: A JSON response with status code 204 indicating successful deletion.
    """
    return controller.delete(request)






