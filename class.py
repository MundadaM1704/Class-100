class Car(object):
    """
    bluePrint for car
    """

    def __init__(self, model, colour, company, speed_limit):
        self.colour = colour
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("Started")

    def stop(self):
        print("Stoped")

    def accelarate(self):
        print("Accelarating...")

    def change_gear(self, gear_type):
        print("Gear Changed")

audi = Car("A6","red","audi",80)
print(audi.colour)