from datetime import date, datetime
from engine.battery.nubbin_battery import NubbinBattery
from engine.sternman_engine import SternmanEngine
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Calliope:
    def __init__(self, last_service_date: date, engine: SternmanEngine, battery: NubbinBattery, tire_wear: list):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery
        self.tire_wear = tire_wear

    def needs_service(self):
        try:
            service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
            tire_service = any(wear >= 0.9 for wear in self.tire_wear)
            return service_threshold_date < datetime.today().date() or self.engine.needs_service() or tire_service
        except Exception as e:
            logger.error(f"An error occurred in needs_service: {e}")
            raise

