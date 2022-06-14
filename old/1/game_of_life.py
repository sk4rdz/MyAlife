import numpy as np
import tkinter

SCREEN_SIZE = 600
FIELD_SIZE = 240
GRID_SIZE = SCREEN_SIZE / FIELD_SIZE
INTERVAL = 10


class LifeGame:
    def __init__(self):
        self.cells = np.random.randint(2, size=(FIELD_SIZE, FIELD_SIZE))

    def update(self):
        new_cells = np.zeros_like(self.cells)

        for index, state in np.ndenumerate(self.cells):
            neighbors = self.around(index) - state
            if (neighbors == 2 and state) or neighbors == 3:
                new_cells[index] = 1

        self.cells = new_cells

    def around(self, index):
        x, y = index[1], index[0]
        slx = slice(0, x + 2) if x == 0 else slice(x - 1, x + 2)
        sly = slice(0, y + 2) if y == 0 else slice(y - 1, y + 2)

        return self.cells[sly, slx].sum()


class Visualizer:
    def __init__(self, master, lg):
        self.master = master
        self.lg = lg
        self.cv = tkinter.Canvas(master, width=SCREEN_SIZE, height=SCREEN_SIZE)

        master.title(u"Conway's Game of Life")
        master.after(INTERVAL, self.update)

        self.cv.pack()
        self.draw(self.cv)

    def update(self):
        self.lg.update()
        self.draw(self.cv)
        self.master.after(INTERVAL, self.update)

    def draw(self, cv):
        cv.delete('all')
        cv.create_rectangle(0, 0, SCREEN_SIZE, SCREEN_SIZE, fill='black')

        for i in range(FIELD_SIZE):
            cv.create_line(i*GRID_SIZE, 0, i*GRID_SIZE, SCREEN_SIZE, fill='gray')
            cv.create_line(0, i*GRID_SIZE, SCREEN_SIZE, i*GRID_SIZE, fill='gray')

        for index, live in np.ndenumerate(self.lg.cells):
            x, y = index[1]*GRID_SIZE, index[0]*GRID_SIZE
            if live:
                cv.create_rectangle(x + 1, y + 1, x + GRID_SIZE, y + GRID_SIZE, fill='white', width=0)


if __name__ == '__main__':
    root = tkinter.Tk()
    life_game = LifeGame()
    Visualizer(root, life_game)
    root.mainloop()
