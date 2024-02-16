import math
import logging

class Coords():
    x = 0
    y = 0 


class Circle():
    pi = 3.141
    radius = 0.0
    coords = Coords()
    color = ""
    filled = False
    positions = []

    def __init__(self, r):
        logging.warning('New Circle Created')
        self.radius = r
        


    def circumfernce(self):
        return self.radius * Circle.pi * 2
    
    def __myFunc(self):
        print(f"myFunc was invoked - Radius - {self.radius}")

