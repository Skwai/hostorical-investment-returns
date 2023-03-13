import csv
import matplotlib.pyplot as plt
import math
import seaborn as sns
import pandas as pd
import numpy as np


class Calculation:
    historical_data: list[tuple[int, float]] = []
    results = []

    def __init__(self, **kwargs):
        self.principal = kwargs.get("principal")
        self.duration = kwargs.get("duration")
        self.monthly_deposits = kwargs.get("monthly_deposits")

        self.load_historical_data()

    def load_historical_data(self) -> None:
        with open("./data/sp500.csv") as input:
            reader = csv.DictReader(input, delimiter=",")

            self.historical_data = []

            for row in reader:
                year = (int(row["year"]), float(row["total_return"]))
                self.historical_data.append(year)

    def __calculate_for_period(self, returns_for_period) -> float:
        balance = self.principal

        data = [balance]

        for year in range(self.duration):
            return_for_year = returns_for_period[year][1] / 100
            return_for_month = return_for_year / 12

            for _month in range(12):
                balance += self.monthly_deposits
                interest = balance * return_for_month
                balance += interest

            data.append(balance)

        return data

    def __get_historical_returns(self, start, end):
        return self.historical_data[start:end]

    def __sort_results(self):
        return self.results.sort(key=lambda item: item[1][-1])

    def get_percentile(self, percentile: int):
        count = len(self.results)
        index = min(max(0, math.floor(count * (percentile / 100))), count - 1)

        return self.results[index]

    def get_return_values(self):
        return list(map(lambda item: item[1], self.results))

    def calculate(self):
        end = len(self.historical_data) - self.duration

        self.results = []

        for i in range(end):
            returns = self.__get_historical_returns(i, i + self.duration)

            period_start_year = returns[0][0]
            period_end_year = returns[-1][0]

            data = self.__calculate_for_period(returns)

            self.results.append((f"{period_start_year}-{period_end_year}", data))

        self.__sort_results()

        return self.results

    def draw(self):
        count = len(self.results)

        worst = self.get_percentile(0)
        median = self.get_percentile(50)
        best = self.get_percentile(100)

        dict = {
            "year": list(range(0, self.duration + 1)),
            f"worst ({worst[0]})": worst[1],
            f"median ({median[0]})": median[1],
            f"best ({best[0]})": best[1],
        }

        # Chart all values
        # for [years, values] in self.results:
        #     dict[years] = values

        data = pd.DataFrame(dict)

        plt.ticklabel_format(style="plain", axis="y")

        sns.lineplot(
            x="year",
            y="value",
            # hue="variable",
            # estimator="median",
            # orient="x",
            data=pd.melt(data, ["year"]),
            markers=True,
        )

        plt.show()
