from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from heapq import heapify, heappush

class Vehicle(ABC):
    """
    define an abstract class to create diferents type of vehicles
    taking into account that each vehicule share theirs methods and attibutes
    """
    def __init__(self, registration_num: str, vehicle_type: Enum):
        self._registration_num = registration_num
        self._vehicle_type = vehicle_type


    """
    abstract methods that we will use 
    when create the differents types of vehicles
    """

    @abstractmethod
    def get_registration_num(self):
        pass

    @abstractmethod
    def get_vehicle_type(self):
        pass

class SUV(Vehicle):
    """
    create an class Bike which inheritance the abstract class
    """
    def __init__(self, registration_num: str, vehicle_type: Enum):
        #Call the constructor of the abstract class
        super().__init__(registration_num, vehicle_type)

    #return the registration numbers of the vehicle
    def get_registration_num(self):
        return self._registration_num
    #return the type of the vehicle
    def get_vehicle_type(self):
        return self._vehicle_type

class Van(Vehicle):
    """
    create an class Car which inheritance the abstract class
    """
    def __init__(self, registration_num: str, vehicle_type: Enum):
        #Call the constructor of the abstract class
        super().__init__(registration_num, vehicle_type)

#return the registration numbers of the vehicle
    def get_registration_num(self):
        return self._registration_num
#return the type of the vehicle
    def get_vehicle_type(self):
        return self._vehicle_type

class Compact(Vehicle):
    """
    create an class Truck which inheritance the abstract class
    """
    def __init__(self, registration_num: str, vehicle_type: Enum):
        #Call the constructor of the abstract class
        super().__init__(registration_num, vehicle_type)

#return the registration numbers of the vehicle
    def get_registration_num(self):
        return self._registration_num
#return the type of the vehicle
    def get_vehicle_type(self):
        return self._vehicle_type

class Ticket:
    def __init__(self, parked_at: datetime):
        #use datatime to take the time the vehicule is in the parking lot
        self.__parked_at = parked_at
    #return the time, the vehicle start at the parking lot
    def get_parked_at(self):
        return self.__parked_at

class ParkingSpot:
    def __init__(self, spot_num:int):
        """
        Create the numbers of spots that a parking's floor has
        """
        self.__spot_num = spot_num
        self.__is_taken = 0
        self.__vehicle = None

    def __lt__(self, other):
        """
        this method compare the aviable of a spot taking as reference the next one of it
        it compares the one given with the next one
        and taking in account that if is empty, the __is_taken=0
        but if not it will be 1
        """
        if self.__is_taken != other.__is_taken:
            return self.__is_taken < other.__is_taken

        return self.__spot_num < other.__spot_num

    #if its taken it will return that the spot was taken
    def get_is_taken(self):
        return self.__is_taken
    #update the spot aviable
    def update_is_taken(self, val: int):
        self.__is_taken = val
    #will return the spot number taken
    def get_spot_num(self):
        return self.__spot_num
    #the vehicle that take that spot
    def get_vehicle(self):
        return self.__vehicle
    #and update that vehicule in the spot
    def update_vehicle(self, vehicle: Vehicle):
        self.__vehicle = vehicle

class ParkingFloor:
    def __init__(self, floor_num:int, num_of_spots:int):
        """
        This parking lot could have differents floors
        with certain numbers of spots
        """
        self.__floor_num = floor_num
        self.__spots = [ParkingSpot(spot_num) for spot_num in range(num_of_spots)]
        self.__spots_index = {}
        heapify(self.__spots)

    def get_floor_num(self):
        return self.__floor_num

    def get_spots(self):
        return self.__spots

    def update_spots(self, spot: ParkingSpot):
        heappush(self.__spots, spot)

    def get_spots_index(self):
        return self.__spots_index

    def update_spots_index(self, vehicle: Vehicle, spot: ParkingSpot, ticket: Ticket):
        self.__spots_index[vehicle] = (spot, ticket)

    def is_full(self):
        return self.__spots[0].get_is_taken()

class SingletonMeta(type):
    """
    Use the disegn pattern of the singleton to avoid that the system
    assign the same spot of the parking lot, to two different vehicles
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class ParkingLot(metaclass=SingletonMeta):
    def __init__(self):
        """
        A parking lot can have differents floors
        and each floor has a different index
        """
        self.__floors = []
        self.__floors_index = {}

    #return the list of floors
    def get_floors(self):
        return self.__floors
    #update that list of floor
    def update_floors(self, floors: list):
        self.__floors = floors
    #return the floors index
    def get_floors_index(self):
        return self.__floors_index
    
    def update_floors_index(self, vehicle: Vehicle, floor: ParkingFloor):
        self.__floors_index[vehicle] = floor