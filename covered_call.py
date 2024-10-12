class CoveredCallOption:
    def __init__(self, strike: float, premium: float, stock_price: float) -> None:
        """
        Initialize the CoveredCallOption with strike price, premium, and stock price.

        :param strike: Strike price of the call option
        :param premium: Premium received for selling the call option
        :param stock_price: Initial stock price
        """
        self.strike = strike
        self.premium = premium
        self.stock_price = stock_price

    def break_even(self) -> float:
        """
        Calculate the breakeven point for the covered call option.

        :return: Breakeven stock price
        """
        return self.stock_price - self.premium

    def max_gain(self) -> float:
        """
        Calculate the maximum gain for the covered call option.

        :return: Maximum gain
        """
        return self.strike - self.stock_price + self.premium

    def max_loss(self) -> float:
        """
        Calculate the maximum loss for the covered call option.

        :return: Maximum loss
        """
        return self.stock_price - self.premium

    def effective_sell_price(self, current_stock_price: float) -> float:
        """
        Calculate the effective sell price for the underlying stock.

        :param current_stock_price: Current stock price
        :return: Effective sell price
        """
        if current_stock_price >= self.strike:
            return self.strike + self.premium
        else:
            return current_stock_price + self.premium

# Input section for user to provide option parameters
strike = float(input("Enter strike price: "))
premium = float(input("Enter call premium: "))
initial_stock_price = float(input("Enter initial stock price: "))
current_stock_price = float(input("Enter current stock price: "))

# Create an instance of CoveredCallOption
covered_call = CoveredCallOption(strike, premium, initial_stock_price)

# Output the calculated values
print(f"Maximum gain is {covered_call.max_gain()}")
print(f"Breakeven point is {covered_call.break_even()}")
print(f"Maximum loss is {covered_call.max_loss()}")
print(f"Effective sell price is {covered_call.effective_sell_price(current_stock_price)}")

# Note: A covered call strategy is appropriate if the expected volatility is lower than the implied volatility.
