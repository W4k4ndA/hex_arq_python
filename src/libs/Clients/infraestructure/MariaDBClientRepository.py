
from ..domain import ClientName, ClientType
from ..domain.Client import Client
from ..domain.ClientAddress import ClientAddress
from ..domain.ClientEmail import ClientEmail
from ..domain.ClientId import ClientId
from ..domain.ClientPhone import ClientPhone
from ..domain.ClientRepository import ClientRepository
from sqlalchemy import create_engine, text, Row


class MariaDBClientRepository(ClientRepository):
    def __init__(self, connection_string: str) -> None:
        """
        Initializes a MariaDBClientRepository object with a connection string.

        Args:
            connection_string (str): A valid connection string to a MariaDB database.
            The connection string should be in the format "mysql://<username>:<password>@<host>:<port>/<database>"
        """
        
        self.__engine_url = connection_string    
        self.__engine = create_engine(self.__engine_url)
        
    
    def create(self, client: Client):
        """
        Persists a new client in the database.

        Args:
            client (Client): The client object to be created and stored in the repository.
        """
        self.__connection = self.__engine.connect()
        query = text("INSERT INTO clients (id, type, name, email, address, phone) VALUES(:id, :type, :name, :email, :address, :phone)")
        params = {"id": client.id.value, "type": client.type.value, "name": client.name.value, "email": client.email.value, "address": client.address.value, "phone": client.phone.value}
        self.__connection.execute(query,params)
        self.__connection.close()
    
    def get_all(self) -> list[Client]:
        """
        Retrieves all clients from the MariaDB database.

        Returns:
            list[Client]: A list of Client objects representing all clients in the database.
        """
        self.__connection = self.__engine.connect()
        query = text("SELECT * FROM clients")
        result = self.__connection.execute(query)
        rows = result.fetchall()
        self.__connection.close()
        return [self.__map_to_domain(row) for row in rows]
        # return [Client(ClientId(row[0]), ClientType(row[1]), ClientName(row[2]), ClientEmail(row[3]), ClientAddress(row[4]), ClientPhone(row[5])) for row in rows]
    
    def get_one_by_id(self, id: ClientId) -> Client | None:
        """
        Retrieves a client from the MariaDB database using the provided client ID.

        Args:
            id (ClientId): The unique identifier of the client to be retrieved.

        Returns:
            Client | None: The client object if found, otherwise None.
        """
        self.__connection = self.__engine.connect()
        query = text("SELECT * FROM clients WHERE id = :id")
        params = {"id": id.value}
        result = self.__connection.execute(query, params)
        row = result.fetchone()
        self.__connection.close()
        if row is None:
            return None
        else:
            return self.__map_to_domain(row)
            # return Client(ClientId(row[0]), ClientType(row[1]), ClientName(row[2]), ClientEmail(row[3]), ClientAddress(row[4]), ClientPhone(row[5]))
        
    
    def delete(self, client: Client)-> None:
        """
        Deletes a client from the MariaDB database.

        Args:
            client (Client): The client object to be deleted, identified by its unique ID.
        """
        self.__connection = self.__engine.connect()
        query = text("DELETE FROM clients WHERE id = :id")
        params = {"id": client.id.value}
        self.__connection.execute(query, params)
        self.__connection.close()
            
    
    def edit(self, client: Client)-> None:
        """
        Edits a client in the repository.

        Args:
            client (Client): The client object with the updated information.
        """
        
        self.__connection = self.__engine.connect()
        query = text("UPDATE clients SET type = :type, name = :name, email = :email, address = :address, phone = :phone WHERE id = :id")
        params = {"type": client.type.value, "name": client.name.value, "email": client.email.value, "address": client.address.value, "phone": client.phone.value, "id": client.id.value}
        self.__connection.execute(query, params)
        self.__connection.close()
        
        
        
        
    def __map_to_domain(self, row: Row) -> Client:
        """
        Maps a row from the MariaDB database to a Client object.

        Args:
            row: A tuple containing the values of a row in the clients table.

        Returns:
            Client: A Client object with the values from the row.
        """
        return Client(ClientId(row[0]), ClientType(row[1]), ClientName(row[2]), ClientEmail(row[3]), ClientAddress(row[4]), ClientPhone(row[5]))        
