from car import Car

class UberConfort(Car):
    aceptado        = bool
    asientos        = int
    tapizado        = str
    
    def __init__(self, placa, modelo, color, año, Driver, aceptado, asiento, tapizado):
        super().__init__(placa, modelo, color, año, Driver)
        self.aceptado = aceptado
        self.asientos = asiento
        self.tapizado = tapizado