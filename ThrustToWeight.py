from tkinter import *
from tkinter import ttk 

from Calculator import Calculator

import math
import pint

class ThrustToWeight(Calculator):
    def __init__(self, root):
        self.root = Toplevel(root)
        self.thrust = DoubleVar()
        self.weight = DoubleVar()

        super(ThrustToWeight, self).__init__("Thrust To Weight", ["Thrust", "Weight"], 
        	[self.thrust, self.weight], 120, self.root)

        self.ureg.define("Newton = 1 * kg * meter * second**2")
        self.ureg.define("PoundForce = 4.4482216152605 * Newton")
        self.t_units = ["Newton", "PoundForce"]
        self.w_units = ["kg", "grams", "lbs", "oz"]

        self.t_unit = StringVar()
        self.w_unit = StringVar()
        self.t_unit.set("Newton")
        self.w_unit.set("kg")

        self.add_input_units(self.t_unit, self.t_units)
        self.add_input_units(self.w_unit, self.w_units)

        #System.out.println(2 * self.ureg("Pound Force"))

    def calculate(self):
        thrust = (self.thrust.get() * self.ureg(self.t_unit.get())).to(self.ureg("Newton"))
        weight = (self.weight.get() * self.ureg(self.w_unit.get())).to(self.ureg("kg"))
        g = 9.80665 * self.ureg("meters / second**2")
        return (thrust / (weight * g)).magnitude
