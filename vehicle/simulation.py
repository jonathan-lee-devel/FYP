import pygame

from vehicle.collision import Collision


class Simulation:
    vehicles = []
    collisions = []
    total_delay = 0.0

    def __init__(self):
        pass

    def update(self):
        # Check for collisions
        for i in range(len(self.vehicles)):
            self.vehicles[i].update()
            for j in range(len(self.vehicles)):
                if i == j:
                    continue
                if i != j and (self.vehicles[i].x - self.vehicles[j].x) < 0.5 and (self.vehicles[i].y - self.vehicles[j].y) < 0.5:
                    # Collision has occurred
                    print('Collision has occurred at ' + str(self.vehicles[i].x) + ',' + str(self.vehicles[i].y))
                    collision = Collision(self.vehicles[i].x, self.vehicles[i].y)
                    collision.vehicles.append(self.vehicles.pop(i))
                    collision.vehicles.append(self.vehicles.pop(j-1))
                    self.collisions.append(collision)
                    return

    def draw(self, screen: pygame.display):
        for vehicle in self.vehicles:
            vehicle.draw(screen)
        for collision in self.collisions:
            collision.draw(screen)

