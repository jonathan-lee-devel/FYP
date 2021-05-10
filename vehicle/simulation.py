import pygame


class Simulation:
    vehicles = []

    def __init__(self):
        pass

    def update(self):
        for vehicle in self.vehicles:
            vehicle.update()

    def draw(self, screen: pygame.display):
        for vehicle in self.vehicles:
            vehicle.draw(screen)

