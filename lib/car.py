from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

benz= Car("60cm radius", 4)
print (benz.wheel_size)
print(benz.wheel_number)