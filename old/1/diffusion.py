import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

FIG_SIZE = (6, 4)
STEP_NUM = int(1e5)
INTERVAL = 0
LOG_INTERVAL = 100

FIELD_SIZE = 120
DIFFUSION_SPEED = 0.1  # < 0.25


e = np.random.rand(FIELD_SIZE, FIELD_SIZE)

fig = plt.figure(figsize=FIG_SIZE)
im = plt.imshow(e, interpolation='nearest', cmap='GnBu_r', vmin=0, vmax=1)


def update(frame):
    global e
    de = (np.roll(e, 1, axis=0) + np.roll(e, -1, axis=0) +
          np.roll(e, 1, axis=1) + np.roll(e, -1, axis=1) - e*4) * DIFFUSION_SPEED
    e += de
    im.set_data(e)
    if frame % LOG_INTERVAL == 0 and not frame == 0:
        print(f"STEP:{str(frame)}", f"STD:{np.std(e)}")
    return [im]


animate = animation.FuncAnimation(fig, update, interval=INTERVAL, frames=STEP_NUM, repeat=False, blit=True)
plt.colorbar()
plt.show()
