from Clients.domain.ClientRepository import ClientRepository
from Clients.domain.Client import Client


class ClientGetAll:
    def __init__(self, repository: ClientRepository):
        self.__repository = repository
    
    def run(self) -> list[Client]:
        return self.__repository.get_all()



