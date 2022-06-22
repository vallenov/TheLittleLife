import random
from cell.gen import (
    Size,
    SightDistance,
    Anger,
    Color,
    MaxEnergy,
    BirthLosses,
    EnergyForBorn,
)


class Genotype:

    def __init__(self):
        self.dna = {
            'size': Size(random.randint(10, 16)),
            'sight_distance': SightDistance(random.randint(200, 400)),
            'anger': Anger(random.randint(0, 100)),
            'color': Color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),
            'max_energy': MaxEnergy(random.randint(800, 1500)),
            'birth_losses': BirthLosses(random.randint(600, 800)),
            'energy_for_born': EnergyForBorn(random.randint(600, 800))
        }
        self.dna['energy_for_born'] = EnergyForBorn(
            random.randint(self.dna['max_energy'].value // 2, self.dna['max_energy'].value)
        )

    def __repr__(self):
        return f'(\n{"".join([fr"   {gen}: {val}{chr(10)}" for gen, val in self.dna.items()])})'

    @classmethod
    def transfer_genotype(cls, genotype):
        if not isinstance(genotype, Genotype):
            raise TypeError
        new_genotype = Genotype()
        new_genotype.mutation(genotype)
        return new_genotype

    def mutation(self, genotype):
        self.dna = genotype.dna.copy()
        self.dna['size'] = self.dna['size'].mutation()
        self.dna['sight_distance'] = self.dna['sight_distance'].mutation()
        self.dna['anger'] = self.dna['anger'].mutation()
        self.dna['color'] = self.dna['color'].mutation()
        self.dna['max_energy'] = self.dna['max_energy'].mutation()
        self.dna['birth_losses'] = self.dna['birth_losses'].mutation()
        self.dna['energy_for_born'] = self.dna['energy_for_born'].mutation()
