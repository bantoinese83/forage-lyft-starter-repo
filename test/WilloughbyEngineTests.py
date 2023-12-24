import unittest
from engine.willoughby_engine import WilloughbyEngine


class WilloughbyEngineTests(unittest.TestCase):
    def test_should_return_true_when_current_mileage_exceeds_last_service_mileage_by_10000(self):
        engine = WilloughbyEngine(20000, 10000)
        self.assertTrue(engine.needs_service())

    def test_should_return_false_when_current_mileage_is_equal_to_last_service_mileage(self):
        engine = WilloughbyEngine(10000, 10000)
        self.assertFalse(engine.needs_service())

    def test_should_return_false_when_current_mileage_is_less_than_last_service_mileage_by_10000(self):
        engine = WilloughbyEngine(15000, 10000)
        self.assertFalse(engine.needs_service())

    def test_should_return_false_when_current_mileage_is_0(self):
        engine = WilloughbyEngine(0, 10000)
        self.assertFalse(engine.needs_service())

    def test_should_return_false_when_current_mileage_is_less_than_10000(self):
        engine = WilloughbyEngine(9999, 10000)
        self.assertFalse(engine.needs_service())
