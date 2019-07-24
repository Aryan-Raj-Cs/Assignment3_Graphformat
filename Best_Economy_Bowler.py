import matplotlib.pyplot as plt
import csv

years = []

def readcsvFile():
    with open('matches.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            years.append(row[1])
    csvFile.close()

    ft_indx = years.index('2015') + 1
    lt_indx = years.index('2015') + years.count('2015')
    
    run = {}
    over = {}
    with open('deliveries.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            if int(row[0])>=ft_indx and int(row[0])<=lt_indx:
                if row[8] not in run.keys():
                    run[row[8]] = int(row[17])
                    over[row[8]] = 1
                else:
                    run[row[8]] = (run[row[8]]+int(row[17]))
                    over[row[8]] = (over[row[8]]+1)
                    
            elif int(row[0])>lt_indx:
                break
            
        over_dict = {k:v//6 for k, v in over.items()}
    csvFile.close()
    # Economy of each bowler of 2015
    economy_dict = {k: run[k]/over_dict[k] for k in run.keys() & over_dict}
    # calculate the top 10 economical bowlers
    data = dict(sorted(economy_dict.items(), key=lambda x: x[1], reverse=True)[:10])
    graph(data)

#plot the graph
def graph(data):
    plt.bar(data.keys(), data.values(), color='c')
    plt.title("Top 10 Economical Bowler of Year 2015 IPL", fontweight="bold")
    plt.xticks(rotation='90')
    plt.xlabel("Name Of Bowlers", fontweight='bold')
    plt.ylabel("Economic", fontweight="bold")
    plt.show()


readcsvFile()
