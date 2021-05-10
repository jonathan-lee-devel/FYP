import json
# from datetime import datetime
from vehicle.simulation import Simulation
from vehicle.vehicle import Vehicle


def log_vehicle(vehicle: Vehicle):
    vehicle_dict = {
        "id": vehicle.id,
        "x": vehicle.x,
        "y": vehicle.y,
        "dx": vehicle.dx,
        "dy": vehicle.dy
    }
    vehicle_json = json.dumps(vehicle_dict)
    print(vehicle_json)
    # with open('log/run_' + str(datetime.now()), 'w') as outfile:
    #     json.dump(vehicle_dict, outfile)


def log_simulation(simulation: Simulation):
    for vehicle in simulation.vehicles:
        log_vehicle(vehicle)
