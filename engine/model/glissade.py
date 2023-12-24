import logging
from car import Car
from engine import battery

# Create a logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Glissade(Car):
    def __init__(self, last_service_date, engine, current_mileage, last_service_mileage):
        super().__init__(last_service_date, engine, battery)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = engine

    def needs_service(self):
        try:
            # Calculate the service threshold mileage
            service_threshold_mileage = self.last_service_mileage + 10000  # Adjust based on your scenario
            needs_service = self.engine.needs_service() or self.current_mileage >= service_threshold_mileage
            logger.info(f"Service needed: {needs_service}")
            return needs_service
        except Exception as e:
            logger.error(f"An error occurred in needs_service: {e}")
            raise
