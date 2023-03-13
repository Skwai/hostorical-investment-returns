from investment.calculation import Calculation

simuluation = Calculation(principal=150_000, duration=20, monthly_deposits=2_000)

simuluation.calculate()

simuluation.draw()
