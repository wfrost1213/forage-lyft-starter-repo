import unittest
from datetime import datetime
from car import *


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        calliope = car_factory.create_calliope(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)

        self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        calliope = car_factory.create_calliope(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)

        self.assertFalse(calliope.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        calliope = car_factory.create_calliope(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertTrue(calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        calliope = car_factory.create_calliope(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertFalse(calliope.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear_levels = [0.2, 0.4, 0.8, 0.9]

        car_factory = CarFactory()
        calliope = car_factory.create_calliope(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertTrue(calliope.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        calliope = car_factory.create_calliope(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertFalse(calliope.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        glissade = car_factory.create_glissade(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertTrue(glissade.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        glissade = car_factory.create_glissade(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertFalse(glissade.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        glissade = car_factory.create_glissade(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertTrue(glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        glissade = car_factory.create_glissade(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertFalse(glissade.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear_levels = [1, 1, 1, 0.2]

        car_factory = CarFactory()
        glissade = car_factory.create_glissade(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertTrue(glissade.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear_levels = [0.4, 0.3, 0.1, 0.2]

        car_factory = CarFactory()
        glissade = car_factory.create_glissade(today, last_service_date, last_service_mileage, current_mileage, tire_wear_levels)
        self.assertFalse(glissade.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear_levels)
        self.assertTrue(palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear_levels)
        self.assertFalse(palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear_levels)
        self.assertTrue(palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear_levels)
        self.assertFalse(palindrome.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear_levels = [0.9, 1, 0.2, 0.6]

        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear_levels)
        self.assertTrue(palindrome.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear_levels)
        self.assertFalse(palindrome.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertFalse(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertTrue(rorschach.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertFalse(rorschach.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [1, 0.8, 1, 0.5]

        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertTrue(rorschach.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertFalse(rorschach.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertTrue(thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertFalse(thovex.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertTrue(thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertFalse(thovex.needs_service())

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear_levels = [0.9, 1, 0.8, 0.7]

        car_factory = CarFactory()
        thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertTrue(thovex.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear_levels = [0, 0, 0, 0]

        car_factory = CarFactory()
        thovex = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear_levels)
        self.assertFalse(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()
