class Chaos:
    def __init__(self, x0, r):
        self.x, self.r = x0, r

    def update(self):
        self.x = self.r * self.x*(1-self.x)

    def generate_sequence(self, n):
        path = []
        for i in range(n):
            path.append(self.x)
            self.update()
        return path
