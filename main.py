from Constants import VehicleType
from models import SUV
from models import Van
from models import Compact
from controllers import ParkingLotController
import time

if __name__ == '__main__':
    parking_lot = ParkingLotController()
    parking_lot.add_floor(2)
    parking_lot.add_floor(1)

    b1 = SUV('AB-01-CD-1234', VehicleType.SUV)
    b2 = Van('AB-01-CD-5678', VehicleType.SUV)
    c1 = Compact('BC-01-DC-9876', VehicleType.Van)
    t1 = Compact('EF-10-GH-3456', VehicleType.Compact)
    

    parking_lot.park(b1)
    parking_lot.park(b2)
    parking_lot.park(c1)
    parking_lot.park(t1)

    """
    Use the sleep function to make a death time
    to represent the time the car will spend at the parking lot

    to use this function, you need to use the time in seconds

    take in account that this code was programmed to charge a cost by minute
    """
    
    time.sleep(160)
    parking_lot.unpark(b2)
    parking_lot.unpark(c1)