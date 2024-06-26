# Factory Method Pattern Example in Python
class Car:
    def __init__(self, model):
        self.model = model

class CarFactory:
    @staticmethod
    def create_car(model):
        return Car(model)

if __name__ == "__main__":
    my_car = CarFactory.create_car('Tesla Model 3')
    print(my_car.model)  # Tesla Model 3
