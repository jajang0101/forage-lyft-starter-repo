class Octoprime:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.tire_worn = [0, 0, 0, 0]
    def tire_should_be_serviced(self):
        result = False
        sum1 = 0
        for i in range(4):
            sum += self.tire.worn[i]
           
        if (sum1 >= 3):
                result = True
        return result
