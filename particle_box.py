import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


class ParticleBox:
    def __init__(self,
                 init_state=[[1, 0, 0, -1],
                             [-0.5, 0.5, 0.5, 0.5],
                             [-0.5, -0.5, -0.5, 0.5]],
                 bounds=[-2, 2, -2, 2],
                 size=0.04,
                 M=0.05,
                 G=9.8):
        self.init_state = np.asarray(init_state, dtype=float)
        self.M = M * np.ones(self.init_state.shape[0])
        self.size = size
        self.state = self.init_state.copy()
        self.time_elapsed = 0
        self.bounds = bounds
        self.G = G

    def step(self, dt):
        self.time_elapsed += dt
        self.state[:, :2] += dt * self.state[:, 2:]
        D = squareform(pdist(self.state[:, :2]))
        ind1, ind2 = np.where(D < 2 * self.size)
        unique = (ind1 < ind2)
        ind1 = ind1[unique]
        ind2 = ind2[unique]
        for i1, i2 in zip(ind1, ind2):
            m1 = self.M[i1]
            m2 = self.M[i2]
            r1 = self.state[i1, :2]
            r2 = self.state[i2, :2]
            v1 = self.state[i1, 2:]
            v2 = self.state[i2, 2:]
            r_rel = r1 - r2
            v_rel = v1 - v2
            v_cm = (m1 * v1 + m2 * v2) / (m1 + m2)
            rr_rel = np.dot(r_rel, r_rel)
            vr_rel = np.dot(v_rel, r_rel)
            v_rel = 2 * r_rel * vr_rel / rr_rel - v_rel
            self.state[i1, 2:] = v_cm + v_rel * m2 / (m1 + m2)
            self.state[i2, 2:] = v_cm - v_rel * m1 / (m1 + m2)
        crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
        crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
        crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
        crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)
        self.state[crossed_x1, 0] = self.bounds[0] + self.size
        self.state[crossed_x2, 0] = self.bounds[1] - self.size
        self.state[crossed_y1, 1] = self.bounds[2] + self.size
        self.state[crossed_y2, 1] = self.bounds[3] - self.size
        self.state[crossed_x1 | crossed_x2, 2] *= -1
        self.state[crossed_y1 | crossed_y2, 3] *= -1
        self.state[:, 3] -= self.M * self.G * dt

np.random.seed(0)


def Particles(dt=1./30, init_state=-0.5 + np.random.random((50, 4))):
    init_state[:, :2] *= 3.9
    box = ParticleBox(init_state, size=0.04)
    return init_state, box


def animate(name, dt=1./30, init_state=-0.5 + np.random.random((50, 4))):
    init_state, box = Particles(dt, init_state)
    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                         xlim=(-3.2, 3.2), ylim=(-2.4, 2.4))

    particles, = ax.plot([], [], 'bo', ms=6)

    rect = plt.Rectangle(box.bounds[::2],
                         box.bounds[1] - box.bounds[0],
                         box.bounds[3] - box.bounds[2],
                         ec='none', lw=2, fc='none')
    ax.add_patch(rect)

    def init():
        # global box, rect
        particles.set_data([], [])
        rect.set_edgecolor('none')
        return particles, rect

    def animate(i):
        # global box, rect, dt, ax, fig
        box.step(dt)

        ms = int(fig.dpi * 2 * box.size * fig.get_figwidth() /
                 np.diff(ax.get_xbound())[0])
        rect.set_edgecolor('k')
        particles.set_data(box.state[:, 0], box.state[:, 1])
        particles.set_markersize(ms)
        return particles, rect

    ani = animation.FuncAnimation(fig, animate, frames=600,
                                  interval=10, blit=True, init_func=init)
    ani.save(name+'.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

if __name__ == '__main__':
    animate('particle_box')
