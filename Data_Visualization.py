import json

team_name = input("Enter the Team Name")
team_name = 'Teams/' + team_name
Losing_data_file = team_name + '/1/Losing/data.json'
Winning_data_file = team_name + '/Winning/data.json'
Tied_data_file = team_name + '/Tied/data.json'


with open(Losing_data_file, 'r') as json_file:
  data = json.load(open(Losing_data_file))
  for i in range(0, len(data)):
    yards_length = round(int(data[i]['Yards_Away_From_Scoring'])/10)
    print(yards_length)
  if(yards_length == 1):
    print('one')
  elif(yards_length == 2):
    print('Two')
  elif(yards_length == 3):
    print('Three')
  else:
    print('Greater than four')


