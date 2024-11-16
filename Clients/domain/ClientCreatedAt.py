import datetime

class ClientCreatedAt:
    def __init__(self, value: datetime):
        """
        Inicializa la clase ClientCreatedAt con un valor de fecha y hora.
        
        Args:
            value (datetime): La fecha y hora de creación del cliente. Debe ser una instancia de datetime.
        """
        self.value = value
        self.__ensure_value_is_valid(value)
        
    def __ensure_value_is_valid(self, value: datetime):
        """
        Verifica que el valor sea válido.
        
        Args:
            value (datetime): La fecha y hora de creación del cliente. Debe ser una instancia de datetime.
        
        Raises:
            ValueError: Si el valor es inválido.
        """
        if not value:
            raise ValueError('La fecha de creación del cliente no puede estar vacia')    
        if value > datetime.datetime.now():
            raise ValueError('La fecha de creación del cliente no puede ser futura')