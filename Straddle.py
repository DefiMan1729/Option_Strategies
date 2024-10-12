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

class call_option:
    def __init__(self, strike, premium):
        self.strike = float(strike)
        self.premium = float(premium)

    def breakeven(self):
        return self.strike + self.premium
    def maxloss(self):
        return self.premium
    def payoff(self,x):
        x = float(x)
        if x >= self.strike:
            return x - self.strike - self.premium
        return -self.premium

strike = 100
put = put_option(strike,8)
call = call_option(strike,7)

total_premium=(put.premium+call.premium)
print (f"maximum profit from writing straddle at strike price {strike} is {total_premium}")