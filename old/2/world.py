import sys
import numpy as np
import pygame
import random
from pygame.locals import *
from properties import *
from noise import Noise
from plant import Plant

FPS = 60


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(u"World")

    frame = 0
    noise = Noise()
    plants = [Plant(np.random.randint(FIELD_SIZE), np.random.randint(FIELD_SIZE))]

    while True:
        field = noise.update(frame)
        for index, value in np.ndenumerate(field):
            nx, ny = index[1] * GRID_SIZE, index[0] * GRID_SIZE
            bright = int((value if value <= 1.0 else 1.0) * 255)
            screen.fill((bright, bright, bright), Rect(nx, ny, GRID_SIZE, GRID_SIZE))
        death, berth = 0, 0
        for plant in plants:
            args = plant.update(field)
            field[plant.y][plant.x] -= args[0]
            if args[1]:
                direction = random.choice([(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)])
                bx, by = adjust_point(plant.x + direction[0]), adjust_point(plant.y + direction[1])

                plants.append(Plant(bx, by))
                berth += 1
            if args[2]:
                plants.remove(plant)
                death += 1
            else:
                plant.draw(screen)
        if frame % LOG_INTERVAL == 0:
            print(f"PLANT_NUM: {len(plants)}", f"DEATH: {death}", f"BERTH: {berth}")

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)
        frame += 1


def adjust_point(point):
    if point < 0:
        point = FIELD_SIZE - 1
    elif point >= FIELD_SIZE:
        point = 0
    return point


if __name__ == "__main__":
    main()
