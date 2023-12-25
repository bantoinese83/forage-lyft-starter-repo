from datetime import datetime
from serviceable import Serviceable


# Modify the SpindlerBattery class
class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return (datetime.today().date() - self.last_service_date).days >= 365 * 3  # Changed from 2 to 3 years
