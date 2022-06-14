import numpy as np
from simulator import *


def update(sensor_data):
    action = np.random.randint(Simulator.AGENT_MOVE_ACTIONS_NUM)
    if sensor_data[0] or sensor_data[1] or sensor_data[2]:
        action = 1
    elif sensor_data[4] or sensor_data[5] or sensor_data[8]:
        action = 2
    elif sensor_data[3] or sensor_data[6] or sensor_data[7]:
        action = 4
    elif sensor_data[9] or sensor_data[10] or sensor_data[11]:
        action = 3
    return action


Simulator(update).start()
