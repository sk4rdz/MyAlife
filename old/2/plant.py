import numpy as np
import pygame
from properties import *

INITIAL_ENERGY = 1.0
BERTH_ENERGY = 10.0
INCREMENT = 0.75
DECREMENT = 0.02
LIFE_SPAN = 120


class Plant:
    energy = INITIAL_ENERGY
    old = 0

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.peak_old = LIFE_SPAN / 2 + np.random.normal(scale=LIFE_SPAN/10)

    def draw(self, screen):
        surface = pygame.Surface((GRID_SIZE, GRID_SIZE))
        surface.set_alpha(int(255 * (self.energy / BERTH_ENERGY) / 4))
        surface.fill((100, 220, 20))
        screen.blit(surface, (self.x * GRID_SIZE, self.y * GRID_SIZE))

    def update(self, field):
        self.old += 1
        death, berth = False, False
        field_energy = field[self.y][self.x]
        increment = INCREMENT * (self.peak_old - np.abs(self.old - self.peak_old)) / self.peak_old
        absorption = (increment if field_energy - increment > 0 else field_energy)
        self.energy += absorption
        self.energy -= DECREMENT
        if self.energy > BERTH_ENERGY:
            self.energy -= INITIAL_ENERGY
            berth = True
        if self.energy <= 0:
            death = True

        return absorption, berth, death