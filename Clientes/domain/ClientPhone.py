class ClientPhone:
    def __init__(self, value: str):
        self.value = value
        self.__ensure_value_is_valid(value)
    
    def __ensure_value_is_valid(self, value: str):
        if not value:
            raise ValueError('El telefono del cliente no puede estar vacio')
        if not value.isnumeric():
            raise ValueError('El telefono del cliente debe ser numerico. No debe tener espacios en blanco, ni letras, ni caracteres especiales')