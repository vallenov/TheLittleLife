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

    def mutation(self):
        rand = random.randint(0, 100)
        diff = 0
        for k in self.sorted_map_keys:
            diff = self.map[k]
            if k > rand:
                diff = self.map[k]
                break
        diff = random.choice([diff, -diff])
        new_value = None
        if self.min_value <= self.value + diff <= self.max_value:
            new_value = self.value + diff
        elif self.value + diff >= self.max_value:
            new_value = self.max_value
        elif self.value + diff <= self.min_value:
            new_value = self.min_value
        return new_value


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
        return Size(super().mutation())


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
        return SightDistance(super().mutation())


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
        return Anger(super().mutation())


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
        rand_grb = random.randint(0, 2)
        new_color = []
        for col_index in range(len(self.value)):
            if col_index == rand_grb:
                tmp = self.value
                self.value = self.value[rand_grb]
                new_color.append(super().mutation())
                self.value = tmp
                continue
            new_color.append(self.value[col_index])
        return Color(tuple(new_color))
