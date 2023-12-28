import market

params = 15, .5, -2, .5, 3
m = market.Market(*params)
print("equilibrium price = ", m.price())
