# Interest Rate Swap to Convert Floating-Rate Securities into Fixed-Rate Securities

# Investment fund issued semi-annual floating rate bond (MRR+50bps)
# Face value of the bond
FV = 20000000

# Fixed swap rate (1.25% converted to decimal)
fixed_rate = 0.0125

# Market Reference Rate (MRR) at the first settlement date (0.75% converted to decimal)
MRR = 0.015

# Calculate the amount received from the floating rate
# Formula: FV * MRR * (1/2) for semi-annual period
receive = FV * MRR * (1/2)

# Calculate the amount paid for the fixed rate
# Formula: FV * fixed_rate * (1/2) for semi-annual period
pay = FV * fixed_rate * (1/2)

# Calculate the coupon payment for the floating rate bond
# Formula: FV * (MRR + 0.005) * (1/2) where 0.005 represents the additional 50 basis points
coupon_payment = FV * (MRR + 0.005) * (1/2)

# Print the calculated amounts
print(f"Receive: {receive}")
print(f"Pay: {pay}")
print(f"Coupon Payment: {coupon_payment}")


# FV = 100000000
# basispoints= .0003
# MRR = input("Enter MRR: ")
# MRR = float(MRR)
# coupon_payment = FV*(MRR+basispoints)*(1/2)

# # Expects interest to rise
# # Enters into pay fixed receive floating swap
# fixed_rate = .05

# payment_to_counterparty= FV*fixed_rate*(1/2)
# payment_from_counterparty = FV*MRR*(1/2)

# net_outflow = payment_to_counterparty+coupon_payment-payment_from_counterparty
# outflow = FV*(fixed_rate+basispoints)*(1/2)

# print(payment_to_counterparty,payment_from_counterparty,net_outflow, outflow )

# assert net_outflow == outflow

