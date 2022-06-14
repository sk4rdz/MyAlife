import sys
from numpy import random
import pygame
from pygame.locals import *
from plant import Plant

WORLD_SIZE = 300
WINDOW_SIZE = 600
GRID_SIZE = WINDOW_SIZE // WORLD_SIZE
FPS = 10

plants = []


def update(screen):
    surface = pygame.Surface((GRID_SIZE, GRID_SIZE))

    if random.random() <= 0.2:
        plants.append(Plant(random.randint(WORLD_SIZE), random.randint(WORLD_SIZE)))

    for plant in plants:
        plant.grow(1.0)
        surface.set_alpha(int(255 * plant.energy / plant.ENERGY_CAPACITY))
        surface.fill(plant.COLOR)
        screen.blit(surface, (plant.x * GRID_SIZE, plant.y * GRID_SIZE))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(u"a_life")

    frame = 0

    while True:
        update(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)
        frame += 1


if __name__ == "__main__":
    main()
