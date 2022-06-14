class Plant:
    ENERGY_CAPACITY = 10.0
    COLOR = (100, 220, 20)

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.energy = 0

    def grow(self, energy):
        if self.energy < self.ENERGY_CAPACITY:
            self.energy += energy