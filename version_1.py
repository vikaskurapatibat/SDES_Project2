#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from ttk import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class MainApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("700x500+200+10")
        self.title("Physics Simulator")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Projectile):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
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
##        f = Frame(self, height = 50, width = 100, height = 100)
##        f.pack() 
        #f.place(x = x, y = y)
##        frame1 = Frame(self)
##        frame1.pack(fill=X)
        photo = PhotoImage(file="atom1.gif", width = 100, height=100)
        #photo.zoomout(0.7,0.7)
        label1 = Label(self, image=photo)
        label1.photo = photo
        label1.pack(pady=5)
        
        var = StringVar()
        var.set("Please select one of the below problems to simulate")
        label2 = Label(self, text="Please select one of the below problems to simulate" )
  
        label2.pack()
 
        button1 = Button(self, text="Projectile",
                           command=lambda: self.controller.show_frame("Projectile"))
        button1.pack(padx=5, pady=5)          
       
        button2 = Button(self, text="Kinetic Theory of Gases",
                           command=lambda: self.controller.show_frame("Projectile"))
        button2.pack(padx=5, pady=5) 
        
##        frame2 = Frame(self)
##        frame2.pack(fill=X)
        
        button3 = Button(self, text="Cyclotron Motion",
                           command=lambda: self.controller.show_frame("Projectile"))
        button3.pack(padx=5, pady=5)

        button4 = Button(self, text="Charged Particles",
                           command=lambda: self.controller.show_frame("Projectile"))
        button4.pack(padx=5, pady=5) 
        
##        frame3 = Frame(self)
##        frame3.pack(fill=BOTH, expand=True)
        button5 = Button(self, text="Schrodinger Equation",
                           command=lambda: self.controller.show_frame("Projectile"))
        button5.pack(padx=5, pady=5)        
        
              
class Projectile(Frame):
  
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.controller = controller
        self.initUI()
        
    def initUI(self):
      
##        self.parent.title("Review")
##        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(side = LEFT)
        
        button1 = Button(frame1, text="Projectile",
                           command=lambda: self.controller.show_frame("Projectile"))
        button1.grid(row=0, column=0, padx=5, pady=5)          
       
        button2 = Button(frame1, text="Kinetic Theory of Gases",
                           command=lambda: self.controller.show_frame("Projectile"))
        button2.grid(row=1, column=0, padx=5, pady=5)  
      
        button3 = Button(frame1, text="Cyclotron Motion",
                           command=lambda: self.controller.show_frame("Projectile"))
        button3.grid(row=2, column=0, padx=5, pady=5)

        button4 = Button(frame1, text="Charged Particles",
                           command=lambda: self.controller.show_frame("Projectile"))
        button4.grid(row=3, column=0,padx=5, pady=5) 
        
##        frame3 = Frame(self)
##        frame3.pack(fill=BOTH, expand=True)
        button5 = Button(frame1, text="Schrodinger Equation",
                           command=lambda: self.controller.show_frame("Projectile"))
        button5.grid(row=4, column=0, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(side=LEFT)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, frame2)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, frame2)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, expand=True)
        
        frame3 = Frame(self)
        frame3.pack(side = LEFT)

        label1 = Label(frame3, text="Parameters:")
        label1.grid(row=0, column=0, sticky= W)
              

def main():
  
    app = MainApp()
    app.mainloop()
##    root.mainloop()  


if __name__ == '__main__':
    main()  
