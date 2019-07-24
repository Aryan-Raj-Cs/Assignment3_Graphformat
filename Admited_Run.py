import matplotlib.pyplot as plt
import csv

years = []


def result():
    with open('matches.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            years.append(row[1])
    csvFile.close()
    ft_indx = years.index('2016') + 1
    lt_indx = years.index('2016') + years.count('2016')

    extra = {}
    with open('deliveries.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            if int(row[0]) >= ft_indx and int(row[0]) <= lt_indx:
                if row[3] not in extra.keys():
                    extra[row[3]] = int(row[16])
                else:
                    extra[row[3]] = (extra[row[3]] + int(row[16]))
            elif int(row[0]) > lt_indx:
                break
    csvFile.close()
    Graph(extra)


def Graph(extra):
    plt.title("Extra Runs admit per Teams in Year 2016 IPL", fontweight="bold")
    plt.rcParams.update({'font.size': 10})
    plt.bar(extra.keys(), extra.values(), color='b')
    plt.xticks(rotation='90')
    plt.xlabel("Tnames", fontweight='bold')
    plt.ylabel("Extra Runs", fontweight='bold')
    plt.show()
result()
