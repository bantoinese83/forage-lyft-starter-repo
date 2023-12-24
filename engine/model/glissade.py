from datetime import datetime
from car import Car
from engine import battery


class Glissade(Car):
    def __init__(self, last_service_date, engine):
        super().__init__(last_service_date, engine, battery)
        self.engine = engine

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date() or self.engine.needs_service()
