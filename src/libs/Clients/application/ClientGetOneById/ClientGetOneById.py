from ...domain.ClientRepository import ClientRepository
from ...domain.ClientId import ClientId
from ...domain.Client import Client
from ...domain.ClientNotFoundError import ClientNotFoundError

class ClientGetOneById:
    def __init__(self, repository: ClientRepository):
        """
        Initializes a new instance of the ClientGetOneById class.

        Args:
            repository (ClientRepository): An object that provides access to client data.
        """
        self.__repository = repository
    
    def run(self, id: str) -> Client:
        
        """
        Retrieves a client from the repository using the provided client ID.

        Args:
            id (str): The unique identifier of the client to be retrieved.

        Returns:
            Client: The client object if found, otherwise None.
        """
        client = self.__repository.get_one_by_id(ClientId(id))
        
        if not client:
            raise ClientNotFoundError('El cliente no existe')
        
        return client




