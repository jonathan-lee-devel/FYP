import uuid

import pygame

vehicle_sprite = pygame.image.load("images/vehicle.png")


class Vehicle:
    id = str(uuid.uuid4())
    x = 0.0
    y = 0.0
    dx = 0.0
    dy = 0.0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def update(self):
        self.x += self.dx
        self.y += self.dy
        # Boundary checking
        if self.x < 0.0:
            self.x = 0.0
        if self.y < 0.0:
            self.y = 0.0
        if self.x > 1000.0:
            self.x = 1000.0
        if self.y > 1000.0:
            self.y = 1000.0

    def draw(self, screen: pygame.display):
        screen.blit(vehicle_sprite, (self.x, self.y))
