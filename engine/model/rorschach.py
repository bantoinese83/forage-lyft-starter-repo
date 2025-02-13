import logging

from car import Car
from engine import battery

# Create a logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Rorschach(Car):
    def __init__(self, last_service_date, engine, current_mileage, last_service_mileage, tire_wear):
        super().__init__(last_service_date, engine, battery)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = engine
        self.tire_wear = tire_wear

    def needs_service(self):
        try:
            service_threshold_mileage = self.last_service_mileage + 10000  # Adjust based on your scenario
            tire_service = any(wear >= 0.9 for wear in self.tire_wear)
            return self.engine.needs_service() or self.current_mileage >= service_threshold_mileage or tire_service
        except Exception as e:
            logger.error(f"An error occurred in needs_service: {e}")
            raise
