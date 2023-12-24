from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        """
        Determines if the component needs service.
        Returns:
            bool: True if the component needs service, False otherwise.
        """
        pass
