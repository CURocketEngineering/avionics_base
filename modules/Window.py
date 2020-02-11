from tkinter import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from random import randint


class Window:
    def __init__(self, data, time):
        self.data = data
        self.time = time

        self.win = Tk()
        self.win.title("Avionics Base Station")
        self.win.geometry("1280x720")

        self.menu_frame = Frame(self.win)
        self.graphs_frame = Frame(self.win)
        self.scale_frame = Frame(self.win)
        self.grid(self.menu_frame, 0,0,1,7,4,8)
        self.grid(self.graphs_frame, 1,0,3,7,4,8)
        self.grid(self.scale_frame, 0,7,8,1,4,8)
        
        """
        self.lbl = Label(self.menu_frame, text="Test")
        self.grid(self.lbl, 0, 0, 1, 1, 1, 8)
        """

        self.all_graphs = {}
        self.all_options = {}

        for key in data:
            self.add_graph(
                time,
                data[key],
                title=key
            )
            but = Button(self.menu_frame, text=key)
            self.grid(but, )


    def __call__(self):
        self.win.mainloop()

    def grid(self, part, x, y, w, h, maxw, maxh):
        return part.place(
            relx=x/maxw,
            rely=y/maxh,
            relheight=h/maxh,
            relwidth=w/maxw
        )
        return part.grid(
            column=x,
            row=y,
            columnspan=w,
            rowspan=h
        )

    def add_menu_option(self, option):
        pass

    def add_graph(
            self,
            x,
            y,
            title="",
            xlabel="",
            ylabel=""
    ):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.grid()
        ax.plot(x,y)
        #fig.tight_layout(w_pad=0.1)
        """
        fig.subplots_adjust(
            left=0,
            bottom=0,
            right=1,
            top=1,
            wspace=0.5,
            hspace=0.5
        )
        """
        fig.subplots_adjust(bottom=0.2,left=0.2)
        graph = FigureCanvasTkAgg(
            fig,
            master=self.graphs_frame
        )
        if len(self.all_graphs) < 4: layer = 0
        else: layer = 1
        self.grid(
            graph.get_tk_widget(),
            len(self.all_graphs)%4,
            layer,
            1,
            1,
            4,
            2,
        )
        self.all_graphs[title] = {
            "graph": graph,
            "fig": fig,
        }
