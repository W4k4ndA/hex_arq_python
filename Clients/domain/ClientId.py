class ClientId:
    def __init__(self, value: str):
        self.value = value
        self.__ensure_value_is_valid(value)
        
    def __ensure_value_is_valid(self, value: str):
        if not value:
            raise ValueError('El id del cliente no puede estar vacio')
        if len(value) < 5:
            raise ValueError('El id del cliente debe tener al menos 5 caracteres')

