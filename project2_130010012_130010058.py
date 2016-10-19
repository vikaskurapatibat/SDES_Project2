import numpy as np
from matplotlib import pyplot as plt

def projectile(u,theta,n):
	"""The motion of a point mass under gravity in two dimensions thrown at an angle theta with horizontal and a velocity u"""
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
                               frames=200, interval=20, blit=True)
    anim.save(name+'.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()