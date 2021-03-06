import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from hypothesis import given
from hypothesis import strategies as st
from scipy.spatial.distance import pdist, squareform
import scipy.integrate as integrate


def projectile(u, theta, n):
	"""The motion of a point mass under gravity in two dimensions thrown at an ang\
	le theta with horizontal and a velocity u"""
	t_max = 2*u*np.sin(theta)/9.81
	t = np.linspace(0.,t_max,n)
	x = u*np.cos(theta)*t
	y = u*np.sin(theta)*t - 0.5*9.81*t*t
	return t,x,y

class charge_particle:
	"""docstring for charge_particle"""
	def __init__(self, q = 0.,m = 1.,x=0.,y=0.,z=0.,vx=0.,vy=0.,vz=0.):
		self.q = q
		self.m = m
		self.x = x
		self.y = y
		self.z = z
		self.vx = vx
		self.vy = vy
		self.vz = vz

class particles:

    def __init__(self, init_state, bounds, size = 0.04, M = 0.05, G = 9.8):
        self.init_state = np.asarray(init_state, dtype=float)
        self.M = M * np.ones(self.init_state.shape[0])
        self.size = size
        self.state = self.init_state.copy()
        self.time_elapsed = 0
        self.bounds = bounds
        self.G = G

def test_projectile_dummy():
     t,x,y = projectile(10,np.pi/2.0,10)
     assert x[0] == 0.
     assert y[0] == y[-1]

@given(st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=1) )
def test_projectile_hyp(u, theta, n):
    t,x,y = projectile(u, theta, n)
    assert y[0] == y[-1]
    if (theta > 0) and (theta<np.pi/2.):
        assert x[-1]>0
        assert y[0] == y[-1]
    elif (theta < np.pi) and (theta<np.pi/2.):
        assert x[-1]>0
        assert y[0] == y[-1]

def test_cyclotron():
    pass

def Bx(x,y,z):
	return 0.0

def By(x,y,z):
	return 0.0

def Bz(x,y,z):
	return 10

def Ex(x,y,z):
	return 10

def Ey(x,y,z):
	return 0.0

def Ez(x,y,z):
	return 0.0

def new():
	pass

def cyclotron(q,m,x_i,y_i,z_i,vx_i,vy_i,vz_i,Bx,By,Bz,Ex,Ey,Ez,tf,dt):
	"""The motion of a point charge under a varying electric and magnetic field which are to  be given as functions of x,y,z in three components."""
	particle = charge_particle(q,m,x_i,y_i,z_i,vx_i,vy_i,vz_i)
	X = [particle.x]
	Y = [particle.y]
	Z = [particle.z]
	t = 0.
	T = [0.]
	while t < tf:
		#Using Semi-implicit Euler Integrator to integrate the motion of the body
		particle.vx = (q/m)*(Ex(particle.x,particle.y,particle.z) + particle.vy*Bz(particle.x,particle.y,particle.z) - particle.vz*By(particle.x,particle.y,particle.z))
		particle.vy = (q/m)*(Ey(particle.x,particle.y,particle.z) - particle.vx*Bz(particle.x,particle.y,particle.z) - particle.vz*Bx(particle.x,particle.y,particle.z))
		particle.vz = (q/m)*(Ez(particle.x,particle.y,particle.z) + particle.vx*By(particle.x,particle.y,particle.z) - particle.vy*Bx(particle.x,particle.y,particle.z))
		particle.x += particle.vx*dt
		particle.y += particle.vy*dt
		particle.z += particle.vz*dt
		X.append(particle.x)
		Y.append(particle.y)
		Z.append(particle.z)
		t += dt
		T.append(t)

	return T,X,Y,Z


def animate(X,Y,name):
    fig = plt.figure()
    ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y), np.amax(Y)+0.1*np.amin(Y)))
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([],[])
        return line,
    def animate(i):
        x = X[:i]
        y = Y[:i]
        #print x,y
        line.set_data(x, y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=10, blit=True)
    anim.save(name+'.mp4', fps=120, extra_args=['-vcodec', 'libx264'])
    plt.show()

if __name__ == '__main__':
    #t,x,y = projectile(10,np.pi/4.,1000)
    #animate(x,y,'projectile')
    test_projectile()
