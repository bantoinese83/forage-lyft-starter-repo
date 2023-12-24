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
    def create_calliope(last_service_date: date, current_mileage: int):
        engine = SternmanEngine(False)  # Initialize with warning_light_is_on = False
        battery = NubbinBattery(last_service_date)
        return Calliope(last_service_date, engine, battery)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Glissade(last_service_date, engine)

    @staticmethod
    def create_palindrome(last_service_date: date, current_mileage: int):
        engine = SternmanEngine(False)  # Initialize with warning_light_is_on = False
        return Palindrome(last_service_date, engine)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Rorschach(last_service_date, engine)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Thovex(last_service_date, engine)

    @staticmethod
    def create_car(car_type: str, last_service_date: date, current_mileage: int, last_service_mileage: int):
        if car_type == 'Calliope':
            return CarFactory.create_calliope(last_service_date, current_mileage)
        elif car_type == 'Glissade':
            return CarFactory.create_glissade(last_service_date, current_mileage, last_service_mileage)
        elif car_type == 'Palindrome':
            return CarFactory.create_palindrome(last_service_date, current_mileage)
        elif car_type == 'Rorschach':
            return CarFactory.create_rorschach(last_service_date, current_mileage, last_service_mileage)
        elif car_type == 'Thovex':
            return CarFactory.create_thovex(last_service_date, current_mileage, last_service_mileage)
        else:
            raise ValueError('Unknown car type')
