from datetime import datetime

from Clients.domain.Client import Client

from Clients.domain.ClientEmail import ClientEmail
from Clients.domain.ClientName import ClientName
from Clients.domain.ClientType import ClientType
from Clients.domain.ClientAddress import ClientAddress
from Clients.domain.ClientCreatedAt import ClientCreatedAt
from Clients.domain.ClientId import ClientId
from Clients.domain.ClientIsActive import ClientIsActive
from Clients.domain.ClientPhone import ClientPhone
from Clients.domain.ClientRepository import ClientRepository

class ClientEdit:
    def __init__(self, repository: ClientRepository):
        """
        Inicializa la clase ClientEdit con un repositorio de clientes.
        
        Args:
            repository (ClientRepository): El repositorio de clientes.
        """
        self.__repository = repository
    
    def run(self, id: str, type: bool, name:str, email: str, address: str, phone: str, created_at: datetime, is_active: bool) -> None:
        """
        Edita un cliente existente en el repositorio con los detalles proporcionados.

        Args:
            id (str): El identificador único del cliente.
            type (bool): El tipo de cliente.
            name (str): El nombre del cliente.
            email (str): El correo electrónico del cliente.
            address (str): La dirección del cliente.
            phone (str): El número de teléfono del cliente.
            created_at (datetime): La fecha de creación del cliente.
            is_active (bool): Estado de actividad del cliente.

        Returns:
            None
        """
        client = Client(ClientId(id), 
                        ClientType(type),
                        ClientName(name), 
                        ClientEmail(email), 
                        ClientAddress(address),
                        ClientPhone(phone),
                        ClientCreatedAt(created_at),
                        ClientIsActive(is_active))
        
        return self.__repository.edit(client)