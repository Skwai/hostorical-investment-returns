from investment.calculation import Calculation

simuluation = Calculation(principal=150_000, duration=10, monthly_deposits=2_000)

simuluation.calculate()

print("0%tile", simuluation.get_percentile(0))
print("10%tile", simuluation.get_percentile(10))
print("50%tile", simuluation.get_percentile(50))
print("90%tile", simuluation.get_percentile(90))
print("100%tile", simuluation.get_percentile(100))
