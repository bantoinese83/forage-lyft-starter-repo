import unittest
from datetime import datetime

from engine.model.thovex import Thovex
from engine.willoughby_engine import WilloughbyEngine


class ThovexTests(unittest.TestCase):
    def test_should_return_true_when_current_mileage_exceeds_threshold(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(9000, 1)
        car = Thovex(last_service_date, engine, 20000, 9000)

        self.assertTrue(car.needs_service())

    def test_should_return_false_when_engine_does_not_need_service_and_current_mileage_is_below_threshold(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(9000, 1)
        car = Thovex(last_service_date, engine, 19000, 9000)

        self.assertFalse(car.needs_service())

    def test_should_raise_exception_when_error_occurs_in_needs_service(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(9000, 1)
        car = Thovex(last_service_date, engine, "invalid", 9000)

        with self.assertRaises(Exception):
            car.needs_service()

    def test_should_return_false_when_current_mileage_is_0(self):
        engine = WilloughbyEngine(0, 10000)
        car = Thovex(datetime.today().date(), engine, 0, 10000)
        self.assertFalse(car.needs_service())

    def test_should_return_false_when_current_mileage_is_less_than_10000(self):
        engine = WilloughbyEngine(9999, 10000)
        car = Thovex(datetime.today().date(), engine, 9999, 10000)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
