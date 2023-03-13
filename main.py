from investment.calculation import Calculation

simuluation = Calculation(principal=150_000, duration=10, monthly_deposits=2_000)

print(simuluation.calculate())
