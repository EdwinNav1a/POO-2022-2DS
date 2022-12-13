from pprint import pprint
from account import Account
from accountDriver import Driver
from accountUser import User
from car import Car 
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentTransfer import PaymentTransfer
from route import Route
from trip import Trip
from UberXL import UberXL
from UberConfort import UberConfort
from UberX import UberX

if __name__ == "__main__":
    usuario1 = User(1, "Alexander Pacho", "Masculino", 99999999, 20)
    print(vars(usuario1))
    
    usuario2 = User(2, "Alexander Pacho", "Masculino", 99999999, 39)
    print(vars(usuario2))
    
    uberX1 = UberX("XLX-5599", "Chevrolet Corse", "Gris", 2018, Driver(5, "Alexander Pacho", "Masculino", 999999, 20, "Tipo C"))
    print(vars(uberX1))
    