from tkinter import *
from tkinter import ttk 

import pint

class Calculator:
    def __init__(self, title, labels, textvars, h, root):
        self.title = title
        self.labels = labels
        self.textvars = textvars
        self.height = h
        self.root = root
        self.ureg = pint.UnitRegistry()

        self.set_root()
        self.set_column1()
        self.set_column2()
        self.set_column3()
        self.set_calc()
        self.set_out()
        self.set_menu()
        self.keys()

    def calculate(self):
        return 000000

    def display(self):
        self.output.config(state=NORMAL)
        self.output.delete(0, END)
        try:
            self.output.insert(0, '{0:.2f}'.format(self.calculate()))   
        except TclError:
             self.output.insert(0, "Please enter numbers in every field")
        except ZeroDivisionError:
            self.output.insert(0, "Dimensions cannot be 0")
        self.output.config(state=DISABLED)

    def display_2(self, event):
        self.display()

    def display_help(self):
        pass

    def move_up(self, event):
        current = self.root.focus_get()
        new = self.entries[self.entries.index(current)-1]
        new.focus_set()

    def move_down(self, event):
        current = self.root.focus_get()
        try:
            new = self.entries[self.entries.index(current)+1]
        except IndexError:
            new = self.entries[0]
        finally:
            new.focus_set()

    def set_root(self):
        self.root.title(self.title)
        self.root.minsize(width=300, height=self.height)
        self.row1 = Frame(self.root)
        self.row1.pack(side=TOP, expand=YES, fill=BOTH)

    def set_column1(self):
        column1 = Frame(self.row1)
        column1.pack(side=LEFT, expand=YES, fill=BOTH)

        for label in self.labels:
            ttk.Label(column1, text=label).pack(side=TOP, expand=YES, fill=BOTH)

    def set_column2(self):
        column2 = Frame(self.row1)
        column2.pack(side=LEFT, expand=YES, fill=BOTH)

        self.entries = []
        for var in self.textvars:
            e = ttk.Entry(column2, width=7, textvariable=var)
            self.entries.append(e)
            e.pack(side=TOP, expand=YES, fill=BOTH)
            e.delete(0, END)

        self.entries[0].focus_set()

    def set_column3(self):
        self.column3 = Frame(self.row1)
        self.column3.pack(side=LEFT, expand=YES, fill=BOTH)
            
    def set_calc(self):
        row2 = Frame(self.root)
        row2.pack(side=TOP, expand=YES, fill=BOTH)

        calc_button = ttk.Button(row2, text = 'Calculate', command=self.display)
        calc_button.pack(anchor=E, side=TOP, expand=YES, fill=BOTH)

    def set_out(self):
        self.row3 = Frame(self.root)
        self.row3.pack(side=BOTTOM, expand=YES, fill=BOTH)

        self.output = ttk.Entry(self.row3, width=7, state=DISABLED)
        self.output.pack(anchor=E, side=LEFT, expand=YES, fill=BOTH)

    def set_menu(self):
        mb = Menu(self.root)
        mb.add_command(label='Help', command=self.display_help)
        self.root.config(menu=mb)

    def keys(self):
        self.root.bind('<Return>', self.display_2)
        self.root.bind('<Down>', self.move_down)
        self.root.bind('<Up>', self.move_up)

    def add_input_units(self, unit, units):
        mb = OptionMenu(self.column3, unit, *units)
        mb.pack(expand=NO, fill=X, anchor=N)

    def add_output_units(self, units):
        self.unit_out = StringVar()
        self.unit_out.set(units[0])

        self.units_out = units
        mb_out = OptionMenu(self.row3, self.unit_out, *self.units_out)
        mb_out.pack(side=TOP)



