import csv

teams_list = []
with open('teams.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        teams_list.append(FootBallTeam(row[0], row[1], row[2], row[3]))

# Example usage
for team in teams_list:
    print(team)