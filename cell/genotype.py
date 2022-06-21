import random
from typing import Optional
from cell.gen import (
    Size,
    SightDistance,
    Anger,
    Color,
)


class Genotype:

    def __init__(self):
        self.dna = {
            'size': Size(random.randint(10, 16)),
            'sight_distance': SightDistance(random.randint(200, 400)),
            'anger': Anger(random.randint(0, 100)),
            'color': Color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),
            'max_energy': random.randint(800, 1500),
            'birth_losses': random.randint(600, 800)
        }
        self.dna['energy_for_born'] = random.randint(self.dna['max_energy'] - 300, self.dna['max_energy'])

    def __repr__(self):
        return f'(\n{"".join([fr"   {gen}: {val}{chr(10)}" for gen, val in self.dna.items()])})'

    @classmethod
    def transfer_genotype(cls, genotype):
        if not isinstance(genotype, Genotype):
            raise TypeError
        new_genotype = Genotype()
        new_genotype.mutation(genotype)
        return new_genotype

    @staticmethod
    def rand_change(val: Optional[int], min_val: int = None, max_val: int = None):
        tmp = [i for i in range(-5, 0)] + [j for j in range(1, 6)]
        if isinstance(val, int):
            new_val = val + random.choice(tmp)
            if min_val is not None:
                new_val = min_val if new_val <= min_val else new_val
            if max_val is not None:
                new_val = max_val if new_val >= max_val else new_val
            return new_val
        elif isinstance(val, tuple):
            lst = list(val)
            rand = random.randint(0, len(val) - 1)
            lst[rand] += random.choice(tmp)
            if min_val is not None:
                lst[rand] = min_val if lst[rand] <= min_val else lst[rand]
            if max_val is not None:
                lst[rand] = max_val if lst[rand] >= max_val else lst[rand]
            return tuple(lst)

    def mutation(self, genotype):
        self.dna = genotype.dna.copy()
        self.dna['size'] = self.dna['size'].mutation()
        self.dna['sight_distance'] = self.dna['sight_distance'].mutation()
        self.dna['anger'] = self.dna['anger'].mutation()
        self.dna['color'] = self.dna['color'].mutation()
        self.dna['max_energy'] = self.rand_change(val=self.dna['max_energy'])
        self.dna['birth_losses'] = self.rand_change(val=self.dna['birth_losses'])
        self.dna['energy_for_born'] = self.rand_change(val=self.dna['energy_for_born'])
