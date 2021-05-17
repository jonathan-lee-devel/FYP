import pygame

from vehicle.logger import log_simulation, log_simulation_final
from vehicle.simulation import Simulation
from vehicle.vehicle import Vehicle

# Initialize pygame
pygame.init()

# Create display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic Simulator")

# Initialise the simulation
simulation = Simulation()
vehicle_x_coords = [330.0, 330.0, 450.0, 450.0]
vehicle_y_coords = [0.0, 100.0, 600.0, 700.0]
vehicle_dx = [0.0, 0.0, 0.0, 0.0]
vehicle_dy = [0.05, 0.1, -0.1, -0.1]
for i in range(len(vehicle_x_coords)):
    vehicle = Vehicle(vehicle_x_coords[i], vehicle_y_coords[i], vehicle_dx[i], vehicle_dy[i])
    simulation.vehicles.append(vehicle)


# Main loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                running = False

    # Display code
    screen.fill((0, 102, 0))  # Green background
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 300, 800, 200))  # Vertical road
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 0, 200, 800))  # Horizontal road

    # Simulation code
    simulation.update()
    simulation.draw(screen)
    log_simulation(simulation)

    # Final display update
    pygame.display.update()

# End of application
print('Application exiting...')
log_simulation_final(simulation)
pygame.quit()
