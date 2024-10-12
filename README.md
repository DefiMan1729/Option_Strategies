## Call Option Pricing
This repository contains a simple Python class for modeling call options, designed for CFA members who are interested in programming and financial modeling.

## Overview
The `Call_Option` class allows you to create call option objects with a specified strike price and premium. It includes methods to calculate the breakeven point and the payoff of the option.

## Class Definition
```python
class Call_Option:
    def __init__(self, strike, premium):
        self.strike = strike
        self.premium = premium

    def breakeven(self):
        return self.strike + self.premium

    def payoff(self, x):
        if x >= self.strike:
            if x > self.strike:
                return x - self.strike - self.premium
```

### Methods

- `breakeven()`: Returns the breakeven price of the call option.
- `payoff(x)`: Returns the payoff of the call option given the price of the underlying asset `x`.

## Example Usage

```python
# Create a call option with a strike price of 100 and a premium of 10
option = Call_Option(100, 10)

# Print the strike price
print(f"The strike price is {option.strike}")

# Calculate and print the breakeven price
print(f"The breakeven is {option.breakeven()}")

# Calculate and print the payoff at a given underlying price
x = 101  # price of the underlying asset
print(f"The payoff at {x} is {option.payoff(x)}")
```

## Getting Started

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/call-option-pricing.git
    cd call-option-pricing
    ```

2. **Run the example**:
    ```sh
    python example.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.