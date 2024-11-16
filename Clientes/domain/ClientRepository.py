from typing import Protocol, runtime_checkable
from Client import Client
from ClientId import ClientId

@runtime_checkable
class ClientRepository(Protocol):
    def create(self, client: Client) -> None:
        pass

    def get_one_by_id(self, id: ClientId) -> Client | None:
        pass 

    def get_all(self) -> list[Client]:
        pass  
    
    def edit(self, client: Client) -> None:
        pass
    
    def delete(self, client: Client) -> None:
        pass
