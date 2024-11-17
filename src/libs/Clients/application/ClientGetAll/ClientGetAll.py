from ...domain.ClientRepository import ClientRepository
from ...domain.Client import Client


class ClientGetAll:
    def __init__(self, repository: ClientRepository):
        """
        Initializes a new instance of the ClientGetAll class.

        Args:
            repository (ClientRepository): An object that provides access to client data.
        """
        self.__repository = repository
    
    def run(self) -> list[Client]:
        """
        Retrieves all clients from the repository.

        Returns:
            list[Client]: A list of Client objects, each representing a client.
        """
        return self.__repository.get_all()



