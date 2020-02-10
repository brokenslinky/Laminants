class Material:
    """A Material which can be used to weave Fabrics or build Laminants"""
    name: str
    # The name of this Material
    description: str
    # A description of this Material
    modulus: float
    # Elatic modulus of the Material (GPa)
    strength: float
    # Ultimate strength of the Material (MPa)
    density: float
    # Density of the Material (g/cc)
    yieldStrength: float
    # Yield strength of the Material (MPa)
    shearModulus: float
    # Shear modulus of the Material (GPa)
    poissonsRatio: float
    # Poisson's Ratio for the Material 

    def __init__(self, modulus=None, strength=None, density=None, yieldStrength=None, shearModulus=None, poissonsRatio=None, name="", description=""):
        self.modulus = modulus
        self.strength = strength
        self.density = density
        self.yieldStrength = yieldStrength
        self.shearModulus = shearModulus
        self.poissonsRatio = poissonsRatio
        self.name = name
        self.description = description

    @property
    def elongation(self):
        """The elongation this Material can experience before yielding or breaking"""
        if self.modulus == 0.:
            return 999999999.
        stress = self.strength
        if self.yieldStrength != None:
            if self.yieldStrength < self.strength:
                stress = self.yieldStrength
        return stress / (1000. * self.modulus)

steel_4340 = Material(
    name = "4340",
    description = "Steel 4340",
    modulus = 205.,
    strength = 1110.,
    density = 7.85,
    yieldStrength = 710.,
    shearModulus = 80.,
    poissonsRatio = 0.29)

aluminum_6061 = Material(
    name = "6061",
    description = "Aluminum 6061-T6",
    modulus = 68.9,
    strength = 310.,
    density = 2.7,
    yieldStrength = 276.)

carbon_T700 = Material(
    name = "T700",
    description = "Toray T700 Carbon Fiber",
    modulus = 230.,
    strength = 4900.,
    density = 1.8)

carbon_AS4 = Material(
    name = "AS4",
    description = "AS4 Carbon Fiber",
    density = 1.79,
    strength = 4413.,
    modulus = 231.)

epoxy = Material(
    name = "Epoxy",
    description= "Typical Composite Epoxy",
    density = 1.25,
    strength = 69.,
    modulus = 3.5)

space = Material(
    name = "Nothing",
    description = "Empty Space",
    density = 0.,
    strength = 0.,
    modulus = 0.
    )

# Set default aliases
carbon = carbon_AS4
aluminum = aluminum_6061
steel = steel_4340