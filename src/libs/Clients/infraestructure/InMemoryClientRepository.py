
from ..domain.Client import Client
from ..domain.ClientId import ClientId
from ..domain.ClientRepository import ClientRepository


class InmemoryClientRepository(ClientRepository):
    def __init__(self):
        """
        Initializes a new instance of the InmemoryClientRepository class.

        This constructor initializes an empty list of clients.
        """
        self.__clients = []

    def create(self, client: Client):
        """
        Persists a new client in the repository.

        Args:
            client (Client): The client object to be created and stored in the repository.
        """
        self.__clients.append(client)

    def get_one_by_id(self, id: ClientId) -> Client | None:
                
        """
        Retrieves a client from the repository using the provided client ID.

        Args:
            id (ClientId): The unique identifier of the client to be retrieved.

        Returns:
            Client | None: The client object if found, otherwise None.
        """
        for client in self.__clients:
            if client.id.value == id.value:
                return client        
        return None

    def get_all(self) -> list[Client]:
        """
        Retrieves all clients from the in-memory repository.

        Returns:
            list[Client]: A list of all client objects stored in the repository.
        """
        return self.__clients

    def edit(self, client: Client) -> None:
        self.__clients[self.__clients.index(client)] = client
        index = [i for i, x in enumerate(self.__clients) if x.id.value == client.id.value]
        self.__clients[index[0]] = client
        
        
    def delete(self, client: Client) -> None:
        self.__clients.remove(client)   

