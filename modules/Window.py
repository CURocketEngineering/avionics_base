from tkinter import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Window:
    def __init__(self):
        self.win = Tk()
        self.win.title("Avionics Base Station")
        self.win.geometry("1280x720")

        self.menu_frame = Frame(self.win)
        self.graphs_frame = Frame(self.win)
        self.scale_frame = Frame(self.win)
        self.grid(self.menu_frame, 0,0,1,7)
        self.grid(self.graphs_frame, 1,0,3,7)
        self.grid(self.scale_frame, 0,7,8,1)
        
        self.lbl = Label(self.menu_frame, text="Test")
        self.grid(self.lbl, 0, 0, 1, 1)
        #self.lbl.grid(column=0, row=0)

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel("Test")
        ax.set_ylabel("Test Test Test")
        ax.grid()
        graph = FigureCanvasTkAgg(fig, master=self.graphs_frame)
        self.grid(graph.get_tk_widget(), 0,0,1,1)

    def __call__(self):
        self.win.mainloop()

    def grid(self, part, x, y, w, h):
        return part.grid(
            column=x,
            row=y,
            columnspan=w,
            rowspan=h
        )
