class Solow:
    def __init__(self,
                 n=0.05,  # tasa de crecimiento de la población
                 s=0.25,  # tasa de ahorro
                 d=0.1,   # tasa de depreciación
                 a=0.3,   # proporción del trabajo
                 z=2.0,   # productividad
                 k=1.0):  # stock de capital actual
        self.n, self.s, self.d, self.a, self.z = n, s, d, a, z
        self.k = k

    def h(self):
        n, s, d, a, z = self.n, self.s, self.d, self.a, self.z
        return (s * z * self.k**a + (1 - d) * self.k) / (1 + n)

    def update(self):
        self.k = self.h()

    def steady_state(self):
        n, s, d, a, z = self.n, self.s, self.d, self.a, self.z
        return ((s*z) / (n + d))**(1 / (1 - a))

    def generate_sequence(self, t):
        sequence = []
        for i in range(t):
            sequence.append(self.k)
            self.update()
        return sequence
