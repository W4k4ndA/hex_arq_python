import re
class ClientEmail:
    def __init__(self, value: str):
        self.value = value
        self.__ensure_value_is_valid(value)
        
    def __ensure_value_is_valid(self, value: str):
        

        """esta expresión regular coincide con cadenas que tengan el formato de una 
        dirección de correo electrónico con las siguientes características:
        Un conjunto de caracteres alfanuméricos al inicio.
        Opcionalmente, un guion bajo (_) cero o más veces.
        Opcionalmente, un punto (.) cero o una vez.
        Un conjunto de caracteres alfanuméricos después del punto.
        Opcionalmente, un guion bajo (_) cero o más veces.
        El símbolo @.
        Un conjunto de caracteres alfanuméricos y guiones después del @.
        Un punto (.) literal.
        La cadena "com" literal al final."""
        regex = r"^[a-zA-Z0-9]+[_]*\.?[a-zA-Z0-9]+[_]*@[a-zA-Z0-9]+\.[com]$"
        if not re.match(regex, value):
            raise ValueError('El email del cliente no es válido')
