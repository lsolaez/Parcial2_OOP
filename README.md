### Requirements:
  Parking Lot: You have a parking lot that accepts cars only during certain times. Th cars can be charge by minute, hour or days. You will charge different depending on whether the car is a compact, SUV or van. You need to keep track of the available spaces to admit a car. You need to show how many spaces are left. There are different spaces for compact cars, SUV and van.

# How to Run:
  Run the main.py module
  if you want to park a different vehicule, create an new object that represent a vehicle
  `t1 = Compact('EF-10-GH-3456', VehicleType.Compact)`

  in this line we create an compact vehicle object, if you want to make another one, u can create a new object and use SVU, Compact or Van, and the parameters are the Vehicule Register Number as string, and the vehicle type (VehicleType.[the thime of the vehicle you want {Van, Compact or SVU}])

  to change the time the car will spend at the parking lot, you can go to the `main.py`, and look for the  `time.sleep(160)` line, in this
  function you can change the number and put the time (IN SECONDS) that the vehicle will spend in the parking lot.
  Take in account that this app make a parking cost by minute your vehicle spend in the parking lot and not by seconds.



  ## UML Explaining:

    To solve this problem was create an class ParkingLot which has a relation of compose with the parkingFloor and a ParkingController.
    This use an abstract class to create differents types of vehicles, because the methods that each type of vehicle has are basicly the same,
    in that order of ideas, the classes that inherate from the abstract class, can use those abstract methods in the way they needed, this was used in order to not duplicate the code.

    There's also a ParkingController that has methods to park, unpark and create a ticket when the vehicle left the parking
    to show how much the client how to pay for the time he spend at the parking lot. 