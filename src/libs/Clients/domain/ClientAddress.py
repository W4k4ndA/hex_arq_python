class ClientAddress:
    def __init__(self, value: str):
        """
        Initializes a ClientAddress object with a value.

        Args:
            value (str): The address of the client. It must be a non-empty string with less than 200 characters.
        """
        self.value = value
        self.__ensure_value_is_valid(value)

    def __ensure_value_is_valid(self, value: str):
                
        """
        Validates the value of the ClientAddress object.

        Args:
            value (str): The value to be validated.

        Raises:
            ValueError: If the value is empty or has more than 200 characters.
        """
        if not value:
            raise ValueError('La dirección del cliente no puede estar vacia')
        if len(value > 200):
            raise ValueError('La dirección del cliente debe tener menos de 300 caracteres')