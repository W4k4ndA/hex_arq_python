class ClientName: 
    def __init__(self, value: str):
        self.value = value.capitalize()
        self.__ensure_value_is_valid(value)
        
        
    def __ensure_value_is_valid(self, value: str):
        if not value:
            raise ValueError('El nombre del cliente no puede estar vacio')
        if len(value) < 3:
            raise ValueError('El nombre del cliente debe tener al menos 3 caracteres')
        if len(value) > 60:
            raise ValueError('El nombre del cliente debe tener menos de 60 caracteres')
    