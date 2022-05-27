import random
from typing import Optional


class Genotype:
    def __init__(self):
        self.dna = {
            'size': random.randint(10, 16),
            'sight_distance': random.randint(200, 300),
            'anger': random.randint(0, 100),
            'color': (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)),
            'max_energy': random.randint(800, 1500),
            'birth_losses': random.randint(600, 800)
        }
        self.dna['energy_for_born'] = random.randint(self.dna['max_energy'] - 300, self.dna['max_energy'])

    def __repr__(self):
        return str(self.dna)

    @classmethod
    def transfer_genotype(cls, genotype):
        if not isinstance(genotype, Genotype):
            raise TypeError
        new_genotype = Genotype()
        new_genotype.mutation(genotype)
        return new_genotype

    # def mutation(self, genotype):
    #     new_dna = genotype.dna.copy()
    #     tmp = [i for i in range(-5, 0)]
    #     tmp.extend([j for j in range(1, 6)])
    #     for gen in new_dna.keys():
    #         if isinstance(new_dna[gen], int):
    #             new_dna[gen] += random.choice(tmp)
    #             new_dna[gen] = 0 if new_dna[gen] < 0 else new_dna[gen]
    #         elif isinstance(new_dna[gen], tuple):
    #             lst = list(new_dna[gen])
    #             rand = random.randint(0, len(new_dna[gen]) - 1)
    #             lst[rand] += random.choice(tmp)
    #             lst[rand] = 0 if lst[rand] < 0 else lst[rand]
    #             lst[rand] = 255 if lst[rand] > 255 else lst[rand]
    #             new_dna[gen] = tuple(lst)
    #     self.dna = new_dna

    @staticmethod
    def rand_change(val: Optional[int], min_val: int = None, max_val: int = None):
        tmp = [i for i in range(-5, 0)]
        tmp.extend([j for j in range(1, 6)])
        if isinstance(val, int):
            new_val = val + random.choice(tmp)
            if min_val:
                new_val = min_val if new_val < min_val else new_val
            if max_val:
                new_val = max_val if new_val > max_val else new_val
            return new_val
        elif isinstance(val, tuple):
            lst = list(val)
            rand = random.randint(0, len(val) - 1)
            lst[rand] += random.choice(tmp)
            if min_val:
                lst[rand] = min_val if lst[rand] < min_val else lst[rand]
            if max_val:
                lst[rand] = max_val if lst[rand] > max_val else lst[rand]
            return tuple(lst)

    def mutation(self, genotype):
        new_dna = genotype.dna.copy()
        tmp = [i for i in range(-5, 0)]
        tmp.extend([j for j in range(1, 6)])
        new_dna['size'] = self.rand_change(val=new_dna['size'], min_val=10)
        new_dna['sight_distance'] = self.rand_change(val=new_dna['sight_distance'])
        new_dna['anger'] = self.rand_change(val=new_dna['anger'])
        new_dna['color'] = self.rand_change(val=new_dna['color'], max_val=255)
        new_dna['max_energy'] = self.rand_change(val=new_dna['max_energy'])
        new_dna['birth_losses'] = self.rand_change(val=new_dna['birth_losses'])
        new_dna['energy_for_born'] = self.rand_change(val=new_dna['energy_for_born'])
        self.dna = new_dna
