

import csv
import matplotlib.pyplot as plt
import numpy as np

winners = []
years = []

    
def result():
    year = []
    team = []
    with open('matches.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        
        for row in reader:
              years.append(row[1])
              winners.append(row[10])
              if row[4] not in team:
                  team.append(row[4])
              if row[1] not in year:
                  year.append(row[1])
    csvFile.close()

    enter(team, year)


#define logic function
def enter(team, year):
    
    year.sort()
    team_win = []
    #Logic to Find the team win per year
    for t in team:
        win_count = []
        for y in year:
             win_count.append(winners[years.index(y):years.index(y) + years.count(y)].count(t))
        team_win.append(win_count)

    #call the plotGraph function
    Graph(team_win, team, year)


def Graph(team_win, team, year):

    x = [0,1,2,3,4,5,6,7,8,9]
    barwidth = 1
    dataset1 = np.array(team_win[0])
    dataset2 = np.array(team_win[1])
    dataset3 = np.array(team_win[2])
    dataset4 = np.array(team_win[3])
    dataset5 = np.array(team_win[4])
    dataset6 = np.array(team_win[5])
    dataset7 = np.array(team_win[6])
    dataset8 = np.array(team_win[7])
    dataset9 = np.array(team_win[8])
    dataset10 = np.array(team_win[9])
    dataset11 = np.array(team_win[10])
    dataset12 = np.array(team_win[11])
    dataset13 = np.array(team_win[12])
    dataset14 = np.array(team_win[13])
    # plot the each team graph
    p1 = plt.bar(x, dataset1, color="#1abc9c", edgecolor='white', width=barwidth)
    p2 = plt.bar(x, dataset2, color="#2ecc71", bottom=dataset1, edgecolor='white', width=barwidth)
    p3 = plt.bar(x, dataset3, color="#3498db", bottom=dataset1+dataset2, edgecolor='white', width=barwidth)
    p4 = plt.bar(x, dataset4, color="#9b59b6", bottom=dataset1+dataset2+dataset3, edgecolor='white', width=barwidth)
    p5 = plt.bar(x, dataset5, color="#f1c40f", bottom=dataset1+dataset2+dataset3+dataset4, edgecolor='white', width=barwidth)
    p6 = plt.bar(x, dataset6, color="#e67e22", bottom=dataset1+dataset2+dataset3+dataset4+dataset5, edgecolor='white', width=barwidth)
    p7 = plt.bar(x, dataset7, color="#e74c3c", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6, edgecolor='white', width=barwidth)
    p8 = plt.bar(x, dataset8, color="#badc58", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7, edgecolor='white', width=barwidth)
    p9 = plt.bar(x, dataset9, color="#95a5a6", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7+dataset8, edgecolor='white', width=barwidth)
    p10 = plt.bar(x, dataset10, color="#d35400", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7+dataset8+dataset9, edgecolor='white', width=barwidth)
    p11 = plt.bar(x, dataset11, color="#e056fd", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7+dataset8+dataset9+dataset10, edgecolor='white', width=barwidth)
    p12 = plt.bar(x, dataset12, color="#ff7979", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7+dataset8+dataset9+dataset10+dataset11, edgecolor='white', width=barwidth)
    p13 = plt.bar(x, dataset13, color="#22a6b3", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7+dataset8+dataset9+dataset10+dataset11+dataset12, edgecolor='white', width=barwidth)
    p14 = plt.bar(x, dataset14, color="#130f40", bottom=dataset1+dataset2+dataset3+dataset4+dataset5+dataset6+dataset7+dataset8+dataset9+dataset10+dataset11+dataset12+dataset13, edgecolor='white', width=barwidth)
                  
    plt.xticks(x, year)
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0], p12[0], p13[0], p14[0]) ,team, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title("Winning Matches bar chart all Years in IPL", fontweight="bold")
    plt.xlabel("Years" , fontweight="bold")
    plt.ylabel("Won Matches per Team", fontweight='bold')
    plt.show()



result()
