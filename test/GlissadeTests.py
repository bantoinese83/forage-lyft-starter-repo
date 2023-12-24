import unittest
from datetime import datetime

from engine.model.glissade import Glissade
from engine.willoughby_engine import WilloughbyEngine


class GlissadeTests(unittest.TestCase):

    def test_should_return_true_when_current_mileage_exceeds_threshold(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(9000, 1)
        car = Glissade(last_service_date, engine, 20000, 9000)

        self.assertTrue(car.needs_service())

    def test_should_raise_exception_when_error_occurs_in_needs_service(self):
        last_service_date = datetime.today().date()
        engine = WilloughbyEngine(9000, 1)
        car = Glissade(last_service_date, engine, "invalid", 9000)

        with self.assertRaises(Exception):
            car.needs_service()


if __name__ == '__main__':
    unittest.main()
