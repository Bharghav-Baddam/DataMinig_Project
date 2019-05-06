import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import seaborn as sns


team_name = input("Enter the Team Name")
quarter_number = int(input("Enter the Quarter Number ranging from 1 to 5"))
situation = str(input("Enter 1 for Losing, 2 for Tied, 3 for Winning"))




if(quarter_number<1 or quarter_number>5):
  sys.exit("Wrong Data Entered")


if(situation == '1'):
  file_open = "Losing"
elif(situation == '2'):
  file_open = "Tied"
elif(situation == '3'):
  file_open = "Winning"
else:
  sys.exit('Wrong Data Entered')

quarter_number = str(quarter_number)
file_name = 'Teams/{}/{}/{}/data.json'.format(team_name, quarter_number, file_open)
print(file_name)
no_of_yards_data = (np.zeros(11, dtype=int))
pass_list = (np.zeros(11, dtype=int))
run_list = (np.zeros(11, dtype=int))

#------------Losing Data Visualization###################################################


with open(file_name, 'r') as json_file:
  data = json.load(open(file_name))
  for i in range(0, len(data)):
    yards_length = round(int(data[i]['Yards_Away_From_Scoring'])/10)


    if(yards_length == 0):
      no_of_yards_data[0] = no_of_yards_data[0] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[0] = pass_list[0] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[0] = run_list[0] + 1

    elif(yards_length == 1):
      no_of_yards_data[1] = no_of_yards_data[1] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[1] = pass_list[1] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[1] = run_list[1] + 1

    elif(yards_length == 2):
      no_of_yards_data[2] = no_of_yards_data[2] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[2] = pass_list[2] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[2] = run_list[2] + 1

    elif(yards_length == 3):
      no_of_yards_data[3] = no_of_yards_data[3] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[3] = pass_list[3] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[3] = run_list[3] + 1

    elif (yards_length == 4):
      no_of_yards_data[4] = no_of_yards_data[4] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[4] = pass_list[4] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[4] = run_list[4] + 1

    elif (yards_length == 5):
      no_of_yards_data[5] = no_of_yards_data[5] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[5] = pass_list[5] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[5] = run_list[5] + 1

    elif (yards_length == 6):
      no_of_yards_data[6] = no_of_yards_data[6] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[6] = pass_list[6] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[6] = run_list[6] + 1

    elif (yards_length == 7):
      no_of_yards_data[7] = no_of_yards_data[7] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[7] = pass_list[7] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[7] = run_list[7] + 1

    elif (yards_length == 8):
      no_of_yards_data[8] = no_of_yards_data[8] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[8] = pass_list[8] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[8] = run_list[8] + 1

    elif (yards_length == 9):
      no_of_yards_data[9] = no_of_yards_data[9] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[9] = pass_list[9] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[9] = run_list[9] + 1

    elif (yards_length == 10):
      no_of_yards_data[10] = no_of_yards_data[10] + 1

      if(data[i]['Passer_Name'] != 'NA'):
        pass_list[10] = pass_list[10] + 1
      if(data[i]['Runner_Name'] != 'NA'):
        run_list[10] = run_list[10] + 1

    else:
      print('Test')


print(no_of_yards_data)
print(pass_list)
print(run_list)


#------------Tied Data Visualization###################################################
line_1, = plt.plot([1,2,3,4,5,6,7,8,9,10,11],no_of_yards_data, '-o', label="Yards Away from Scoring")

line_2, = plt.plot([1,2,3,4,5,6,7,8,9,10,11],run_list, '-o', label="Runs")

line_3, = plt.plot([1,2,3,4,5,6,7,8,9,10,11],pass_list, '-o', label="Passes")

plt.legend(handles=[line_1, line_2, line_3])

plt.show()
