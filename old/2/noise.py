import numpy as np
from properties import *

SIN_CYCLE = 32


class Noise:
    octaves = []

    def __init__(self):
        for num in range(OCTAVE_NUM):
            self.octaves.append(Octave(2 ** num))

    def update(self, frame):
        field = np.zeros((FIELD_SIZE, FIELD_SIZE))

        for num in range(OCTAVE_NUM):
            length = 2 ** num
            if frame % length == 0:
                self.octaves[num].update()

            for i in range(length):
                for j in range(length):
                    field[i::length, j::length] += self.octaves[num].field

            sin = (np.sin(frame * np.pi / SIN_CYCLE) + 1) * 0.5
            field *= sin

        return field


class Octave:
    def __init__(self, cell_size):
        self.length = int(FIELD_SIZE / cell_size)
        self.field = np.zeros((self.length, self.length))

    def update(self):
        self.field = np.random.rand(self.length, self.length) / OCTAVE_NUM
