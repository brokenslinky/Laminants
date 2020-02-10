
import Layers
from Layers import *

class Laminant:
    layers: [Layer]

    def __init__(self, layers):
        self.layers = layers

    @property
    def stiffness(self):
        """The stiffness of this Laminant along the grain (kN/mm)"""
        _stiffness = 0.
        for layer in self.layers:
            _stiffness += layer.modulus * layer.thickness * 25.4
        return _stiffness

    @property
    def elongation(self):
        """The maximum elongation of this Laminant along the grain (unitless)"""
        _elongation = 1.
        for layer in self.layers:
            if layer.elongation < _elongation:
                _elongation = layer.elongation
        return _elongation

    @property
    def strength(self):
        """The strength of this Laminant along the grain (kN/mm)"""
        _strength = 0.
        for layer in self.layers:
            _strength += self.elongation * layer.modulus * layer.fabric.thickness * 25.4
        return _strength

    @property
    def thickness(self):
        _thickness = 0.
        for layer in self.layers:
            _thickness += layer.thickness
        return _thickness

    @property
    def density(self):
        """The net density of this Laminant (g/cc)"""
        _density = 0.
        for layer in self.layers:
            _density += layer.density * layer.thickness
        _density /= self.thickness
        return _density

if __name__ == "__main__":
    emptyScaffold = Fabric(thickness=.018, orientation=[0.])
    pureSteel = Laminant([Layer(fabric=emptyScaffold, matrix=steel, ratio=0.)])
    pureAluminum = Laminant([Layer(fabric=emptyScaffold, matrix=aluminum, ratio=0.)])
    isoCarbon = Laminant([Layer(fabric=twill), Layer(fabric=biax)])
    offAxisCarbon = Laminant([Layer(fabric=biax), Layer(fabric=biax)])
    orthoCarbon = Laminant([Layer(fabric=twill), Layer(fabric=twill)])
    uniCarbon = Laminant([Layer(fabric=uni)])
    laminantDict = {"steel": pureSteel, "aluminum": pureAluminum, "carbon": isoCarbon, 
                    "offAxis": offAxisCarbon, "orthoCarbon": orthoCarbon, "uni": uniCarbon}
    descriptions = {
        "steel": steel.description, "aluminum": aluminum.description, 
        "carbon": "Isotropic Carbon Composite", 
        "offAxis": "Orthogonal Carbon Laminant loaded 45 degrees off axis",
        "orthoCarbon": "Orthogonal Carbon Laminant loaded on axis",
        "uni": "Unidirectional Carbon Laminant"}

    def chooseMaterial():
        response = input("Choose a Laminant. (ls for a list of available Laminants)\n")
        if response == "ls":
            for laminant in descriptions:
                print(f"{laminant}: {descriptions[laminant]}")
            return chooseMaterial()
        if response in laminantDict:
            return laminantDict[response]
        print(f"{response} is not a known Material.")
        return chooseMaterial()
    
    while True:
        laminant = chooseMaterial()
        relativeStrength = laminant.strength / laminant.thickness # currently in units of kN/mm / inches
        relativeStrength /= 25.4 # now in units of GPa^2
        print(f"Strength: {relativeStrength :.2f} GPa (kN/mm^2)")
        print(f"Specific Strength: {relativeStrength / (laminant.density) :.2f} GPa/(g/cc)")




