from datetime import datetime
import inspect
from .ClientId import ClientId
from .ClientType import ClientType
from .ClientPhone import ClientPhone
from .ClientName import ClientName
from .ClientEmail import ClientEmail
from .ClientAddress import ClientAddress
from .ClientIsActive import ClientIsActive
from .ClientCreatedAt import ClientCreatedAt

# Entidad cliente
class Client:
    def __init__(self, id: ClientId, type: ClientType, name: ClientName, email: ClientEmail, address: ClientAddress, phone: ClientPhone, created_at: ClientCreatedAt, is_active: ClientIsActive):
        """
        Initializes a new instance of the Client class.

        Args:
            id (ClientId): The unique identifier for the client.
            type (ClientType): The type of the client.
            name (ClientName): The name of the client.
            email (ClientEmail): The email address of the client.
            address (ClientAddress): The address of the client.
            phone (ClientPhone): The phone number of the client.
            created_at (ClientCreatedAt): The datetime when the client was created.
            is_active (ClientIsActive): A flag indicating whether the client is active.
        """
        self.id = id
        self.type = type
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.is_active = is_active
        self.created_at = created_at
    
    #Servicio de dominio: Se denomina asi porque no depende de las otras capas    
    def __str__(self):
        """
        Returns a string representation of the client.

        The string representation is in the format:
            "<name> (<email>)"
        Where <name> is the client's name and <email> is the client's email address.

        Returns:
            str: A string representation of the client.
        """
        return "%s (%s)" % (self.name.value, self.email.value)
    
    
    def to_dict(self):
        """
        Convierte la entidad en un diccionario para su serializacion (json)
        Se utiliza inspect.getmembers para obtener los atributos de la entidad
        y se itera sobre ellos para obtener un diccionario con los valores
        de los atributos. Se utiliza el nombre del atributo como clave y
        el valor del atributo como valor. Si el valor es una instancia de
        datetime, se utiliza el metodo isoformat() para convertirlo en una
        cadena en formato ISO 8601.
        De no hacerse todo esto, al intentar serializar la entidad se 
        obtendria un error de serializacion de la libreria json debido a que
        la Clase esta tiene atributos que asu vez son otras clases con atributos
        """
        attributes = inspect.getmembers(self, lambda a: not inspect.ismethod(a))
        # return {key: value.value for key, value in attributes if not key.startswith('__')}
        return {key: value.value.isoformat() if isinstance(value.value, datetime) else value.value for key, value in attributes if not key.startswith('__')}
    
    