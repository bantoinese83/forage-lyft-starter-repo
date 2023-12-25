from datetime import datetime
from car import Car
from engine import battery
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Palindrome(Car):
    def __init__(self, last_service_date, engine, tire_wear):
        super().__init__(last_service_date, engine, battery)
        self.engine = engine
        self.tire_wear = tire_wear

    def needs_service(self):
        try:
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
            tire_service = any(wear >= 0.9 for wear in self.tire_wear)
            return service_threshold_date < datetime.today().date() or self.engine.needs_service() or tire_service
        except Exception as e:
            logger.error(f"An error occurred in needs_service: {e}")
            raise
