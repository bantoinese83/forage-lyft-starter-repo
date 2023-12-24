from datetime import datetime
from car import Car


class Calliope(Car):
    def __init__(self, last_service_date, engine, battery):
        super().__init__(last_service_date, engine, battery)
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date() or self.engine.needs_service() or self.battery.needs_service()
