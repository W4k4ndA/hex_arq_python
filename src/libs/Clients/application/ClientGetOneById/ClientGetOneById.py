from ...domain.ClientRepository import ClientRepository
from ...domain.ClientId import ClientId
from ...domain.Client import Client
from ...domain.ClientNotFoundError import ClientNotFoundError

class ClientGetOneById:
    def __init__(self, repository: ClientRepository):
        self.__repository = repository
    
    def run(self, id: str) -> Client:
        
        client = self.__repository.get_one_by_id(ClientId(id))
        
        if not client:
            raise ClientNotFoundError('El cliente no existe')
        
        return client




