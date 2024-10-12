class CallOption:
    def __init__(self, strike, premium):
        """
        Initialize a Call Option instance.

        :param strike: The strike price of the call option.
        :param premium: The premium paid for the call option.
        """
        self.strike = strike
        self.premium = premium

# Get user inputs for strike prices and premiums
strike_l = float(input("Enter the lower strike price: "))
strike_h = float(input("Enter the higher strike price: "))
premium_l = float(input("Enter the premium for the lower strike priced call: "))
premium_h = float(input("Enter the premium for the higher strike priced call: "))

# Create Call Option instances for the lower and higher strike prices
call_l = CallOption(strike_l, premium_l)
call_h = CallOption(strike_h, premium_h)

# Calculate the maximum profit
max_profit = call_h.strike - call_l.strike - (call_l.premium - call_h.premium)
print(f"Maximum profit from this strategy is {max_profit}")

# Calculate the maximum loss
max_loss = call_l.premium - call_h.premium
print(f"Maximum loss from this strategy is {max_loss}")

# Calculate the breakeven point
break_even = call_l.strike + (call_l.premium - call_h.premium)
print(f"Breakeven point for this strategy is {break_even}")

# hypothetical_prices = []
# int i = call_l.strike_l - 10; call_h.strike_h+10:
# hypothetical_prices = append(hypothetical_prices)
