class Consumer:
    def __init__(self, w):
        self.wealth = w

    def earn(self, w):
        self.wealth += w

    def spend(self, w):
        if self.wealth < w:
            print("Insufficent funds")
        else:
            self.wealth -= w


c1 = Consumer(100)
c2 = Consumer(120)
c2.spend(130)
print('testing')
