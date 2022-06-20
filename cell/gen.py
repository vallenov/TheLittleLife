import random


class Gen:
    min_value = None
    max_value = None
    map = None
    sorted_map_keys = None

    def __init__(self):
        self.value = None

    def __repr__(self):
        return f'<{type(self).__name__} {self.value}>'


class Size(Gen):
    min_value = 10
    max_value = 100
    map = {
        1: 10,
        3: 8,
        10: 5,
        30: 3,
        40: 2,
        50: 1
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        rand = random.randint(0, 100)
        for k in Size.sorted_map_keys:
            if Size.map[k] <= rand:
                diff = Size.map[k]
                break
        else:
            print('0')
            diff = Size.map[-1]
        diff = random.choice([diff, -diff])
        if self.min_value <= self.value + diff <= self.max_value:
            return Size(self.value + diff)
        elif self.value + diff >= self.max_value:
            return Size(self.max_value)
        elif self.value + diff <= self.min_value:
            return Size(self.min_value)


class SightDistance(Gen):
    min_value = 200
    max_value = 400
    map = {
        1: 100,
        3: 80,
        10: 40,
        30: 30,
        40: 20,
        50: 10
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        diff = 0
        rand = random.randint(0, 100)
        if 0 < rand < 75:
            diff = 10
        elif 75 < rand < 90:
            diff = 20
        elif 90 < rand < 97:
            diff = 30
        elif 97 < rand <= 99:
            diff = 40
        elif rand == 100:
            diff = 50
        diff = random.choice([diff, -diff])
        if self.min_value <= self.value + diff <= self.max_value:
            return SightDistance(self.value + diff)
        elif self.value + diff >= self.max_value:
            return SightDistance(self.max_value)
        elif self.value + diff <= self.min_value:
            return SightDistance(self.min_value)
