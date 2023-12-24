import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from engine.battery.spindler_battery import SpindlerBattery
from engine.battery.nubbin_battery import NubbinBattery


class TestBatteryAndEngine(unittest.TestCase):

    def test_thovex_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(9999, 1)
        car = Thovex(last_service_date, engine, 1, 1)

        self.assertFalse(car.needs_service())

    def test_rorschach_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = CapuletEngine(9999, 1)
        car = Rorschach(last_service_date, engine, 1, 1)

        self.assertFalse(car.needs_service())

    def test_glissade_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(10000, 1)
        car = Glissade(last_service_date, engine, 1, 1)
        self.assertFalse(car.needs_service())

    def test_calliope_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        engine = SternmanEngine(False)  # Initialize with warning_light_is_on = False
        battery = NubbinBattery(last_service_date)

        car = Calliope(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_calliope_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        engine = SternmanEngine(False)  # Initialize with warning_light_is_on = False
        battery = NubbinBattery(last_service_date)

        car = Calliope(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_calliope_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = SternmanEngine(True)  # Initialize with warning_light_is_on = True
        battery = NubbinBattery(last_service_date)

        car = Calliope(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_calliope_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = SternmanEngine(False)
        battery = NubbinBattery(last_service_date)

        car = Calliope(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_palindrome_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = SternmanEngine(True)
        car = Palindrome(last_service_date, engine)

        self.assertTrue(car.needs_service())

    def test_palindrome_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        engine = SternmanEngine(False)
        car = Palindrome(last_service_date, engine)

        self.assertFalse(car.needs_service())

    def test_nubbin_battery_does_not_need_service_when_last_service_date_is_less_than_4_years_ago(self):
        last_service_date = datetime.today().date().replace(year=datetime.today().year - 3)
        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_needs_service_when_last_service_date_is_more_than_4_years_ago(self):
        last_service_date = datetime.today().date().replace(year=datetime.today().year - 5)
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_sternman_engine_needs_service_when_warning_light_is_on(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_does_not_need_service_when_warning_light_is_off(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

    def test_glissade_engine_does_not_need_service_when_current_mileage_is_less_than_10000_miles_since_last_service(
            self):
        engine = WilloughbyEngine(9999, 1)
        self.assertFalse(engine.needs_service())

    def test_glissade_engine_does_not_need_service_when_current_mileage_is_equal_to_10000_miles_since_last_service(
            self):
        engine = WilloughbyEngine(10000, 1)
        self.assertFalse(engine.needs_service())

    def test_glissade_engine_does_not_need_service_when_current_mileage_is_equal_to_0_miles_since_last_service(self):
        engine = WilloughbyEngine(0, 1)
        self.assertFalse(engine.needs_service())

    def test_spindler_battery_does_not_need_service_when_last_service_date_is_less_than_2_years_ago(self):
        last_service_date = datetime.today().date().replace(year=datetime.today().year - 1)
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_needs_service_when_last_service_date_is_more_than_2_years_ago(self):
        last_service_date = datetime.today().date().replace(year=datetime.today().year - 3)
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_willoughby_engine_does_not_need_service_when_current_mileage_is_less_than_10000_miles_since_last_service(
            self):
        engine = WilloughbyEngine(current_mileage=9999, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_does_not_need_service_when_current_mileage_is_0_miles_since_last_service(self):
        engine = WilloughbyEngine(current_mileage=0, last_service_mileage=0)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
