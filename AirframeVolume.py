from tkinter import *
from tkinter import ttk 

from Calculator import Calculator

import math
import pint

class AirframeVolume(Calculator):
    def __init__(self, root):
        self.root = Toplevel(root)
        self.outer_d = DoubleVar()
        self.inner_d = DoubleVar()
        self.thickness = DoubleVar()

        super(AirframeVolume, self).__init__("Volume", ["Outer Diameter",
        	"Inner Diameter", "Thickness"], [self.outer_d, self.inner_d,
        	self.thickness], 160, self.root)

        self.input_units = ["in", "cm"]
        self.outer_unit = StringVar()
        self.inner_unit = StringVar()
        self.thickness_unit = StringVar()

        units = [self.outer_unit, self.inner_unit, self.thickness_unit]
        for u in units:
            u.set("in")
            self.add_input_units(u, self.input_units)

        self.add_output_units(["in**3", "cm**3"])

    def to_inches(self, value, unit):
        return (value.get() * self.ureg(unit.get())).to(self.ureg("in"))

    def calculate(self):
        outer = self.to_inches(self.outer_d, self.outer_unit)
        inner = self.to_inches(self.inner_d, self.inner_unit)
        thickness = self.to_inches(self.thickness, self.thickness_unit)

        volume = thickness * math.pi * ((outer**2) - (inner**2))
        return volume.to(self.ureg(self.unit_out.get())).magnitude

    def display_help(self):
        wind = Toplevel(self.root)
        about_out = "Outer Diameter: The outside diameter of the body tube, centering ring. or bulkhead.\n"
        about_in = "Inner Diameter: The inner diameter of the body tube, centering ring, or bulkhead. If there is none, enter 0.\n"
        about_thick = "Thickness: The thickness or height of the body tube, centering ring, or bulkhead.\n"
        about_output = "Output: The volume of the body tube, centering ring, or bulkhead.\n"
        about_general = "Do not enter 0 for 'Outer Diameter' or 'Thickness.' Do not enter negative numbers. Do not enter Inner Diameters larger than the Outer Diameter."
        msg = Text(wind, wrap=WORD, spacing1=10)

        msg.insert(INSERT, about_out)
        msg.insert(INSERT, about_in)
        msg.insert(INSERT, about_thick)
        msg.insert(INSERT, about_output)
        msg.insert(INSERT, about_general)
        msg.pack(expand=YES, fill=X, anchor=N)

#a = AirframeVolume()