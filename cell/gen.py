import random


class Gen:
    def __init__(self):
        self.value = None
        self.min_value = None
        self.max_value = None


class Size(Gen):
    def __init__(self, value=None):
        super().__init__()
        self.min_value = 10
        self.value = self.min_value if not value else value
        self.max_value = 100

    def mutation(self):
        diff = 0
        rand = random.randint(0, 100)
        if 0 < rand < 50:
            diff = 1
        elif 50 < rand < 75:
            diff = 3
        elif 75 < rand < 90:
            diff = 5
        elif 90 < rand < 99:
            diff = 8
        elif rand == 100:
            diff = 10
        diff = random.choice([diff, -diff])
        if self.min_value <= self.value + diff <= self.max_value:
            return Size(self.value + diff)
