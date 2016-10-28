from tkinter import *
from tkinter import ttk 

from Calculator import Calculator

import math
import pint

class KineticEnergy(Calculator):
    def __init__(self, root):
        self.root = Toplevel(root)
        self.velocity  = DoubleVar()
        self.mass = DoubleVar()

        super(KineticEnergy, self).__init__("Kinetic Energy", ["Velocity", "Mass"], 
        	[self.velocity, self.mass], 120, self.root)

        self.ureg.define("f = feet")
        self.ureg.define("ftlbs = kg * meters**2 * seconds**-2 * 1.35581795")
        self.v_units = ["m/s", "f/s"]
        self.m_units = ["kg", "grams", "lbs", "oz"]
        self.out_units = ["joules", "ftlbs"]

        self.v_unit = StringVar()
        self.m_unit = StringVar()

        self.v_unit.set("m/s")
        self.m_unit.set("kg")

        self.add_input_units(self.v_unit, self.v_units)
        self.add_input_units(self.m_unit, self.m_units)
        self.add_output_units(self.out_units)

    def calculate(self):
        vel = (self.velocity.get() * self.ureg(self.v_unit.get())).to(self.ureg("m/s"))
        mass = (self.mass.get() * self.ureg(self.m_unit.get())).to(self.ureg("kg"))

        ke = 0.5 * mass * (vel**2)
        return ke.to(self.ureg(self.unit_out.get())).magnitude

    def display_help(self):
        wind = Toplevel(self.root)
        
        about_v = "Velocity: The speed of the vehicle.\n"
        about_m = "Mass: The mass of the vehicle or section of the vehicle.\n"
        about_out = "Output: The kinetic energy of the vehicle in either Joules (Newton Meters) or Foot-Pounds.\n"
        
        msg = Text(wind, wrap=WORD, spacing1=10)
        msg.insert(INSERT, about_v)
        msg.insert(INSERT, about_m)
        msg.insert(INSERT, about_out)
        msg.pack(expand=YES, fill=X, anchor=N)


