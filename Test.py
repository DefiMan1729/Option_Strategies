class Call_Option:
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
        return 0   

# Example usage:
strike = input("Enter the strike price: ")
premium = input("Enter the call premium: ")
x = input("Enter the price of the underlying stock: ")
option = Call_Option(strike, premium)
print (f"The strike price is {option.strike}")
print(f"The breakeven is {option.breakeven()}")
print(f"The maximum loss is {option.maxloss()}")
print(f"The payoff at {x} is {option.payoff(x)}") 
