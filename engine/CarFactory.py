from datetime import date
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, tire_type: str):
        engine = SternmanEngine(False)  # Initialize with warning_light_is_on = False
        battery = NubbinBattery(last_service_date)
        tire_wear = [0.0, 0.0, 0.0, 0.0]
        return Calliope(last_service_date, engine, battery, tire_wear, tire_type)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tire_wear = [0.0, 0.0, 0.0, 0.0]
        return Glissade(last_service_date, engine, battery, tire_wear, tire_type)

    @staticmethod
    def create_palindrome(last_service_date: date, current_mileage: int, tire_type: str):
        engine = SternmanEngine(False)  # Initialize with warning_light_is_on = False
        battery = NubbinBattery(last_service_date)  # Initialize the battery
        tire_wear = [0.0, 0.0, 0.0, 0.0]
        return Palindrome(last_service_date, engine, battery, tire_wear, tire_type)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tire_wear = [0.0, 0.0, 0.0, 0.0]
        return Rorschach(last_service_date, engine, current_mileage, last_service_mileage, tire_wear, tire_type)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str):
        engine = SternmanEngine(False)
        return Thovex(last_service_date, engine, current_mileage, last_service_mileage, tire_type)

    @staticmethod
    def create_car(car_type: str, last_service_date: date, current_mileage: int, last_service_mileage: int,
                   tire_type: str):
        if car_type == 'Calliope':
            return CarFactory.create_calliope(last_service_date, current_mileage, tire_type)
        elif car_type == 'Glissade':
            return CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage, tire_type)
        elif car_type == 'Palindrome':
            return CarFactory.create_palindrome(last_service_date, current_mileage, tire_type)
        elif car_type == 'Rorschach':
            return CarFactory.create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_type)
        elif car_type == 'Thovex':
            return CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage, tire_type)
        else:
            raise ValueError('Unknown car type')
