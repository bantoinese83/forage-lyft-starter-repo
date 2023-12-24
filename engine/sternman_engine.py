from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Engine(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
