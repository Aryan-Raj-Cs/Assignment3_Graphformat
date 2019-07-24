
import csv
import matplotlib.pyplot as plt


season = []
match_id = []
total_runs = []
bowling_team = []
overs = []


def result():
    teams = []
    with open('matches.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            season.append(row[1])
            if row[1]=='2017':
                if row[4] not in teams:
                    teams.append(row[4])
                    
    csvfile.close()
    
    ft_indx = season.index('2017')+1
    lt_indx = season.index('2017')+season.count('2017')
    #print(first_index)
    #print(last_index)
    
    with open('deliveries.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            match_id.append(row[0])
            bowling_team.append(row[3])
            overs.append(row[4])
            total_runs.append(row[17])
    csvfile.close() 
    calculateData(ft_indx, lt_indx, teams)
    

def calculateData(first_index, last_index, teams):
    last = match_id.index(str(last_index))+match_id.count(str(last_index))
    first = match_id.index(str(first_index))
    
    economy_list = []
    
    for t in teams:
        runs = 0
        ovr = 0
        for i in range(first, last):
            if 16<=int(overs[i])<=20:
                if bowling_team[i] == t:
                    runs += int(total_runs[i])
                    if overs[i] != overs[i+1]:
                       ovr += 1
        economy_list.append(runs/ovr)
    
    #print(economy_list) 

    Graph(teams, economy_list)
    

def Graph(teams, economy_list):
    plt.bar(teams, economy_list, color=['#e67e22', 'b', '#3498db', '#f1c40f', 'r', '#e74c3c', '#8e44ad', 'pink'])
    plt.xticks(rotation='90')
    plt.title("Economy rate in Overs 16-20 of IPL 2017", fontweight="bold")
    plt.xlabel("Teams", fontweight="bold")
    plt.ylabel("Economy", fontweight="bold")
    plt.show()
    

result()