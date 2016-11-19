#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from ttk import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
#from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def projectile( u,theta,n):
    """The motion of a point mass under gravity in two dimensions thrown at an angle theta with horizontal and a velocity u"""
    t_max = 2*u*np.sin(theta)/9.81
    t = np.linspace(0.,t_max,n)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*9.81*t*t
    return t,x,y

class MainApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("700x500+200+10")
        self.title("Physics Simulator")
        self.configure(background='white')
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Projectile, Brownian,Cyclotron, Schrodinger ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.controller = controller
        self.initUI()
        
    def initUI(self):
        title = Label(self, text="Welcome to Physics Simulator!" ,font=("Comic Sans MS", 25))
        title.pack(pady=5)
        photo = PhotoImage(file="atom1.gif",)
        #photo = photo.zoom(2)
        photo = photo.subsample(3)
        label1 = Label(self, image=photo)
        label1.photo = photo
        label1.pack(pady=10)
        
        var = StringVar()
        var.set("Please select one of the below problems to simulate")
        label2 = Label(self, text="Please select one of the below problems to simulate" )
  
        label2.pack(pady=10)
 
        button1 = Button(self, text="Projectile Motion",
                           command=lambda: self.controller.show_frame("Projectile"))
        button1.pack(padx=5, pady=5)          
       
        button2 = Button(self, text="Brownian Motion",
                           command=lambda: self.controller.show_frame("Brownian"))
        button2.pack(padx=5, pady=5) 
        
        button3 = Button(self, text="Cyclotron Motion",
                           command=lambda: self.controller.show_frame("Cyclotron"))
        button3.pack(padx=5, pady=5)

        button5 = Button(self, text="Schrodinger Equation",
                           command=lambda: self.controller.show_frame("Schrodinger"))
        button5.pack(padx=5, pady=5)        
        
              
class Projectile(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.controller = controller
        self.initUI()
        
    def initUI(self):
        frame0 = Frame(self)
        frame0.pack()

        title = Label(frame0, text="Projectile Motion" ,font=("Comic Sans MS", 25))
        title.pack()
        
        frame1 = Frame(self)
        frame1.pack(side = LEFT, anchor=N)
        
        button1 = Button(frame1, text="Home",
                           command=lambda: self.controller.show_frame("Home"))
        button1.grid(row=0, column=0, padx=5, pady=25)          
       
        button2 = Button(frame1, text="Brownian Motion",
                           command=lambda: self.controller.show_frame("Brownian"))
        button2.grid(row=1, column=0, padx=5, pady=5)  
      
        button3 = Button(frame1, text="Cyclotron Motion",
                           command=lambda: self.controller.show_frame("Cyclotron"))
        button3.grid(row=2, column=0, padx=5, pady=5) 
        
        button5 = Button(frame1, text="Schrodinger Equation",
                           command=lambda: self.controller.show_frame("Schrodinger"))
        button5.grid(row=3, column=0, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(side=LEFT)

##        f = Figure(figsize=(4,4), dpi=100)
##        a = f.add_subplot(111)
##        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
##        global fig
##        plt.ion()
        fig = plt.figure(figsize=(4,4), dpi=100)
        canvas = FigureCanvasTkAgg(fig, frame2)
        #canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM)

##        toolbar = NavigationToolbar2TkAgg(canvas, frame2)
##        toolbar.update()
##        canvas._tkcanvas.pack(side=TOP, anchor= CENTER)

        time ,x,y = projectile(10,np.pi/4.,100)
        #self.animate(x,y, fig)
        #canvas.show()
        
        frame3 = Frame(self)
        frame3.pack(side = LEFT, anchor= N)

        labelframe1 = LabelFrame(frame3, text="Parameters:")
        labelframe1.pack(side = LEFT, anchor= N, pady=20)

        vel = StringVar()
        label2 = Label(labelframe1, text="Velocity:")
        label2.grid(row=0, column=0, sticky= W, pady=10)
        entry1 = Entry(labelframe1, textvariable=vel)
        entry1.grid(row=1, column=0)
        vel.set(1)
        v = int(entry1.get())
        print v
        label3 = Label(labelframe1, text="Angle:")
        label3.grid(row=2, column=0, sticky= W, pady=10)
        entry2 = Entry(labelframe1)
        entry2.grid(row=3, column=0)

        label4 = Label(labelframe1, text="Resolution(Integer):")
        label4.grid(row=4, column=0, sticky= W, pady=10)
        entry3 = Entry(labelframe1)
        entry3.grid(row=5, column=0)


##        time ,x,y = projectile(10,np.pi/4.,100)
        
        button5 = Button(labelframe1, text="Run!",
                           command=lambda: self.animate_2(v, np.pi/4.,100, fig))
        button5.grid(row=6, column=0, padx=5, pady=25)

    def animate_2(self, vel, ang, n, fig):
        print vel
        time ,X,Y = projectile(vel, ang, n)
        plt.ion()
        ax = fig.add_subplot(111)
        ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y),\
                                                   np.amax(Y)+0.1*np.amin(Y)))
        i=0
        #plt.show()
        while i<len(X) :
            plt.clf()
            plt.plot(X[:i], Y[:i])
            fig.canvas.draw()
            i+=1
        print "complete"
    

class Brownian(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.controller = controller
        self.initUI()
        
    def initUI(self):
        frame0 = Frame(self)
        frame0.pack()

        title = Label(frame0, text="Brownian Motion" ,font=("Comic Sans MS", 25))
        title.pack()
        
        frame1 = Frame(self)
        frame1.pack(side = LEFT, anchor=N)
        
        button1 = Button(frame1, text="Home",
                           command=lambda: self.controller.show_frame("Home"))
        button1.grid(row=0, column=0, padx=5, pady=25)          
       
        button2 = Button(frame1, text="Projectile Motion",
                           command=lambda: self.controller.show_frame("Projectile"))
        button2.grid(row=1, column=0, padx=5, pady=5)  
      
        button3 = Button(frame1, text="Cyclotron Motion",
                           command=lambda: self.controller.show_frame("Cyclotron"))
        button3.grid(row=2, column=0, padx=5, pady=5) 
        
        button5 = Button(frame1, text="Schrodinger Equation",
                           command=lambda: self.controller.show_frame("Schrodinger"))
        button5.grid(row=3, column=0, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(side=LEFT)

        fig = plt.figure(figsize=(4,4), dpi=100)
        canvas = FigureCanvasTkAgg(fig, frame2)
        #canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM)

        frame3 = Frame(self)
        frame3.pack(side = LEFT, anchor= N)

        labelframe1 = LabelFrame(frame3, text="Parameters:")
        labelframe1.pack(side = LEFT, anchor= N, pady=20)

        vel = StringVar()
        label2 = Label(labelframe1, text="Velocity:")
        label2.grid(row=0, column=0, sticky= W, pady=10)
        entry1 = Entry(labelframe1, textvariable=vel)
        entry1.grid(row=1, column=0)
        vel.set(1)
        v = int(entry1.get())
        print v
        label3 = Label(labelframe1, text="Angle:")
        label3.grid(row=2, column=0, sticky= W, pady=10)
        entry2 = Entry(labelframe1)
        entry2.grid(row=3, column=0)

        label4 = Label(labelframe1, text="Resolution(Integer):")
        label4.grid(row=4, column=0, sticky= W, pady=10)
        entry3 = Entry(labelframe1)
        entry3.grid(row=5, column=0)

        button5 = Button(labelframe1, text="Run!",
                           command=lambda: self.animate_2(v, np.pi/4.,100, fig))
        button5.grid(row=6, column=0, padx=5, pady=25)

    def animate_2(self, vel, ang, n, fig):
        print vel
        time ,X,Y = projectile(vel, ang, n)
        plt.ion()
        ax = fig.add_subplot(111)
        ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y),\
                                                   np.amax(Y)+0.1*np.amin(Y)))
        i=0
        #plt.show()
        while i<len(X) :
            plt.clf()
            plt.plot(X[:i], Y[:i])
            fig.canvas.draw()
            i+=1
        print "complete"

class Cyclotron(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.controller = controller
        self.initUI()
        
    def initUI(self):
        frame0 = Frame(self)
        frame0.pack()

        title = Label(frame0, text="Cyclotron Motion" ,font=("Comic Sans MS", 25))
        title.pack()
        
        frame1 = Frame(self)
        frame1.pack(side = LEFT, anchor=N)
        
        button1 = Button(frame1, text="Home",
                           command=lambda: self.controller.show_frame("Home"))
        button1.grid(row=0, column=0, padx=5, pady=25)          
       
        button2 = Button(frame1, text="Projectile Motion",
                           command=lambda: self.controller.show_frame("Projectile"))
        button2.grid(row=1, column=0, padx=5, pady=5)  
      
        button3 = Button(frame1, text="Brownian  Motion",
                           command=lambda: self.controller.show_frame("Brownian"))
        button3.grid(row=2, column=0, padx=5, pady=5) 
        
        button5 = Button(frame1, text="Schrodinger Equation",
                           command=lambda: self.controller.show_frame("Schrodinger"))
        button5.grid(row=3, column=0, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(side=LEFT)

        fig = plt.figure(figsize=(4,4), dpi=100)
        canvas = FigureCanvasTkAgg(fig, frame2)

        canvas.get_tk_widget().pack(side=BOTTOM)

        time ,x,y = projectile(10,np.pi/4.,100)

        
        frame3 = Frame(self)
        frame3.pack(side = LEFT, anchor= N)

        labelframe1 = LabelFrame(frame3, text="Parameters:")
        labelframe1.pack(side = LEFT, anchor= N, pady=20)

        vel = StringVar()
        label2 = Label(labelframe1, text="Velocity:")
        label2.grid(row=0, column=0, sticky= W, pady=10)
        entry1 = Entry(labelframe1, textvariable=vel)
        entry1.grid(row=1, column=0)
        vel.set(1)
        v = int(entry1.get())
        print v
        label3 = Label(labelframe1, text="Angle:")
        label3.grid(row=2, column=0, sticky= W, pady=10)
        entry2 = Entry(labelframe1)
        entry2.grid(row=3, column=0)

        label4 = Label(labelframe1, text="Resolution(Integer):")
        label4.grid(row=4, column=0, sticky= W, pady=10)
        entry3 = Entry(labelframe1)
        entry3.grid(row=5, column=0)


##        time ,x,y = projectile(10,np.pi/4.,100)
        
        button5 = Button(labelframe1, text="Run!",
                           command=lambda: self.animate_2(v, np.pi/4.,100, fig))
        button5.grid(row=6, column=0, padx=5, pady=25)

    def animate_2(self, vel, ang, n, fig):
        print vel
        time ,X,Y = projectile(vel, ang, n)
        plt.ion()
        ax = fig.add_subplot(111)
        ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y),\
                                                   np.amax(Y)+0.1*np.amin(Y)))
        i=0
        #plt.show()
        while i<len(X) :
            plt.clf()
            plt.plot(X[:i], Y[:i])
            fig.canvas.draw()
            i+=1
        print "complete"

class Schrodinger(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.controller = controller
        self.initUI()
        
    def initUI(self):
        frame0 = Frame(self)
        frame0.pack()

        title = Label(frame0, text="Schrodinger Equation" ,font=("Comic Sans MS", 25))
        title.pack()
        
        frame1 = Frame(self)
        frame1.pack(side = LEFT, anchor=N)
        
        button1 = Button(frame1, text="Home",
                           command=lambda: self.controller.show_frame("Home"))
        button1.grid(row=0, column=0, padx=5, pady=25)          
       
        button2 = Button(frame1, text="Projectile Motion",
                           command=lambda: self.controller.show_frame("Projectile"))
        button2.grid(row=1, column=0, padx=5, pady=5)  
      
        button3 = Button(frame1, text="Brownian Motion",
                           command=lambda: self.controller.show_frame("Brownian"))
        button3.grid(row=2, column=0, padx=5, pady=5) 
        
        button5 = Button(frame1, text="Cyclotron Motion",
                           command=lambda: self.controller.show_frame("Cyclotron"))
        button5.grid(row=3, column=0, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(side=LEFT)

##        f = Figure(figsize=(4,4), dpi=100)
##        a = f.add_subplot(111)
##        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
##        global fig
##        plt.ion()
        fig = plt.figure(figsize=(4,4), dpi=100)
        canvas = FigureCanvasTkAgg(fig, frame2)
        #canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM)

##        toolbar = NavigationToolbar2TkAgg(canvas, frame2)
##        toolbar.update()
##        canvas._tkcanvas.pack(side=TOP, anchor= CENTER)

        time ,x,y = projectile(10,np.pi/4.,100)
        #self.animate(x,y, fig)
        #canvas.show()
        
        frame3 = Frame(self)
        frame3.pack(side = LEFT, anchor= N)

        labelframe1 = LabelFrame(frame3, text="Parameters:")
        labelframe1.pack(side = LEFT, anchor= N, pady=20)

        vel = StringVar()
        label2 = Label(labelframe1, text="Velocity:")
        label2.grid(row=0, column=0, sticky= W, pady=10)
        entry1 = Entry(labelframe1, textvariable=vel)
        entry1.grid(row=1, column=0)
        vel.set(1)
        v = int(entry1.get())
        print v
        label3 = Label(labelframe1, text="Angle:")
        label3.grid(row=2, column=0, sticky= W, pady=10)
        entry2 = Entry(labelframe1)
        entry2.grid(row=3, column=0)

        label4 = Label(labelframe1, text="Resolution(Integer):")
        label4.grid(row=4, column=0, sticky= W, pady=10)
        entry3 = Entry(labelframe1)
        entry3.grid(row=5, column=0)


##        time ,x,y = projectile(10,np.pi/4.,100)
        
        button5 = Button(labelframe1, text="Run!",
                           command=lambda: self.animate_2(v, np.pi/4.,100, fig))
        button5.grid(row=6, column=0, padx=5, pady=25)

    def animate_2(self, vel, ang, n, fig):
        print vel
        time ,X,Y = projectile(vel, ang, n)
        plt.ion()
        ax = fig.add_subplot(111)
        ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y),\
                                                   np.amax(Y)+0.1*np.amin(Y)))
        i=0
        #plt.show()
        while i<len(X) :
            plt.clf()
            plt.plot(X[:i], Y[:i])
            fig.canvas.draw()
            i+=1
        print "complete"

def animate0(X,Y, fig):
##        fig = plt.figure()
    #ax = plt.axes(xlim=(np.amin(X), np.amax(X)), ylim=(np.amin(Y)-0.1*np.amin(Y),\
##                                                       np.amax(Y)+0.1*np.amin(Y)))
    ax = fig.add_subplot(111)
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([],[])
        return line,
    def animate(i):
        x = X[:i]
        y = Y[:i]
        line.set_data(x, y)
        return line,
    
    #canvas.show()
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1000, interval=10, blit=True, repeat=False)
    print 'reached'
    #plt.show()



def animate_2(x,y, fig):
    plt.ion()
    ax = fig.add_subplot(111)
    i=0
    #plt.show()
    while i<len(x) :
        plt.clf()
        plt.plot(x[:i], y[:i])
        fig.canvas.draw()
        i+=1
    print "complete"

def animate1(fig):
    x = np.arange(0, 2*np.pi, 0.01) 
    def animate(i):
        line.set_ydata(np.sin(x+i/10.0))  # update the data
        return line,
    ax = fig.add_subplot(111)
    line, = ax.plot(x, np.sin(x))
    ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
    print 'ditch'

##def init():
##    line.set_data([],[])
##    return line,
##
##def animate(i):
##    x = X[:i]
##    y = Y[:i]
##    line.set_data(x, y)
##    return line,

def main():
    app = MainApp()
##    x = np.arange(0, 2*np.pi, 0.01) 
##    def animate(i):
##        line.set_ydata(np.sin(x+i/10.0))  # update the data
##        return line,
##    ax = fig.add_subplot(111)
##    line, = ax.plot(x, np.sin(x))
##    ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
##    ax = fig.add_subplot(111)
##    line, = ax.plot([], [], lw=2)
##
##    def init():
##        line.set_data([],[])
##        return line,
##    def animate(i):
##        x = X[:i]
##        y = Y[:i]
##        line.set_data(x, y)
##        return line,
##
##    anim = animation.FuncAnimation(fig, animate, init_func=init,
##                                   frames=1000, interval=10, blit=True, repeat=False)
    app.mainloop() 
    #print 'finished'

if __name__ == '__main__':
    main()  
