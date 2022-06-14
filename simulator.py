import numpy as np
import visualizer as vis


class Simulator:
    FIELD_WIDTH, FIELD_HEIGHT = 128, 128
    FIELD_SIZE = FIELD_HEIGHT, FIELD_WIDTH

    FEED_NUM = 200
    FEED_ENERGY = 1.0

    AGENT_SIZE = 3
    AGENT_MOVE_ACTIONS = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
    AGENT_MOVE_ACTIONS_NUM = len(AGENT_MOVE_ACTIONS)

    AGENT_VISIONS = [
        (-2, 0), (-1, -1), (-1, 0), (-1, 1),
        (0, -2), (0, -1), (0, 1), (0, 2),
        (1, -1), (1, 0), (1, 1), (2, 0), ]
    AGENT_VISIONS_NUM = len(AGENT_VISIONS)

    def __init__(self, update_function):
        self.feeds = np.zeros(self.FIELD_SIZE)
        for num in np.random.choice(self.FIELD_WIDTH * self.FIELD_HEIGHT, self.FEED_NUM, replace=False):
            x, y = num % self.FIELD_WIDTH, num // self.FIELD_WIDTH
            self.feeds[y][x] = self.FEED_ENERGY

        self.agent_pos = np.array([np.random.randint(self.FIELD_HEIGHT), np.random.randint(self.FIELD_WIDTH)])

        self.update_func = update_function
        self.visualizer = vis.MatrixVisualizer(self.__get_vis_data(), update_function=self.__update)

    def __update(self):
        sensor_data = np.zeros(self.AGENT_VISIONS_NUM)
        for i, v in enumerate(self.AGENT_VISIONS):
            y, x = (self.agent_pos + v) % self.FIELD_SIZE
            sensor_data[i] = self.feeds[y][x]

        action = self.update_func(sensor_data)

        vy, vx = self.AGENT_MOVE_ACTIONS[action]
        self.agent_pos += vy, vx
        self.agent_pos %= self.FIELD_SIZE

        for i in range(self.AGENT_SIZE):
            for j in range(self.AGENT_SIZE):
                y, x = (self.agent_pos + (i, j)) % self.FIELD_SIZE
                if self.feeds[y][x]: self.feeds[y][x] = 0

        return self.__get_vis_data()

    def __get_vis_data(self):
        vis_data = self.feeds * np.full_like(self.feeds, vis.get_color_index("white"))
        for i in range(self.AGENT_SIZE):
            for j in range(self.AGENT_SIZE):
                y, x = (self.agent_pos + (i, j)) % self.FIELD_SIZE
                vis_data[y][x] = vis.get_color_index("blue")
        return vis_data

    def start(self):
        self.visualizer.show(interval=10)
