from engine import *
from battery import *
from tires import *
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    @abstractmethod
    def needs_service(self) -> bool:
        engine_service = self.engine.needs_service()
        battery_service = self.battery.needs_service()
        tires_service = self.tires.needs_service()
        return battery_service or engine_service or tires_service


class CarFactory(ABC):

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_levels) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear_levels)
        return Car(engine, battery, tires)

    def create_glissade(self, current_date, last_service_date, last_service_mileage, current_mileage, tire_wear_levels) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear_levels)
        return Car(engine, battery, tires)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear_levels) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear_levels)
        return Car(engine, battery, tires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_levels) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear_levels)
        return Car(engine, battery, tires)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_levels) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear_levels)
        return Car(engine, battery, tires)
