import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

ALPHA_VALUE = 0.75

COLOR_LIST = [
    "black", "gray", "lightgray", "white", "red",
    "orange", "yellow", "limegreen", "blue", "navy"
]
COLOR_INDEX = {
    "black": 0, "dgray": 1, "lgray": 2, "white": 3, "red": 4,
    "orange": 5, "yellow": 6, "green": 7, "blue": 8, "navy": 9
}
COLOR_MAP, COLOR_NUM = ListedColormap(COLOR_LIST), len(COLOR_LIST)


def get_color_index(color):
    return COLOR_INDEX["black"] if color not in COLOR_INDEX else COLOR_INDEX[color]


class MatrixVisualizer:
    def __init__(self, init_data, update_function=None):
        self.fig = plt.figure()
        self.im = plt.imshow(
            init_data, interpolation="nearest", vmin=0, vmax=COLOR_NUM-1, cmap=COLOR_MAP, alpha=ALPHA_VALUE)
        self.update_func = update_function

    def show(self, interval=100):
        if interval <= 0: interval = 1
        if self.update_func is not None:
            _ = animation.FuncAnimation(self.fig, self.__update, interval=interval)
        plt.show()

    def __update(self, frame):
        self.im.set_data(self.update_func())


if __name__ == "__main__":
    sample_data = [[(j - i) % COLOR_NUM for j in range(COLOR_NUM)] for i in range(COLOR_NUM)]
    vis = MatrixVisualizer(sample_data)
    vis.show(interval=0)
