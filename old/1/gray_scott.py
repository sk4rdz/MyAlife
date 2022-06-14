import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

FIG_SIZE = (9, 7)

FIELD_SIZE = 128
SQUARE_SIZE = 10

Du, Dv = 0.2, 0.1
f, k = 0.04, 0.06

u = np.ones((FIELD_SIZE, FIELD_SIZE))
v = np.zeros((FIELD_SIZE, FIELD_SIZE))

s1, s2 = FIELD_SIZE // 2, SQUARE_SIZE // 2
u[s1-s2:s1+s2, s1-s2:s1+s2] = 0.5
v[s1-s2:s1+s2, s1-s2:s1+s2] = 0.25
u += np.random.rand(FIELD_SIZE, FIELD_SIZE)*0.1
v += np.random.rand(FIELD_SIZE, FIELD_SIZE)*0.1

fig = plt.figure(figsize=FIG_SIZE)
im = plt.imshow(u, interpolation='nearest', cmap='gray', vmin=0, vmax=1)


def update(frame):
    global u, v
    nu = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) +
          np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 4 * u)
    nv = (np.roll(v, 1, axis=0) + np.roll(v, -1, axis=0) +
          np.roll(v, 1, axis=1) + np.roll(v, -1, axis=1) - 4 * v)
    u += Du*nu - u*v*v + f*(1.0-u)
    v += Dv*nv + u*v*v - (f+k)*v
    im.set_data(u)
    if frame % 100 == 0:
        print("STEP: " + str(frame))
    return [im]


animate = animation.FuncAnimation(fig, update, interval=10, frames=10**5, repeat=False, blit=True)
plt.colorbar()
plt.show()
