class ClientAddress:
    def __init__(self, value: str):
        self.value = value
        self.__ensure_value_is_valid(value)

    def __ensure_value_is_valid(self, value: str):
        if not value:
            raise ValueError('La dirección del cliente no puede estar vacia')
        if len(value > 200):
            raise ValueError('La dirección del cliente debe tener menos de 300 caracteres')