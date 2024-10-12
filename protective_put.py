class ProtectivePutOption:
    def __init__(self, strike: float, premium: float, stock_price: float) -> None:
        """
        Initialize the ProtectivePutOption with strike price, premium, and stock price.

        :param strike: Strike price of the put option
        :param premium: Premium paid for buying the put option
        :param stock_price: Initial stock price
        """
        self.strike = strike
        self.premium = premium
        self.stock_price = stock_price

    def max_gain(self) -> str:
        """
        Calculate the maximum gain for the protective put option.
        
        :return: Maximum gain (infinite)
        """
        return "infinite"

    def max_loss(self) -> float:
        """
        Calculate the maximum loss for the protective put option.
        
        :return: Maximum loss
        """
        return self.stock_price - self.strike + self.premium

    def breakeven(self) -> float:
        """
        Calculate the breakeven point for the protective put option.
        
        :return: Breakeven stock price
        """
        return self.stock_price + self.premium

    def effective_gain(self, current_stock_price: float) -> float:
        """
        Calculate the effective gain based on the current stock price.
        
        :param current_stock_price: Current stock price
        :return: Effective gain
        """
        if current_stock_price >= self.strike:
            return current_stock_price - self.stock_price - self.premium
        else:
            return self.strike - self.stock_price - self.premium

# Create an instance of ProtectivePutOption with example values
protective_put = ProtectivePutOption(20, 1.15, 25)

# Output the calculated values
print(f"Maximum gain: {protective_put.max_gain()}")
print(f"Maximum loss: {protective_put.max_loss()}")
print(f"Breakeven point: {protective_put.breakeven()}")
print(f"Effective gain: {protective_put.effective_gain(31.33)}")
