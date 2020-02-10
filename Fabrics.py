
import Materials
from Materials import *

class Fabric:
    """A reinforcement fabric for composites"""
    _name: str
    @property 
    def name(self):
        """The name of this Material"""
        return self._name

    _material: Material
    @property
    def material(self): 
        """The Material this Fabric is made from"""
        return self._material

    _thickness: float
    @property 
    def thickness(self):
        """Thickness of this Material (inches)"""
        return self._thickness

    _orientation: [float, float]
    @property
    def orientation(self):
        """Weave angles of this fabic ([degrees, degrees])"""
        return self._orientation

    _weight: float
    @property
    def weight(self):
        """Weight of this fabic (oz / yd^2)"""
        return self._weight

    _description: str
    @property
    def description(self):
        if self._description != None:
            return self._description
        else:
            return ""

    def __init__(self, material=None, thickness=0., orientation=[0.,90.], weight=0., name=None, description=None):
        if material == None:
            self._material = space
        else:
            self._material = material
        self._thickness = thickness
        self._orientation = orientation
        self._weight = weight
        self._name = name
        self._description = description

twill = Fabric(
    name = "twill",
    description = "2x2 Twill Weave Carbon Fiber",
    material = carbon,
    thickness = 0.009,
    weight = 5.9, 
    orientation = [0., 90.])

biax = Fabric(
    name = "biax",
    description = "45° Twil Weave Carbon Fiber",
    material = carbon,
    thickness = 0.009,
    weight = 5.9,
    orientation = [45., -45.])

uni = Fabric(
    name = "uni",
    description = "Unidirectional T700 Carbon Fiber",
    material = carbon_T700,
    thickness = 0.021,
    weight = 8.8,
    orientation = [0.])

soricXf = Fabric(
    name = "soricXf",
    description = "Lightweight Filler Mat",
    thickness = 0.07874,
    weight = 29.5)