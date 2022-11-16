from enum import Enum

class VehicleType(Enum):
    """
    use Enum to enummerate the type of vehicule
    to help the code identify each type of vehicule
    on a easier way
    """
    SUV, Van, Compact = 1, 2, 3

PER_MINUTE_COST = 100