from typing import Protocol, runtime_checkable
from Client import Client
from ClientId import ClientId

@runtime_checkable
class ClientRepository(Protocol):
    def create(self, client: Client) -> None:
        """
        Persists a new client in the repository.

        Args:
            client (Client): The client object to be created and stored in the repository.
        """
        pass

    def get_one_by_id(self, id: ClientId) -> Client | None:
        """
        Retrieves a client from the repository using the provided client ID.

        Args:
            id (ClientId): The unique identifier of the client to be retrieved.

        Returns:
            Client | None: The client object if found, otherwise None.
        """
        pass 

    def get_all(self) -> list[Client]:
        """
        Retrieves all clients from the repository.

        Returns:
            list[Client]: A list of client objects.
        """
        pass  
    
    def edit(self, client: Client) -> None:
        """
        Edits a client in the repository.

        Args:
            client (Client): The client object with the updated information.
        """
        pass
    
    def delete(self, client: Client) -> None:
        """
        Deletes a client from the repository.

        Args:
            client (Client): The client object to be deleted from the repository.
        """        
        pass
