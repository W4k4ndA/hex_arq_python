import datetime

class ClientCreatedAt:
    def __init__(self, value: datetime):
        self.value = value
        self.__ensure_value_is_valid(value)
        
    def __ensure_value_is_valid(self, value: datetime):
        if not value:
            raise ValueError('La fecha de creación del cliente no puede estar vacia')    
        if value > datetime.datetime.now():
            raise ValueError('La fecha de creación del cliente no puede ser futura')