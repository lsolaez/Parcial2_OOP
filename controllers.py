import Constants
from models import ParkingLot
from models import ParkingFloor
from models import Vehicle
from models import Ticket
from heapq import heappop
from datetime import datetime

class ParkingLotController:
    """
    This class was create to control all the actions
    that can be use for the parking lot
    example: park, unpark, add floor, etc
    """
    def __init__(self):
        self.parking_lot = ParkingLot()

    def add_floor(self, num_of_spots):
        """
        help to create new floors on a parking lot
        """
        #get all the floors existing
        floors = self.parking_lot.get_floors()
        #create a new parking floor in the list of the parking lot floor's list
        floors.append(ParkingFloor(len(floors) + 1, num_of_spots))
        self.parking_lot.update_floors(floors)

    def get_available_floor(self):
        floors = self.parking_lot.get_floors()
        """
        this method help to identify if a floor is full or if there's any spot left
        """
        for floor in floors:
            if not floor.is_full():
                return floor

        return None

    def park(self, vehicle: Vehicle):
        floor = self.get_available_floor()
        #indentify if floor is full or not
        if not floor:
            return None

        #Update a vehicule in the floor
        self.parking_lot.update_floors_index(vehicle, floor)
        #Get a aviable spot
        spots = floor.get_spots()
        spot = heappop(spots)
        #update the vehicule in a spot
        spot.update_vehicle(vehicle)
        #change the aviable of the spot
        spot.update_is_taken(1)
        #show the vehicule status in the parking lot
        print(f'vehicle: {vehicle.get_registration_num()} is parked at: {spot.get_spot_num()}')
        #create a ticket for the vehicle
        ticket = Ticket(datetime.now())
        floor.update_spots_index(vehicle, spot, ticket)
        floor.update_spots(spot)

        return

    def unpark(self, vehicle: Vehicle):
        floors_index = self.parking_lot.get_floors_index()
        #identify is the car is on this floor
        floor = floors_index.get(vehicle)
        if not floor:
            return None
        #take the spot index of the ubication of the vehicle
        spots_index = floor.get_spots_index()
        #take the ticket
        spot, ticket = spots_index.get(vehicle)
        if not spot:
            return None

        #Calculate the parking cost
        parking_cost = ((datetime.now() - ticket.get_parked_at()).total_seconds() // 60) * Constants.PER_MINUTE_COST
        #change the spot status
        spot.update_vehicle(None)
        spot.update_is_taken(0)
        #show the end of the process
        print(f'vehicle: {vehicle.get_registration_num()} is unparked at: {spot.get_spot_num()} and parking cost is: {parking_cost}')

        floor.update_spots(spot)
        #return parking cost
        return parking_cost