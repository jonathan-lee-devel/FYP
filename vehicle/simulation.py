import pygame


class Simulation:
    vehicles = []
    num_collisions = 0
    total_delay = 0.0

    def __init__(self):
        pass

    def update(self):
        for vehicle in self.vehicles:
            vehicle.update()

    def draw(self, screen: pygame.display):
        for vehicle in self.vehicles:
            vehicle.draw(screen)

