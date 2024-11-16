
class ClientNotFoundError(Exception):
    
    def __init__(self, message: str):
        """
        Initializes a new instance of ClientNotFoundError with a message.

        Args:
            message (str): The error message.
        """

        self.message = message    
        super().__init__(message)