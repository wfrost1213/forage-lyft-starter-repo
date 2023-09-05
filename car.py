from engine import *
from battery import *


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service


class CarFactory(ABC):

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
