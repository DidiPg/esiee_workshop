class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f"{self.name} is a {self.species}."


class Platypus(Animal):
    def __init__(self, name,
                 lays_eggs=True,
                 venomous=True,
                 webbed_feet=True):
        super().__init__(name, "platypus")
        self.lays_eggs = lays_eggs
        self.venomous = venomous
        self.webbed_feet = webbed_feet

    def describe(self):
        base = super().describe().rstrip('.')  
        traits = []
        if self.lays_eggs:
            traits.append("lays eggs")
        if self.venomous:
            traits.append("has a venomous spur")
        if self.webbed_feet:
            traits.append("has webbed feet")
        traits_str = ", ".join(traits)
        return f"{base} and {traits_str}."

p = Platypus("Perry")
print(p.describe())
