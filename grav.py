from math import *
import time

import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Constants
G = 6.67430 * (10 ** -11) # Universal Gravitational Constant
M = 1000000 # Million
K = 1000 # Thousand

# Distance formula to find the distance between two bodies
def findr(x1, x2, y1, y2):
    x = x2-x1
    y = y2-y1
    return sqrt(x**2 + y**2), x, y

# Calculate the gravitational force via its formula
def gforce(m1, m2, r):
    if r == 0:
        return 0
    return (G*m1*m2)/(r**2)

class body:
    instance = []
    names = []
    def __init__(self, mass, radius, xpos, ypos, xvel, yvel, color, name):
        self.__class__.instance.append(self)
        self.__class__.names.append(name)
        self.mass = mass
        self.radius = radius
        self.xpos = xpos # x position
        self.ypos = ypos # y position
        self.xvel = xvel # x velocity
        self.yvel = yvel # y velocity
        self.color = color # color for graphing
        self.xacc = 0 # x acceleration
        self.yacc = 0 # y acceleration
        self.xnetforce = 0 # x net force
        self.ynetforce = 0 # y net force
        self.xposes = [xpos] # x positions
        self.yposes = [ypos] # y positions

    def forces(self, object, r, x, y):
        force = gforce(self.mass, object.mass, r) # Gravitational force between the two objects
        if r > 0:
            self.xnetforce += (force/r)*x # Add x-component of gravitational force between the two objects
            self.ynetforce += (force/r)*y # Add y-component of gravitational force between the two objects

    def calcforces(self):
        # Calculate the forces between a body and all other bodies
        for i in body.instance:
            if i != self:
                self.forces(i, *findr(self.xpos, i.xpos, self.ypos, i.ypos))

    def calcacc(self):
        self.xacc = self.xnetforce / self.mass
        self.yacc = self.ynetforce / self.mass

    def calcvel(self):
        self.xvel = self.xvel + t * self.xacc # v final = v inital + a * t
        self.yvel = self.yvel + t * self.yacc

    def calcpos(self):
        self.xpos = self.xpos + (self.xvel * t - 0.5 * self.xacc * (t ** 2)) # d = v final * t - 0.5 * a * t ^ 2
        self.ypos = self.ypos + (self.yvel * t - 0.5 * self.yacc * (t ** 2))

    def calc(self):
        self.xnetforce = 0 # Reset net forces to zero
        self.ynetforce = 0
        body.calcforces(self)
        body.calcacc(self)
        body.calcvel(self)

def calculations():
    for i in body.instance:
        i.calc()

def updatepos():
    for i in body.instance:
        i.calcpos()
        i.xposes.append(i.xpos)
        i.yposes.append(i.ypos)

def getPlots():
    args = []
    for i in body.instance:
        args.append(i.xposes)
        args.append(i.yposes)
        args.append(i.color)
    return args

def plot():
    fig, ax = plt.subplots()
    ax.plot(*getPlots(), marker="o", ms="1")
    ax.set_xlabel("x-position(m)")
    ax.set_ylabel("y-position(m)")
    # plt.plot(*getPlots())
    plt.legend(body.names)
    # plt.xlabel("x-position")
    # plt.ylabel("y-position")
    plt.show()

# Bodies to simulate
# Object = body(mass in kilograms, radius in meters, x-position in meters, y-position in meters, x-velocity in meters per second, y-velocity in meters per second, color for graphing in hex-code, name of object for graph legend)
# Solar System
# THE SUN
sunSpeedx = 0.0 # Adjust the speed of the sun
sunSpeedy = 0
Sun = body(1.989e30, 696340.0*K, 0.0, 0.0, sunSpeedx, sunSpeedy, "#FF0000", "Sun")

#Mercury = body(3.285e23, 2439.7*K, 57.91*M*K, 0.0, 0.0+sunSpeedx, 47.36*K+sunSpeedy, "#EBEBEB", "Mercury")

# Earth and stuff
Earth = body(5.972e24, 6317.0*K, 147.16*M*K, 0.0, 0+sunSpeedx, 29.78*K+sunSpeedy, "#0000FF", "Earth")
Moon = body(7.34767309e22, 1737.4*K, 147.16*M*K, 384400.0*K, -1023.056+sunSpeedx, 29.78*K+sunSpeedy, "#808080", "Moon")

# Mars and stuff
# Mars = body(6.4171e23, 3389.5*K, 227.96*M*K, 0, 0+sunSpeedx, 26.50*K+sunSpeedy, "#BC2732", "Mars")
# Phobos = body(1.0659e16, 11.2667*K, 227.96*M*K, 9376.0*K, -2.138*K+sunSpeedx, 26.50*K+sunSpeedy, "#998b82", "Phobos")
# Deimos = body(1.4762e15, 6.2*K, 227.96*M*K, 23463.2*K, -1.3513*K+sunSpeedx, 26.50*K+sunSpeedy, "#FFFFFF", "Deimos")

# Random stuff
# Object1 = body(1000*M, 1, 100000, 0, 0, 100, "#FF0000", "Object1")
# Object2 = body(1000*M, 1, 0, 0, 0, 100, "#00FF00", "Object2")
# Object3 = body(1000, 1, -100, -100, 1, 0, "#0000FF", "Object3")
# Object4 = body(1000, 1, 1, -1, 0, 0, "#FFFF00", "Object4")

# Earth = body(5.972e24, 6317.0*K, 0.0, 0.0, 0.0, 0.0, "#0000FF", "Earth")
# Satellite = body(7000, 1, 0.0, 20000*K, 11*K, 0.0, "#CCCCCC", "Satellite")

# Simulation parameters
runtime = 360*3600*24 # Total time to simulate in seconds
ttotal = 0 # Total time elapsed in seconds
t = 450 # Time between each calculation in seconds

if __name__ == "__main__":
    
    start = time.time()
    while ttotal <= runtime:
        # print("({}s {} {} {}m/s(x) {}m/s(y) {}m/s)".format(ttotal, Earth.xpos, Earth.ypos, Earth.xvel, Earth.yvel, sqrt(Earth.xvel**2 + Earth.yvel**2)))
        # Earth.calc()
        # Sun.calc()
        # Earth.calcpos()
        # Sun.calcpos()
        calculations()
        updatepos()
        ttotal += t
    print("Completed in {}s".format(time.time() - start))
    plot()
    

# print(0.0, -147.16*1000000*1000)    