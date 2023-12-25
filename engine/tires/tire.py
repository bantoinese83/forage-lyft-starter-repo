# Import the Serviceable class
from abc import ABC

from serviceable import Serviceable


class Tire(Serviceable, ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear


# Implement the CarriganTire class
class CarriganTire(Tire):
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear)


# Implement the OctoprimeTire class
class OctoprimeTire(Tire):
    def needs_service(self):
        return sum(self.tire_wear) >= 3
