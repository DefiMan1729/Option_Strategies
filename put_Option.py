import matplotlib.pyplot as plt
class put_option:
    def __init__(self,strike,premium) -> None:
        self.strike = strike
        self.premium = premium
    def breakeven(self):
        return self.strike-self.premium
    def maxloss(self):
        return self.premium
    def payoff(self,x):
        x = float(x)
        if x <= self.strike:
            return self.strike-x-self.premium
        return -self.premium

put = put_option(100,10)
x=800
print (f"breakeven price of the put option is {put.breakeven()}")
print (f"max loss from the put option strategy is {put.maxloss()}")
print (f"payoff at {x} is {put.payoff(x)}")

payoff = []
prices = [10, 50, 100,120, 160, 200, 300, 900]
for x in prices:
    payoff.append(put.payoff(x))
print (payoff)
plt.plot(payoff)
plt.show()
# plt.close()