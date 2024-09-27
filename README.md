

```markdown
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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
