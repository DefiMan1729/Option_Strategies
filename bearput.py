# Bear Spread Strategy with Put Options
# Buy a put option with a higher exercise price and sell a put option with a lower exercise price.
# Higher exercise prices are more expensive | A put bear spread will result in an initial cash outflow (debit spread).
# For a call bear spread, the investor buys a higher exercise price call and sells the lower exercise price call.
# Higher exercise price call is less expensive than the lower strike being sold | A call bear spread will result in an initial cash inflow (credit spread).

class PutOption:
    def __init__(self, strike, premium):
        """
        Initialize a PutOption instance.

        :param strike: The strike price of the put option.
        :param premium: The premium paid for the put option.
        """
        self.strike = strike
        self.premium = premium
        
put_h_strike = float (input("Enter higher strike price of the Put: "))
put_h_premium = float (input("Enter the premium of the higher strike priced Put: "))
put_l_strike = float (input("Enter lower strike price of the Put: "))
put_l_premium = float (input("Enter the premium of the lower strike priced Put: "))
# Create instances of PutOption for higher and lower strike prices
put_h = PutOption(put_h_strike, put_h_premium)  # Higher strike price put option
put_l = PutOption(put_l_strike, put_l_premium)  # Lower strike price put option

# Calculate the total cash outflow for the put bear spread
total_cash_outflow = put_h.premium - put_l.premium

# Print the maximum loss, which is the total cash outflow
print(f"Maximum loss (total cash outflow) = {total_cash_outflow}")

# Calculate the maximum profit for the put bear spread
max_profit = put_h.strike - put_l.strike - total_cash_outflow

# Print the maximum profit
print(f"Maximum profit = {max_profit}")

# Calculate the breakeven point for the put bear spread
break_even = put_h.strike - total_cash_outflow

# Print the breakeven point
print(f"Breakeven point = {break_even}")

