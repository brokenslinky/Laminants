
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

    def bulk_properties(self):
        relativeStrength = self.strength / self.thickness # currently in units of kN/mm / inches
        relativeStrength /= 25.4 # now in units of GPa^2
        print(f"Strength: {relativeStrength :.2f} GPa (kN/mm^2)")
        print(f"Specific Strength: {relativeStrength / (laminant.density) :.2f} GPa/(g/cc)")

    def energy_stored(self, neutral_axis):
        height = 0.
        energy = 0.
        for layer in self.layers:
            if (height - neutral_axis) * (height + layer.thickness - neutral_axis) >= 0.:
                energy += abs((height - neutral_axis)**2 - (height + layer.thickness - neutral_axis)**2) * layer.modulus
            else:
                energy += ((height - neutral_axis)**2 + (height + layer.thickness - neutral_axis)**2) * layer.modulus
            height += layer.thickness
        return energy

    def neutral_axis(self, divisions = 1000):
        neutral_axis = 0.
        from sys import float_info
        minergy = float_info.max
        for i in range(0, divisions):
            position = i * self.thickness / divisions
            energy = self.energy_stored(position)
            if energy < minergy:
                minergy = energy
                neutral_axis = position
                #print(energy)
        return neutral_axis

    def bend_to_failure(self):
        elongation_per_inch_from_neutral = 0.
        neutral_axis = self.neutral_axis()
        broken = False
        while not broken:
            height = 0.
            for layer in self.layers:
                if max(abs(height - neutral_axis), abs(height + layer.thickness - 
                       neutral_axis)) * elongation_per_inch_from_neutral > layer.elongation:
                    broken = True
                height += layer.thickness
            if not broken:
                elongation_per_inch_from_neutral += 0.0001

        stress = []
        relative_stress = []
        height = []
        h = 0.
        for layer in self.layers:
            stress.append(elongation_per_inch_from_neutral * layer.modulus * (h - neutral_axis))
            #relative_stress.append(stress[-1] * 1000. / layer.strength)
            relative_stress.append(elongation_per_inch_from_neutral * (h - neutral_axis) / layer.elongation)
            height.append(h)
            h += layer.thickness
            stress.append(elongation_per_inch_from_neutral * layer.modulus * (h - neutral_axis))
            #relative_stress.append(stress[-1] * 1000. / layer.strength)
            relative_stress.append(elongation_per_inch_from_neutral * (h - neutral_axis) / layer.elongation)
            height.append(h)

        top_to_bottom = ""
        last_fabric = None
        counter = 0
        for layer in reversed(self.layers):
            if layer.fabric.description == last_fabric:
                counter += 1
            else:
                if last_fabric != None:
                    top_to_bottom+= f"{counter}x {last_fabric}\n"
                last_fabric = layer.fabric.description
                counter = 1
        top_to_bottom += f"{counter}x {last_fabric}"

        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(relative_stress, height)
        plt.xlim(-1., 1.)
        plt.ylim(0., self.thickness)
        ax.set_xlabel("Normalized Stress (Unitless)")
        ax.set_ylabel("Height Within Laminant (inches)")
        ax.legend([top_to_bottom])
        plt.show()


