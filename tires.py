from abc import ABC, abstractmethod


class Tires(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class CarriganTires(Tires):

    def __init__(self, tire_wear_levels):
        self.tire_wear_levels = tire_wear_levels

    def needs_service(self) -> bool:
        return max(self.tire_wear_levels) >= 0.9


class OctoprimeTires(Tires):

    def __init__(self, tire_wear_levels):
        self.tire_wear_levels = tire_wear_levels

    def needs_service(self) -> bool:
        return sum(self.tire_wear_levels) >= 3
