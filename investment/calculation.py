import csv


class Calculation:
    historical_returns: list[tuple[int, float]] = []

    def __init__(self, **kwargs):
        self.principal = kwargs.get("principal")
        self.duration = kwargs.get("duration")
        self.monthly_deposits = kwargs.get("monthly_deposits")

        self.load_historical_data()

    def load_historical_data(self) -> None:
        with open("./data/sp500.csv") as input:
            reader = csv.DictReader(input, delimiter=",")

            self.historical_returns = []

            for row in reader:
                year = (int(row["year"], 10), float(row["total_return"]))
                self.historical_returns.append(year)

    def __calculate_for_period(self, returns_for_period) -> float:
        balance = self.principal

        for year in range(self.duration):
            return_for_year = returns_for_period[year][1] / 100
            return_for_month = return_for_year / 12

            for _ in range(12):
                balance += self.monthly_deposits
                balance *= 1 + return_for_month

        return balance

    def __get_historical_returns(self, start, end):
        return self.historical_returns[start:end]

    def calculate(self):
        end = len(self.historical_returns) - self.duration

        balances = []

        for i in range(end):
            returns = self.__get_historical_returns(i, i + self.duration)

            period_start_year = returns[0][0]
            period_end_year = returns[-1][0]

            balance = self.__calculate_for_period(returns)
            balances.append((f"{period_start_year}-{period_end_year}", round(balance)))

        return balances
