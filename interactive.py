import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

class PutOption:
    def __init__(self, strike, premium) -> None:
        self.strike = float(strike)
        self.premium = float(premium)

    def breakeven(self):
        return self.strike - self.premium

    def maxloss(self):
        return self.premium

    def payoff(self, x):
        x = float(x)
        if x <= self.strike:
            return self.strike - x - self.premium
        return 0  # No payoff if the price is above the strike price

def calculate_put_option(strike, premium, x):
    put = PutOption(strike, premium)
    breakeven = put.breakeven()
    max_loss = put.maxloss()
    payoff = put.payoff(x)
    return breakeven, max_loss, payoff

def plot_payoff(strike, premium):
    put = PutOption(strike, premium)
    x = [0,10,20,30,40,50,60,70,80,90,100,110,120]
    x = int(x)
    y = [put.payoff(price) for price in x]

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Put Option Payoff', color='cyan')
    plt.axhline(0, color='black', lw=1)
    plt.axvline(strike, color='red', linestyle='--', label='Strike Price')
    plt.xlabel('Price of Underlying Asset')
    plt.ylabel('Payoff')
    plt.title('Put Option Payoff Diagram')
    plt.legend()
    plt.grid(True)
    plt.close()
    return plt.gcf()

css = """
body {
    background-color: #1a1a1a;
    color: #e0e0e0;
    font-family: 'Orbitron', sans-serif;
}

h1 {
    color: #00ffcc;
    text-align: center;
}

.gradio-container {
    border: 2px solid #00ffcc;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.5);
}

.gradio-input, .gradio-output {
    margin-bottom: 20px;
}

.gradio-input label, .gradio-output label {
    color: #00ffcc;
    font-weight: bold;
}

.gradio-slider {
    background-color: #333;
    border-radius: 10px;
    padding: 10px;
}

.gradio-slider input {
    background-color: #00ffcc;
}
"""

def update_interface(strike, premium, x):
    breakeven, max_loss, payoff = calculate_put_option(strike, premium, x)
    plot = plot_payoff(strike, premium)
    return breakeven, max_loss, payoff, plot

iface = gr.Interface(
    fn=update_interface,
    inputs=[
        gr.Slider(label="Strike Price", minimum=0, maximum=1000, step=1),
        gr.Slider(label="Premium", minimum=0, maximum=100, step=1),
        gr.Slider(label="Price of Underlying Asset", minimum=0, maximum=1000, step=1)
    ],
    outputs=[
        gr.Textbox(label="Breakeven Price"),
        gr.Textbox(label="Maximum Loss"),
        gr.Textbox(label="Payoff"),
        gr.Plot(label="Payoff Diagram")
    ],
    title="Put Option Calculator",
    description="Calculate the breakeven price, maximum loss, and payoff for a put option.",
    css=css
)

iface.launch()
