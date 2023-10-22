from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
      
    def needs_service(self):
        if  self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False

    @abstractmethod
    def needs_service(self):
        pass
