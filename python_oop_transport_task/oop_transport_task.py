"""Task Transport"""
from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Base abstract class
    """
    using_type = 'Personnel'

    def __init__(self, manufacturer, tank_fullness, moves_with):
        self.manufacturer = manufacturer
        self.tank_fullness = tank_fullness
        self.moves_with = moves_with

    def __bool__(self) -> bool:
        """:returns tank fullness"""
        return self.tank_fullness

    def __del__(self):
        """delete info about your example"""
        self.manufacturer = None
        self.tank_fullness = None
        self.moves_with = None

    @abstractmethod
    def __dict__(self):
        """This method for output info of your vehicle"""

    @abstractmethod
    def _good_manufacturer(self):
        """another script method"""

    @abstractmethod
    def _many_horses(self):
        """another script method"""

    @staticmethod
    def _fly_into_a_pole():
        """method for loose"""
        return "You decayed :("

    def refuel(self):
        """fill your fuel tank"""
        print(self.__dict__())
        self.tank_fullness = True


class Engine(ABC):
    """Class to explain your engine`s power"""
    energy_type = 'ICE'
    fuel_type = 'Gasoline'

    def __init__(self, horse_powers):
        self.horse_powers = horse_powers

    @staticmethod
    def __call__():
        Engine._engine_start()

    def __del__(self):
        self.horse_powers = None

    def __sizeof__(self) -> str:
        return f"This vehicle has {self.horse_powers} horses in!"

    @classmethod
    def _engine_start(cls):
        print('R r r r r r r r r r r r r r r r r r r r r')


class Moto(Transport, Engine):
    """Motorbike class"""

    def __init__(self, manufacturer, tank_fullness, moves_with, horse_powers, wheels_amount):
        Transport.__init__(self, manufacturer, tank_fullness, moves_with)
        Engine.__init__(self, horse_powers)
        self.wheels_amount = wheels_amount

    def __call__(self):
        Moto._engine_start()
        Moto.fly_into_the_sunset(self)

    def __dict__(self):

        if self.tank_fullness:
            return (f"Your {self.manufacturer} with {self.wheels_amount}"
                    f" {self.moves_with} and {self.horse_powers} horses in engine"
                    f"Fulfilled")
        return "Empty"

    def __del__(self):
        Transport.__del__(self)
        Engine.__del__(self)
        self.wheels_amount = None

    @classmethod
    def _engine_start(cls):
        print('Ur ur ur ur ur ur ur ur ur ur ur ur ur ur ur ur ur ur ur ur')

    def fly_into_the_sunset(self):
        """method to run script"""
        return Moto._many_horses(self) if self.__bool__() else print("fill the tank")

    def _many_horses(self):
        if self.horse_powers >= 60:
            print(Moto._good_manufacturer(self))
        else:
            print(Moto._fly_into_a_pole())

    def _good_manufacturer(self):
        if self.manufacturer == 'Harley Davidson':
            return "Going to the run, run angel\n"  # Golden Earring - Going to the run
        return "you are either a grandma or a stupid teenager"


class Car(Transport, Engine):
    """Car class"""

    def __init__(self, manufacturer, tank_fullness, moves_with, horse_powers, seats_amount):
        Transport.__init__(self, manufacturer, tank_fullness, moves_with)
        Engine.__init__(self, horse_powers)
        self.seats_amount = seats_amount

    def __call__(self):
        Car._engine_start()
        Car.fly_into_the_sunset(self)

    def __dict__(self):
        if self.tank_fullness:
            return (f"Your {self.manufacturer} with {self.seats_amount} seats "
                    f"with 4 {self.moves_with} and {self.horse_powers} horses in engine\n"
                    f"Fulfilled")
        return "Empty"

    def __del__(self):
        Transport.__del__(self)
        Engine.__del__(self)
        self.seats_amount = None

    def fly_into_the_sunset(self):
        """method to run script"""
        print(f"You can take {self.seats_amount - 1} friends with you!")
        return Car._many_horses(self) if self.__bool__() else print("fill the tank")

    def _many_horses(self):
        if self.horse_powers > 150:
            print(Car._good_manufacturer(self))
        else:
            print(Car._fly_into_a_pole())

    def _good_manufacturer(self):
        if self.manufacturer == 'Ford':
            return "Ride to Sunset\n"
        return "you are either a grandma or a stupid teenager"

    @classmethod
    def _engine_start(cls):
        print('Mr mr mr mr mr mr mr mr mr mr mr mr mr mr mr mr mr mr mr mr')


class Boat(Transport, Engine):
    """Boat class"""

    def __init__(self, manufacturer, tank_fullness, moves_with, horse_powers, weight):
        Transport.__init__(self, manufacturer, tank_fullness, moves_with)
        Engine.__init__(self, horse_powers)
        self.weight = weight

    def __call__(self):
        Boat._engine_start()
        Boat.fly_into_the_sunset(self)

    def __dict__(self):
        if self.tank_fullness:
            return (f"Your {self.manufacturer} with mass {self.weight} kg "
                    f"with powerful {self.moves_with} and {self.horse_powers} horses in it\n"
                    f"Fulfilled")
        return "Empty"

    def __del__(self):
        Transport.__del__(self)
        Engine.__del__(self)
        self.weight = None

    def fly_into_the_sunset(self):
        """method to run script"""
        print("Fishing or BBQ -- Its your chose!")
        return Boat._many_horses(self) if self.__bool__() else print("fill the tank")

    def _many_horses(self):
        if self.horse_powers > 5:
            print(Boat._good_manufacturer(self))
        else:
            print(Boat._to_bottom())

    def _good_manufacturer(self):
        if self.manufacturer == 'Yamaha':
            return "Down, down, down, by the river\n"
        return "You sunks"

    @staticmethod
    def _to_bottom():
        print("Go to bottom!")
        return Boat._fly_into_a_pole()

    @classmethod
    def _engine_start(cls):
        print('R r r t t t t t t t t t t')


class Aircraft(Transport, Engine):
    """Aircraft class"""

    def __init__(self, manufacturer, tank_fullness, moves_with, horse_powers, engines_amount):
        Transport.__init__(self, manufacturer, tank_fullness, moves_with)
        Engine.__init__(self, horse_powers)
        self.engines_amount = engines_amount

    def __call__(self):
        Aircraft._engine_start()
        Aircraft.fly_into_the_sunset(self)

    def __dict__(self):
        if self.tank_fullness:
            return (f"Your {self.manufacturer} with {self.engines_amount} "
                    f"{self.moves_with} and {self.horse_powers} horses in each\n"
                    f"Fulfilled")
        return "Empty"

    def __del__(self):
        Transport.__del__(self)
        Engine.__del__(self)
        self.engines_amount = None

    def fly_into_the_sunset(self):
        """method to run script"""
        print(f"You can take {self.engines_amount * self.horse_powers} kg of baggage with you!")
        return Aircraft._many_horses(self) if self.__bool__() else print("fill the tank")

    def _many_horses(self):
        if self.horse_powers > 700:
            print(Aircraft._good_manufacturer)
        else:
            print(Aircraft._fly_into_a_pole())

    def _good_manufacturer(self):
        if self.manufacturer == 'ANTONOV':
            return "Fly to Sunset\n"
        return "F U"

    @classmethod
    def _engine_start(cls):
        print('W w w w w w w w w w w w w w w w w w w')


Engine.__call__()

bike = Moto('Harley Davidson', False, 'wheels', 61, 2)

print(bike.__sizeof__)
bike.__dict__()
bike.__del__()
print(bike.__dict__())
bike.__call__()
print('\n___________________________________\n')
car = Car('Ford', False, 'wheels', 175, 4)
car.__call__()
car.refuel()
print(car.__sizeof__)
print(car.__dict__())
car.__del__()
print(car.__dict__())
print('\n___________________________________\n')
boat = Boat('Yamaha', False, 'propeller', 10, 4)
boat.__call__()
boat.refuel()
print(boat.__sizeof__)
boat.__dict__()
boat.__del__()
boat.__dict__()
print('\n___________________________________\n')
plane = Aircraft('ANTONOV', True, 'propellers', 800, 4)
plane.__call__()
plane.refuel()
print(plane.__sizeof__)
plane.__dict__()
plane.__del__()
