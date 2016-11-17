import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from hypothesis import given
from hypothesis import strategies as st


def projectile(u, theta, n=1000, g=9.81):
    '''The motion of a point mass under gravity in two dimensions thrown at an ang\
    le theta with the horizontal and a velocity'''
    theta_rad = theta*np.pi/180.0
    t_max = 2*u*np.sin(abs(theta_rad))/9.81
    t = np.linspace(0.0, t_max, n)
    x = u*np.cos(theta_rad)*t
    y = u*np.sin(theta_rad)*t - 0.5*g*t*t
    return t, x, y


def animate(X, Y, name):
    fig = plt.figure()
    ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y), np.amax(Y)+0.1*np.amin(Y)))
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x = X[:i]
        y = Y[:i]
        line.set_data(x, y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1000, interval=10, blit=True)
    anim.save(name+'.mp4', fps=120, extra_args=['-vcodec', 'libx264'])
    plt.show()


@given(st.integers(min_value=0, max_value=1000), st.integers(min_value=0, max_value=180),
       st.integers(min_value=100, max_value=1e5))
def test_projectile(u, theta, n):
    t, x, y = projectile(u, theta, n)
    if u == 0:
        assert x[-1] == 0
    if (theta > 0) and (theta < 90.0) and u != 0:
        assert x[-1] > 0
        assert abs(y[0] - y[-1]) < 1e-4
    elif (theta < 180.0) and (theta > 90.0)and u != 0:
        assert x[-1] < 0
        assert abs(y[0] - y[-1]) < 1e-4

if __name__ == '__main__':
    # t, x, y = projectile(10.0, 45.0)
    # animate(x, y, 'projectile')
    test_projectile()
