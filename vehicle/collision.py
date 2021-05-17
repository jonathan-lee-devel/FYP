import pygame
import uuid

collision_sprite = pygame.image.load("images/collision.png")


class Collision:
    id = str(uuid.uuid4())
    x = 0.0
    y = 0.0
    vehicles = []

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def draw(self, screen: pygame.display):
        screen.blit(collision_sprite, (self.x, self.y))

