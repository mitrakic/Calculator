from tkinter import *
from tkinter import ttk 

from Calculator import Calculator

import math
import pint

class FinFlutter(Calculator):
    def __init__(self, root):
        self.root = Toplevel(root)
        
        self.altitude = DoubleVar()
        self.shear = DoubleVar()
        self.thickness = DoubleVar()
        self.root_chord = DoubleVar()
        self.tip_chord = DoubleVar()
        self.semi_span = DoubleVar()
        self.ground_pressure = 14.7
        self.ground_sound = 1116.8

        super(FinFlutter, self).__init__("Fin Flutter", ["Altitude", "Shear Modulus",
            "Fin Thickness", "Root Chord", "Tip Chord", "Semi Span"], 
            [self.altitude, self.shear, self.thickness, self.root_chord, self.tip_chord, self.semi_span],
     	    300, self.root)

        self.ureg.define("f = feet")
        self.ureg.define("mach = feet / 0.000895706603191 / s")

        self.unit_alt = StringVar(self.column3)
        self.unit_alt.set("feet")
        self.units_alt = ["feet", "m", "km", "mi"]

        self.unit_shear = StringVar(self.column3)
        self.unit_shear.set("psi")

        self.add_input_units(self.unit_alt, self.units_alt)
        self.add_input_units(self.unit_shear, ["psi"])

        self.add_output_units(["f/s", "m/s", "mph", "kph", "mach"])

    def output_units(self):
        self.unit_out = StringVar(self.row3)
        self.unit_out.set("f/s")

        self.units_out = ["f/s", "m/s", "mph", "kph", "mach"]
        mb_out = OptionMenu(self.row3, self.unit_out, *self.units_out)
        mb_out.pack(side=TOP)

    def display_help(self):
        wind = Toplevel(self.root)
        about_alt = "Altitude: The altitude at which the vehicle reaches maximum velocity. If unknown, set to 0.\n"
        about_shear = "Shear Modulus: The shear modulus of the fin material. MUST be in PSI.\n" 
        about_dim = "The next 4 values can be in any unit, so long as all 4 units are the same.\n"
        about_flutter = ("Output: This is the velocity at which the vehicle will begin to experience flutter." + 
        	" Changes should be made if the vehicle's maximum velocity is within 10% of this.")
        msg = Text(wind, wrap=WORD, spacing1=10)
        msg.insert(INSERT, about_alt)
        msg.insert(INSERT, about_shear)
        msg.insert(INSERT, about_dim)
        msg.insert(INSERT, about_flutter)
        msg.pack(expand=YES, fill=X, anchor=N)

    def calc_pressure(self):
        alt = self.altitude.get() * self.ureg(self.unit_alt.get())
        return self.ground_pressure*math.exp(alt.to(self.ureg("f")).magnitude/(-26500))

    def calc_speed_of_sound(self):
        alt = self.altitude.get() * self.ureg(self.unit_alt.get())
        return self.ground_sound*math.exp(alt.to(self.ureg("f")).magnitude/-(265000))

    def calc_taper(self):
        return self.tip_chord.get() / self.root_chord.get()

    def calc_area(self):
        return ((self.root_chord.get() + self.tip_chord.get()) * self.semi_span.get()/2)

    def calc_aspect(self):
        return self.semi_span.get()**2 / self.calc_area()

    def calculate(self):
        taper = self.calc_taper()
        aspect = self.calc_aspect()
        t1 = math.sqrt(self.ground_pressure / self.calc_pressure()) * self.calc_speed_of_sound()
        t2 = math.sqrt(self.shear.get() / self.ground_pressure)
        t3_1 = ((self.thickness.get()/self.root_chord.get())/aspect)**3
        t3_2 = (2+aspect)/(1+taper)
        t3 = math.sqrt(t3_1*t3_2)
        velocity = 1.223 * t1 * t2 * t3 * self.ureg("f/s")
        return velocity.to(self.ureg(self.unit_out.get())).magnitude
