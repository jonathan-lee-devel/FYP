import json
from datetime import datetime
from vehicle.simulation import Simulation
from vehicle.vehicle import Vehicle

vehicle_states = []


def log_vehicle(vehicle: Vehicle):
    vehicle_dict = {
        "id": vehicle.id,
        "x": vehicle.x,
        "y": vehicle.y,
        "dx": vehicle.dx,
        "dy": vehicle.dy
    }
    vehicle_states.append(vehicle_dict)


def log_simulation(simulation: Simulation):
    for vehicle in simulation.vehicles:
        log_vehicle(vehicle)


def log_simulation_final(simulation: Simulation):
    output_log = {
        "num_collisions": simulation.num_collisions,
        "total_delay": simulation.total_delay,
        "vehicle_states": vehicle_states
    }
    with open('log/run_' + str(datetime.now()) + '.json', 'w') as outfile:
        json.dump(output_log, outfile)
