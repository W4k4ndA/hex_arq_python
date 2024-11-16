
from Clients.application.ClientCreate.ClientCreate import ClientCreate
from Clients.application.ClientDelete.ClientDelete import ClientDelete
from Clients.application.ClientEdit.ClientEdit import ClientEdit
from Clients.application.ClientGetAll.ClientGetAll import ClientGetAll
from Clients.application.ClientGetOneById.ClientGetOneById import ClientGetOneById
from Clients.application.ClientGetAll.ClientGetAll import ClientGetAll
from Clients.infraestructure.InMemoryClientRepository import InMemoryClientRepository


clientRepository = InMemoryClientRepository()

ServiceContainer = {
    "client":{
        "get_one_by_id": ClientGetOneById(clientRepository),
        "get_all": ClientGetAll(clientRepository),
        "create": ClientCreate(clientRepository),
        "edit": ClientEdit(clientRepository),
        "delete": ClientDelete(clientRepository)
    }
}



