import csv
import matplotlib.pyplot as plt

years = []


# read the csv file
def readcsvFile():
    year = []
    matches = []
    nex = 0
    pre = 0
    last_year = ''
    with open('matches.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)

        for row in reader:
            years.append(row[1])
            pre = nex
            if row[1] not in year:
                year.append(row[1])
                nex = years.index(row[1])
                matches.append(nex - pre)
                last_year = row[1]

    csvFile.close()
    enter(last_year, matches, year)


def enter(last_year, matches, year):
    matches.append(years.count(last_year))
    matches = matches[1:]
    start, *rest = matches
    matches = *rest, start

    year.sort()
    Graph(year, matches)


def Graph(year, matches):
    # Plot Bar Graph
    plt.bar(year, matches, color='b')
    plt.xlabel("Years")
    plt.ylabel("Matches Played")
    plt.show()


readcsvFile()