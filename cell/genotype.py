import random


class Genotype:
    def __init__(self):
        # self.size = random.randint(10, 16)
        # self.sight_distance = random.randint(200, 300)
        # self.anger = random.randint(0, 100)
        # self.color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        # self.max_energy = random.randint(800, 1500)
        # self.born_energy = random.randint(self.max_energy - 100, self.max_energy + 300)
        # self.birth_losses = random.randint(600, 800)

        # self.dna = {
        #     'size': self.size,
        #     'sight_distance': self.sight_distance,
        #     'anger': self.anger,
        #     'color': self.color,
        #     'max_energy': self.max_energy,
        #     'born_energy': self.born_energy,
        #     'birth_losses': self.birth_losses
        # }

        self.dna = {
            'size': random.randint(10, 16),
            'sight_distance': random.randint(200, 300),
            'anger': random.randint(0, 100),
            'color': (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)),
            'max_energy': random.randint(800, 1500),
            'birth_losses': random.randint(600, 800)
        }
        self.dna['born_energy'] = random.randint(self.dna['max_energy'] - 100, self.dna['max_energy'] + 300)

    def __repr__(self):
        return str(self.dna)

    @classmethod
    def transfer_genotype(cls, genotype):
        if not isinstance(genotype, Genotype):
            raise TypeError
        new_genotype = Genotype()
        new_genotype.mutation(genotype)
        return new_genotype

    def mutation(self, genotype):
        new_dna = genotype.dna.copy()
        tmp = [i for i in range(-5, 0)]
        tmp.extend([j for j in range(1, 6)])
        for gen in new_dna.keys():
            if isinstance(new_dna[gen], int):
                new_dna[gen] += random.choice(tmp)
                new_dna[gen] = 0 if new_dna[gen] < 0 else new_dna[gen]
            elif isinstance(new_dna[gen], tuple):
                lst = list(new_dna[gen])
                rand = random.randint(0, len(new_dna[gen]) - 1)
                lst[rand] += random.choice(tmp)
                lst[rand] = 0 if lst[rand] < 0 else lst[rand]
                lst[rand] = 255 if lst[rand] > 255 else lst[rand]
                new_dna[gen] = tuple(lst)
        self.dna = new_dna
