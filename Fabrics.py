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
    name = "Twill Carbon",
    description = "Carbon 2x2 Twill Weave",
    material = carbon,
    thickness = 0.009,
    weight = 5.9, 
    orientation = [0., 90.])

biax = Fabric(
    name = "biax",
    description = "45° Twill Weave Carbon Fiber",
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
    thickness = 0.009,
    weight = 29.5)

kevlar = Fabric(
    name = "Kevlar 4HS",
    description = "Kevlar 49 4-Harness Satin Weave",
    material = kevlar49,
    thickness = 0.1,
    weight = 5.,
    orientation = [0., 90.])

kevlarBiax = Fabric(
    name = "Kevlar 4HS",
    description = "±45° Kevlar 49 4-Harness Satin Weave",
    material = kevlar49,
    thickness = 0.1,
    weight = 5.,
    orientation = [45., -45.])

triax = Fabric(
    name = "triax",
    description = "0°,±60° Quasi-Isotropic Carbon Fiber",
    material = carbon,
    thickness = 0.014,
    weight = 8,
    orientation = [0., 60., -60.])

fabric_library = {
    "1": twill, "2": biax, "3": uni, "4": soricXf, "5": kevlar, "6": kevlarBiax, "7": triax
    }

def select_fabric():
    response = input("Choose a fabric. (ls for list)\n")
    def list_fabrics():
        for tag in fabric_library:
            print(f"{tag} : {fabric_library[tag].name} - {fabric_library[tag].description}")
        print("0 : Done")
    if response == "ls":
        list_fabrics()
        return select_fabric()
    if response == "0":
        return 0
    if response in fabric_library:
         return fabric_library[response]
    print("Invalid selection. Please choose from the list:")
    list_fabrics()
    return select_fabric()
