from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill();
        log_event("asteroid_split")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            pos_angle = random.uniform(20, 50)
            neg_angle = -(random.uniform(20, 50))
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_vec1 = self.velocity.rotate(pos_angle)
            new_vec2 = self.velocity.rotate(neg_angle)
            new_asteroid1.velocity = new_vec1 * 1.2
            new_asteroid2.velocity = new_vec2 * 1.2