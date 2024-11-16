class ClientPhone:
    def __init__(self, value: str):
        """
        Initializes a ClientPhone object with a value.

        Args:
            value (str): The phone number of the client. It must be a non-empty string with only numeric characters.

        Raises:
            ValueError: If the value is empty or has non-numeric characters.
        """
        self.value = value
        self.__ensure_value_is_valid(value)
    
    def __ensure_value_is_valid(self, value: str):
        """
        Verifies that the value of the ClientPhone object is valid.

        Args:
            value (str): The value to be validated.

        Raises:
            ValueError: If the value is empty or has non-numeric characters.
        """
        if not value:
            raise ValueError('El telefono del cliente no puede estar vacio')
        if not value.isnumeric():
            raise ValueError('El telefono del cliente debe ser numerico. No debe tener espacios en blanco, ni letras, ni caracteres especiales')