import csv

with open("./data/sp500.csv") as input:
    reader = csv.reader(input, delimiter=",")

    reversed = []

    for row in reader:
        reversed.append(row)

    reversed.reverse()

    with open("./data/sp500-reversed.csv", "w") as output:
        writer = csv.writer(output, delimiter=",")

        for row in reversed:
            writer.writerow(row)
