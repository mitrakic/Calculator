from tkinter import *
from tkinter import ttk

from AirframeVolume import AirframeVolume
from FinFlutter import FinFlutter
from KineticEnergy import KineticEnergy
from ThrustToWeight import ThrustToWeight

def open_flutter():
    f = FinFlutter(root)

def open_airframe():
    a = AirframeVolume(root)

def open_kinetic():
    k = KineticEnergy(root)

def open_thrust():
    t = ThrustToWeight(root)

root = Tk()
root.title("Calculator")
root.minsize(200, 200)

flutter = ttk.Button(root, text="Fin Flutter", command=open_flutter)
flutter.pack(side=TOP, expand=YES, fill=BOTH)

airframe = ttk.Button(root, text="Airframe Volume", command=open_airframe)
airframe.pack(side=TOP, expand=YES, fill=BOTH)

kinetic = ttk.Button(root, text="Kinetic Energy", command=open_kinetic)
kinetic.pack(side=TOP, expand=YES, fill=BOTH)

thrust = ttk.Button(root, text="Thrust to Weight", command=open_thrust)
thrust.pack(side=TOP, expand=YES, fill=BOTH)

root.mainloop()
