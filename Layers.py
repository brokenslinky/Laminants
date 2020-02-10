import Fabrics
from Fabrics import *

class Layer:
    fabric: Fabric
    matrix: Material
    ratio = .50

    def __init__(self, fabric=None, matrix=epoxy, ratio=.5):
        self.fabric = fabric
        self.ratio = ratio
        self.matrix = matrix
        
    @property
    def modulus(self):
        """The effective elastic modulus of this composite Layer (GPa)"""
        import math
        tmp = 0.
        for orientation in self.fabric.orientation:
            tmp += math.cos(orientation * math.pi / 180.) ** 4
        tmp *= self.ratio * self.fabric.material.modulus / len(self.fabric.orientation)
        tmp += (1. - self.ratio) * self.matrix.modulus
        return tmp

    @property
    def strength(self):
        """The effective ultimate strength of this composite Layer (MPa)"""
        # The limiting factor in strength is how much the Materials can stretch
        return self.modulus * self.elongation * 1000.

    @property
    def elongation(self):
        """The maximum elongation of this Layer before it yields or breaks"""
        return min([self.fabric.material.elongation, self.matrix.elongation])

    @property
    def density(self):
        """The density of this composite Layer (g/cc)"""
        return self.ratio * self.fabric.material.density + (1. - self.ratio) * self.matrix.density

    @property
    def thickness(self):
        """The thickness of this Layer"""
        if self.fabric.material.density == 0.:
            return self.fabric.thickness
        thicknessDueToFabric = .001335 * self.fabric.weight / self.fabric.material.density
        thicknessDueToMatrix = .001335 * ((1. - self.ratio) / self.ratio) * self.fabric.weight / self.matrix.density
        return thicknessDueToFabric + thicknessDueToMatrix