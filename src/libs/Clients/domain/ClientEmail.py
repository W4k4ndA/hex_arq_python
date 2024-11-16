import re
class ClientEmail:
    def __init__(self, value: str):
        """
        Initializes a ClientEmail object with a value.

        Args:
            value (str): The email address of the client, which will be validated against a specific pattern.
        """
        self.value = value
        self.__ensure_value_is_valid(value)
        
    def __ensure_value_is_valid(self, value: str):
        """
        Verifies that the value matches the specific pattern of an email address.

        Args:
            value (str): The email address to be validated.

        Raises:
            ValueError: If the value does not match the pattern.
        """
        # This regular expression matches strings that have the format of an email address
        # with the following characteristics:
        # - A set of alphanumeric characters at the beginning.
        # - Optionally, an underscore (_) zero or more times.
        # - Optionally, a dot (.) zero or one time.
        # - A set of alphanumeric characters after the dot.
        # - Optionally, an underscore (_) zero or more times.
        # - The at symbol (@).
        # - A set of alphanumeric characters and hyphens after the @.
        # - A dot (.) literal.
        # - The string "com" literal at the end.
        regex = r"^[a-zA-Z0-9]+[_]*\.?[a-zA-Z0-9]+[_]*@[a-zA-Z0-9]+\.[com]$"
        if not re.match(regex, value):
            raise ValueError('El email del cliente no es válido')

