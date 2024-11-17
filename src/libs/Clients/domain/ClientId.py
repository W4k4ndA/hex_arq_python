class ClientId:
    def __init__(self, value: str):
                
        """
        Initializes a ClientId object with a value.

        Args:
            value (str): The id of the client. It must be a non-empty string with at least 5 characters.

        Raises:
            ValueError: If the value is empty or has less than 5 characters.
        """
        self.value = value
        self.__ensure_value_is_valid(self.value)
        
    def __ensure_value_is_valid(self, value: str):
        """
        Validates the value of the ClientId object.

        Args:
            value (str): The value to be validated.

        Raises:
            ValueError: If the value is empty or has less than 5 characters.
        """
        if not value:
            raise ValueError('El id del cliente no puede estar vacio')
        if len(value) < 5:
            raise ValueError('El id del cliente debe tener al menos 5 caracteres')