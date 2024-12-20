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
        """
        Constructor de la clase ClientCreate.
        
        @param repository: objeto que implementa la interfaz ClientRepository. 
        """
        self.__repository = repository
    
    def run(self, id: str, type: bool, name: str, email: str, address: str, phone: str, created_at: datetime, is_active: bool) -> None:
        """
        Crea un nuevo cliente en el repositorio.
        
        @param id (str): El identificador unico del cliente.
        @param type (bool): El tipo de cliente.
        @param name (str): El nombre del cliente.
        @param email (str): El correo electronico del cliente.
        @param address (str): La direccion del cliente.
        @param phone (str): El numero de telefono del cliente.
        @param created_at (datetime): La fecha de creacion del cliente.
        @param is_active (bool): Un flag que indica si el cliente esta activo.
        
        @return None
        """
        client = Client(ClientId(id), 
                        ClientType(type),
                        ClientName(name), 
                        ClientEmail(email),
                        ClientAddress(address),
                        ClientPhone(phone),
                        ClientCreatedAt(created_at),
                        ClientIsActive(is_active))
        return self.__repository.create(client)