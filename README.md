
# Covered Call Option Calculator

This Python script provides a simple calculator for covered call options. It allows users to input the strike price, call premium, initial stock price, and current stock price to calculate the maximum gain, breakeven point, maximum loss, and effective sell price.

## Features

- Calculate the breakeven point for a covered call option.
- Calculate the maximum gain and maximum loss.
- Determine the effective sell price based on the current stock price.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/covered-call-option-calculator.git
    cd covered-call-option-calculator
    ```

2. Run the script:
    ```bash
    python covered_call_option.py
    ```

3. Follow the prompts to enter the strike price, call premium, initial stock price, and current stock price.

## Example

```plaintext
Enter strike price: 100
Enter call premium: 5
Enter initial stock price: 95
Enter current stock price: 105
Maximum gain is 10.0
Breakeven point is 90.0
Maximum loss is 90.0
Effective sell price is 105.0
```

## Code Overview

The script defines a `CoveredCallOption` class with methods to calculate the breakeven point, maximum gain, maximum loss, and effective sell price.

```python
class CoveredCallOption:
    def __init__(self, strike, premium, stock_price) -> None:
        self.strike = strike
        self.premium = premium
        self.stock_price = stock_price

    def break_even(self) -> float:
        return self.stock_price - self.premium

    def max_gain(self) -> float:
        return self.strike - self.stock_price + self.premium

    def max_loss(self) -> float:
        return self.stock_price - self.premium

    def effective_sell_price(self, current_stock_price: float) -> float:
        if current_stock_price >= self.strike:
            return self.strike + self.premium
        else:
            return current_stock_price + self.premium
```

## Notes

- A covered call strategy is appropriate if the expected volatility is lower than the implied volatility.


# Bear Spread Strategy with Put Options

## Overview

This project demonstrates the implementation of a Bear Spread strategy using put options. A Bear Spread is an options strategy used when an investor expects a decline in the price of the underlying asset. This strategy involves buying a put option with a higher exercise price and selling a put option with a lower exercise price.

## Key Concepts

- **Put Bear Spread**: Involves buying a put option with a higher exercise price and selling a put option with a lower exercise price. This results in an initial cash outflow (debit spread) because the higher exercise price put is more expensive.
- **Call Bear Spread**: Involves buying a call option with a higher exercise price and selling a call option with a lower exercise price. This results in an initial cash inflow (credit spread) because the higher exercise price call is less expensive.

## Code Explanation

The code provided calculates the maximum loss, maximum profit, and breakeven point for a Bear Spread strategy using put options.

### Class Definition

```python
class PutOption:
    def __init__(self, strike, premium):
        """
        Initialize a PutOption instance.

        :param strike: The strike price of the put option.
        :param premium: The premium paid for the put option.
        """
        self.strike = strike
        self.premium = premium
```

The `PutOption` class is used to create instances of put options with specified strike prices and premiums.

### User Input

```python
put_h_strike = float(input("Enter higher strike price of the Put: "))
put_h_premium = float(input("Enter the premium of the higher strike priced Put: "))
put_l_strike = float(input("Enter lower strike price of the Put: "))
put_l_premium = float(input("Enter the premium of the lower strike priced Put: "))
```

The user is prompted to enter the strike prices and premiums for the higher and lower strike price put options.

### Instance Creation

```python
put_h = PutOption(put_h_strike, put_h_premium)  # Higher strike price put option
put_l = PutOption(put_l_strike, put_l_premium)  # Lower strike price put option
```

Instances of `PutOption` are created for the higher and lower strike price put options.

### Calculations

```python
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
```

- **Total Cash Outflow**: Calculated as the difference between the premiums of the higher and lower strike price put options.
- **Maximum Loss**: Equal to the total cash outflow.
- **Maximum Profit**: Calculated as the difference between the strike prices minus the total cash outflow.
- **Breakeven Point**: Calculated as the higher strike price minus the total cash outflow.

## Usage

1. Run the script.
2. Enter the strike prices and premiums for the higher and lower strike price put options when prompted.
3. The script will output the maximum loss, maximum profit, and breakeven point for the Bear Spread strategy.

## Example

```
Enter higher strike price of the Put: 16
Enter the premium of the higher strike priced Put: 1.96
Enter lower strike price of the Put: 15
Enter the premium of the lower strike priced Put: 1.46
Maximum loss (total cash outflow) = 0.5
Maximum profit = 0.5
Breakeven point = 15.5
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
