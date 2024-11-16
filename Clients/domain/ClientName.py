class ClientName: 
    def __init__(self, value: str):
        """
        Initializes a ClientName object with a capitalized value.

        Args:
            value (str): The name of the client, which will be capitalized and validated.
        """
        self.value = value.capitalize()
        self.__ensure_value_is_valid(value)
        
        
    def __ensure_value_is_valid(self, value: str):     
        """
        Validates the provided client name value.

        Args:
            value (str): The name of the client to validate.

        Raises:
            ValueError: If the value is empty, has fewer than 3 characters,
                        or exceeds 60 characters in length.
        """
        if not value:
            raise ValueError('El nombre del cliente no puede estar vacio')
        if len(value) < 3:
            raise ValueError('El nombre del cliente debe tener al menos 3 caracteres')
        if len(value) > 60:
            raise ValueError('El nombre del cliente debe tener menos de 60 caracteres')
    