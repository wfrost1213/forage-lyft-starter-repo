from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class SpindleBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        years = self.current_date - self.last_service_date.year
        return years > 2


class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        years = self.current_date - self.last_service_date.year
        return years > 4
