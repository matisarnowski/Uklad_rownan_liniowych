from my_tkinter import *


class LinearEquations:

    def __init__(self, a1, b1, c1, a2, b2, c2):
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.a2 = a2
        self.b2 = b2
        self.c2 = c2

    def is_compute(self):
        w = self.a1 * self.b2 - self.a2 * self.b1
        if w != 0:
            return True
        else:
            return False

    def equal_equations_linear(self):
        w = self.a1 * self.b2 - self.a2 * self.b1
        if w != 0:
            return tuple([(self.c1 * self.b2 - self.b1 * self.c2) / w,
                          (self.c2 * self.a1 - self.a2 * self.c1) / w])
        else:
            return tuple("Układ równań nie ma rozwiązań.",
                         "Proste są do siebie równoległe")
