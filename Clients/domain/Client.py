from ClientId import ClientId
from ClientType import ClientType
from ClientPhone import ClientPhone
from ClientName import ClientName
from ClientEmail import ClientEmail
from ClientAddress import ClientAddress
from ClientIsActive import ClientIsActive
from ClientCreatedAt import ClientCreatedAt

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
        return "%s (%s)" % (self.name, self.email)