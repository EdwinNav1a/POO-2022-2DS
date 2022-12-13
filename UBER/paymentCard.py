from payment import Payment

class PaymentCard(Payment):
    cuenta = int
    banco  = str
    datoTarjeta = []
    
    def __init__(self, id, valor, cuenta, fecha, banco, datoTarjeta):
        super().__init__(id, valor, fecha)
        self.cuenta = cuenta
        self.banco =banco
        self.datoTarjeta =datoTarjeta
        