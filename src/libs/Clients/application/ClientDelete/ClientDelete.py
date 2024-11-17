

from ...domain.ClientId import ClientId
from ...domain.ClientRepository import ClientRepository


class ClientDelete:
    def __init__(self, repository: ClientRepository):
        """
        Initializes a new instance of the ClientDelete class.

        Args:
            repository (ClientRepository): An object that implements the ClientRepository interface.
        """
        # Store the repository for later use in the class methods
        self.__repository = repository

    def run(self, id:str)->None:
        
        """
        Deletes a client from the repository.

        Args:
            id (str): The unique identifier of the client to be deleted.

        Returns:
            None
        """

        return self.__repository.delete(ClientId(id))