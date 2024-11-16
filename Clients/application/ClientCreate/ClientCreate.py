import datetime
from Clients.domain.ClientRepository import ClientRepository
from Clients.domain.Client import Client
from Clients.domain.ClientId import ClientId
from Clients.domain.ClientType import ClientType
from Clients.domain.ClientName import ClientName
from Clients.domain.ClientEmail import ClientEmail
from Clients.domain.ClientAddress import ClientAddress
from Clients.domain.ClientPhone import ClientPhone
from Clients.domain.ClientIsActive import ClientIsActive
from Clients.domain.ClientCreatedAt import ClientCreatedAt

class ClientCreate:
    def __init__(self, repository: ClientRepository):
        self.__repository = repository
    
    def run(self, id: str, type: bool, name: str, email: str, address: str, phone: str, created_at: datetime, is_active: bool) -> None:
        client = Client(ClientId(id), 
                        ClientType(type),
                        ClientName(name), 
                        ClientEmail(email),
                        ClientAddress(address),
                        ClientPhone(phone),
                        ClientCreatedAt(created_at),
                        ClientIsActive(is_active))
        
        return self.__repository.create(client)