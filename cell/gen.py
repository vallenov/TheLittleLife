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

    def new_value(self, val=None):
        rand = random.randint(0, 100)
        diff = 0
        for k in self.sorted_map_keys:
            diff = self.map[k]
            if k > rand:
                diff = self.map[k]
                break
        diff = random.choice([diff, -diff])
        new_val = None
        val = self.value if val is None else val
        if self.min_value <= val + diff <= self.max_value:
            new_val = val + diff
        elif val + diff >= self.max_value:
            new_val = self.max_value
        elif val + diff <= self.min_value:
            new_val = self.min_value
        return new_val


class Size(Gen):
    min_value = 10
    max_value = 100
    map = {
        10: 10,
        20: 8,
        30: 5,
        40: 3,
        60: 2,
        90: 1
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        return Size(super().new_value())


class Speed(Gen):
    min_value = 10
    max_value = 40
    map = {
        10: 6,
        20: 5,
        30: 4,
        40: 3,
        60: 2,
        90: 1
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        return Speed(super().new_value())


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
        return SightDistance(super().new_value())


class Anger(Gen):
    min_value = 0
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
        return Anger(super().new_value())


class Color(Gen):
    min_value = 0
    max_value = 255
    map = {
        1: 50,
        3: 40,
        10: 30,
        30: 20,
        40: 10,
        50: 5
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        new_color = []
        for col_index in range(len(self.value)):
            new_color.append(super().new_value(val=self.value[col_index]))
        return Color(tuple(new_color))


class MaxEnergy(Gen):
    min_value = 800
    max_value = 2000
    map = {
        1: 70,
        3: 60,
        10: 50,
        30: 40,
        40: 30,
        50: 10
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        return MaxEnergy(super().new_value())


class BirthLosses(Gen):
    min_value = 600
    max_value = MaxEnergy.min_value
    map = {
        1: 70,
        3: 60,
        10: 30,
        30: 15,
        40: 10,
        50: 5
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        return BirthLosses(super().new_value())


class EnergyForBorn(Gen):
    min_value = 700
    max_value = 1500
    map = {
        1: 70,
        3: 60,
        10: 30,
        30: 15,
        40: 10,
        50: 5
    }
    sorted_map_keys = sorted(map.keys())

    def __init__(self, value=None):
        super().__init__()
        self.value = self.min_value if not value else value

    def mutation(self):
        return EnergyForBorn(super().new_value())
