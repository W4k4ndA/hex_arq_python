import datetime
from ...domain.ClientRepository import ClientRepository
from ...domain.Client import Client
from ...domain.ClientId import ClientId
from ...domain.ClientType import ClientType
from ...domain.ClientName import ClientName
from ...domain.ClientEmail import ClientEmail
from ...domain.ClientAddress import ClientAddress
from ...domain.ClientPhone import ClientPhone
from ...domain.ClientIsActive import ClientIsActive
from ...domain.ClientCreatedAt import ClientCreatedAt

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