

from ...domain.ClientId import ClientId
from ...domain.ClientRepository import ClientRepository


class ClientDelete:
    def __init__(self, repository: ClientRepository):
        """
        Constructor de la clase ClientDelete.
        
        @param repository: objeto que implementa la interfaz ClientRepository. 
        """
        self.__repository = repository

    def run(self, id:str)->None:
        
        return self.__repository.delete(ClientId(id))