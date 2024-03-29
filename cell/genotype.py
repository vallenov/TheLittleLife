import random
from cell.gen import (
    Size,
    Speed,
    SightDistance,
    Anger,
    Color,
    MaxEnergy,
    BirthLosses,
    EnergyForBorn,
    RunChance,
    StartEnergy,
)


class Genotype:

    def __init__(self, parent_genotype=None):
        if parent_genotype:
            return
        self.dna = {
            'size': Size(random.randint(10, 16)),
            'speed': Speed(random.randint(8, 10)),
            'sight_distance': SightDistance(random.randint(200, 400)),
            'anger': Anger(random.randint(0, 100)),
            'color': Color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),
            'max_energy': MaxEnergy(random.randint(800, 1500)),
            'birth_losses': BirthLosses(random.randint(600, 800)),
            'energy_for_born': EnergyForBorn(random.randint(600, 800)),
            'run_chance': RunChance(random.randint(0, 30)),
            'start_energy': StartEnergy(random.randint(400, 700))
        }
        self.dna['energy_for_born'] = EnergyForBorn(
            random.randint(self.dna['max_energy'].value // 2, self.dna['max_energy'].value)
        )
        self.dna['speed'].value = self.dna['size'].value \
            if self.dna['speed'].value > self.dna['size'].value \
            else self.dna['speed'].value

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
        for name, gen in self.dna.items():
            self.dna[name] = gen.mutation()
        self.dna['speed'].value = self.dna['size'].value \
            if self.dna['speed'].value > self.dna['size'].value \
            else self.dna['speed'].value
