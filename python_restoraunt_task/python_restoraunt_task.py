"""
This is my Restaurant class-library
Order - class to make order in restaurant({dishes}, {drinks}, {child room})
Delivery - class to order delivery
"""
from abc import ABC, abstractmethod
from collections import Counter
from datetime import datetime
from random import randint
import re


class Menu(ABC):
    """Data class contains prices of dishes/drinks/rooms"""
    dishes_prices = {"Pizza": 200, "Salad": 40, "Shrimps": 300, "Hamburger": 80,
                     "Cheesecake": 30, "Pudding": 40, "Cookies": 10, "Chocolate cake": 30}
    drink_prices = {"Latte": 20, "Espresso": 15, "Raf": 35, "Tea": 20}

    rooms_prices = {"Pirates": 1800, "Fairytale": 600, "Magic Kingdom": 400}


class OrderPattern(ABC):
    """Abstract superclass for Order and Delivery"""
    def __init__(self, dishes_dict, drinks_dict):
        self.dishes_dict = Counter(dishes_dict)
        self.drinks_dict = Counter(drinks_dict)
        self.order_id = Waiter.order_id_creator()

    @abstractmethod
    def raise_conflict(self):
        """scratch for lower().raise_conflict"""

    @staticmethod
    def order_changed(dishes_dict, drinks_dict):
        """method to control, how many precursors' restaurant have"""
        for key in dishes_dict:
            if Kitchen.product_left[key] <= dishes_dict[key]:
                print('We can`t observe this order')
                dishes_dict[key] = 10
        for key in drinks_dict:
            if Bar.product_left[key] <= drinks_dict[key]:
                print('We can`t observe this order')
                drinks_dict[key] = 10
        Kitchen.product_left.subtract(dishes_dict)
        Bar.product_left.subtract(drinks_dict)


class Order(OrderPattern):
    """instantiable class for proceed cycle of order complication"""

    def __init__(self, dishes_dict, drinks_dict, child_room):
        OrderPattern.__init__(self, dishes_dict, drinks_dict)
        self.kitchen = Kitchen()
        self.bar = Bar()

        if child_room in CrManager.empty_rooms.keys():
            self.child_room = child_room
        else:
            print(f'We don`t have room with this name: {child_room} \n Standard: Pirates')
            ChildrenRoom("Pirates")
            self.child_room = "Pirates"
        CrManager.empty_rooms[self.child_room] = False

        self.table_num = Waiter.sat_guest()

        self.order_changed(self.dishes_dict, self.drinks_dict)
        ChildrenRoom(self.child_room)

    def __add__(self, added_dish, added_drink):
        """method to proceed changes in order"""
        self.dishes_dict.update(added_dish)
        self.drinks_dict.update(added_drink)
        self.order_changed(added_dish, added_drink)

    def raise_conflict(self):
        """method to raise problems and resolve them"""
        if randint(0, 1) > 0:
            print("chef`s complement from kitchen")
            self.__add__({Kitchen.chefs_complement(self.kitchen)[0]: 0}, {})
        else:
            print("chef`s complement from Bar")
            self.__add__({}, {Bar.chefs_complement(self.bar)[0]: 0})

    def pay_off(self):
        """method to take receipt of your rest"""
        Waiter.pay_off(self.order_id, self.table_num, self.dishes_dict,
                       self.drinks_dict, self.child_room)
        CrManager.empty_rooms[self.child_room] = True
        Waiter.empty_tables_list[self.table_num - 1] = True


class Delivery(OrderPattern):
    """instantiable class for proceed cycle of delivery order complication"""
    discount = 1

    def __init__(self, order_address, dishes_dict, drinks_dict):
        self.order_address = order_address
        OrderPattern.__init__(self, dishes_dict, drinks_dict)

        self.order_id = Waiter.order_id_creator() + '_D'

    @classmethod
    def raise_conflict(cls):
        """method to resolve conflict in delivery(by making discount)"""
        Delivery.discount *= 0.8

    def pay_off(self):
        """method to take receipt of your order"""
        CallCentre.pay_off(self.order_id, self.order_address, self.dishes_dict,
                           self.drinks_dict, Delivery.discount)


class FrontStaff(ABC):  # Order_Control
    """Abstract superclass for Waiter, CallCentre, CrManager"""
    @abstractmethod
    def sat_guest(self):
        """scratch set the table number for order"""

    @abstractmethod
    def pay_off(self, **kwargs):
        """scratch method to calculate and print receipt"""

    @staticmethod
    def calculate(dishes_dict, drinks_dict, child_room):
        """receipt calculator"""
        total_sum = 0
        for key in dishes_dict:
            if dishes_dict[key] != 0:
                total_sum += Menu.dishes_prices[key] * dishes_dict[key]
        for key in drinks_dict:
            if drinks_dict[key] != 0:
                total_sum += Menu.drink_prices[key] * drinks_dict[key]
        if child_room != '':
            total_sum += Menu.rooms_prices[child_room]
        return total_sum

    @staticmethod
    def print_receipt(order_id, dishes_dict, drinks_dict, child_room):
        """receipt printer"""
        print(f"__________RECEIPT___________\n"
              f"Order# {order_id}\n")
        for key in dishes_dict:
            if dishes_dict[key] != 0:
                print(f"{key}:\t{dishes_dict[key]}pc\t{Menu.dishes_prices[key]}$")
            else:
                print(f"{key}:\t1pc\tgift 0$")
        print("____________________________\n")
        for key in drinks_dict:
            if drinks_dict[key] != 0:
                print(f"{key}:\t{drinks_dict[key]}pc\t{Menu.drink_prices[key]}$")
            else:
                print(f"{key}:\t1pc\tgift 0$")
        if child_room != '':
            print(f"room {child_room}:\t{Menu.rooms_prices[child_room]}$")


class Waiter(FrontStaff, ABC):
    """class to observe orders in restaurant"""

    empty_tables_list = [True for _ in range(20)]

    @classmethod
    def sat_guest(cls):
        """scratch set the table number for order"""
        while True:
            busy_table = randint(0, 19)
            if cls.empty_tables_list[busy_table]:
                cls.empty_tables_list[busy_table] = False
                break
        return busy_table + 1

    @staticmethod
    def order_id_creator():
        """method to create order_id for orders in restaurant """
        return re.sub(r"\D", '', str(datetime.now()))

    @staticmethod
    def pay_off(order_id, table_num, dishes_dict, drinks_dict, child_room):
        """ method to print calculated order` receipt"""
        print(f'\n\nTable: {table_num}')
        FrontStaff.print_receipt(order_id, dishes_dict, drinks_dict, child_room)
        print(f"____________TOTAL___________\n"
              f"PRICE:\t\t{round(FrontStaff.calculate(dishes_dict, drinks_dict, child_room))}")


class CallCentre(FrontStaff, ABC):
    """class to observe delivery orders"""

    deliveries_list = ["Max", "Scott", "Whill"]

    @staticmethod
    def pay_off(order_id, order_address, dishes_dict, drinks_dict, discount):
        """ method to print calculated delivery order receipt"""
        print(f'\n\nDelivery Address: {order_address}')
        FrontStaff.print_receipt(order_id, dishes_dict, drinks_dict, '')
        print(f"____________TOTAL___________\n"
              f"PRICE:\t\t"
              f"{round(FrontStaff.calculate(dishes_dict, drinks_dict, '') * Delivery.discount)}")


class CrManager(FrontStaff, ABC):
    """Data class contains empty_is? rooms and room`s staff"""
    empty_rooms = {"Pirates": True, "Fairytale": True, "Magic Kingdom": True}


class Executor(ABC):
    """Abstract superclass for Kitchen, ChildrenRoom, Bar"""
    product_left = Counter({})

    def chefs_complement(self):
        """scratch for resolving conflicts"""
        return self.product_left.most_common(1)[0]


class Kitchen(Executor):
    """Class for contain how many portions had left"""

    product_left = Counter({"Pizza": 10, "Salad": 10, "Shrimps": 10, "Hamburger": 10,
                           "Cheesecake": 10, "Pudding": 10, "Cookies": 10, "Chocolate cake": 10})


class Bar(Executor):
    """Class for contain how many coffee` precursors had left"""
    product_left = Counter({"Latte": 10, "Espresso": 10, "Raf": 10, "Tea": 10})

    @classmethod
    def wipe_glasses(cls):
        """same, useless, but why not to add some specific features in class-library"""
        print("BAR:  sc.rr, sc.rr, sc.rr")


class ChildrenRoom(Executor):
    """not mention"""
    actors_container = {"Pirates": ('Sonya', 'Anya', 'Melania'),
                        "Fairytale": ('Vas_ya', 'Petya', 'Cost_ya'),
                        "Magic Kingdom": ('Gleb', 'Oleg', 'Fedor')}

    def __init__(self, child_room):
        if child_room is None:
            self.actors = None
        else:
            self.actors = self.actors_container[child_room]

    def __call__(self, *args, **kwargs):
        """ it looks useless, but pretty, right?"""
        if self.actors is None:
            print("No children`s room in your order")
        else:
            print(f'*Sound of unbelievable fun*\n'
                  f'Actors {self.actors} were playing with kids')


print('\n\n')
order = Order({"Pizza": 4, "Salad": 2}, {"Latte": 2, "Espresso": 2}, 'Pirates')
order.__add__({"Shrimps": 4}, {})
print('\n\n')
print(order.dishes_dict)
print(order.drinks_dict)
order.raise_conflict()
print(order.dishes_dict)
print(order.drinks_dict)
print(Kitchen.product_left)
print(Bar.product_left)
order.pay_off()
print('\n\n')
bad_order = Order({"Pizza": 4, "Salad": 2}, {"Latte": 2, "Espresso": 2}, 'Fairytale')

delivery_order = Delivery('Independence.str 80/20', {"Pizza": 4, "Salad": 2},
                          {"Latte": 2, "Espresso": 2})
print(delivery_order.dishes_dict)
print(delivery_order.drinks_dict)
print(delivery_order.order_address)
print(delivery_order.order_id)
print('\n\n')

delivery_order.pay_off()
delivery_order.raise_conflict()
delivery_order.pay_off()
delivery_order.raise_conflict()
delivery_order.pay_off()

Bar.wipe_glasses()
