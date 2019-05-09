import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

graph_dir = os.curdir + "/Generated_Graphs"
try:  # create a new directory to store the files
    os.mkdir(graph_dir)
except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
    pass # directory exists   

Teams = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAC","JAX","KC","LA","LAC","MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI","PIT","SD","SEA","SF","STL","TB","TEN","WAS"]
Quarters = ["1","2","3","4","5"]
Status = ["Winning","Losing","Tied"]
for team in Teams:
  try:  # create a new directory to store the files
      os.mkdir(graph_dir + "/" + team)
  except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
      pass # directory exists 
  for quarter in Quarters:
    try:  # create a new directory to store the files
      os.mkdir(graph_dir + "/" + team + "/" + str(quarter))
    except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
        pass # directory exists 
    for stat in Status:
      try:  # create a new directory to store the files
        os.mkdir(graph_dir + "/" + team + "/" + str(quarter) + "/" + str(stat))
      except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
          pass # directory exists 
        
      file_name = 'Teams/{}/{}/{}/data.json'.format(team, str(quarter), str(stat))
      no_of_yards_data = (np.zeros(11, dtype=int))
      pass_list = (np.zeros(11, dtype=int))
      run_list = (np.zeros(11, dtype=int))
      try:
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

          line_2, = plt.plot([0,10,20,30,40,50,60,70,80,90,100],run_list, '-o', label="Runs")
          line_3, = plt.plot([0,10,20,30,40,50,60,70,80,90,100],pass_list, '-o', label="Passes")
          plt.title(team + " Play Tendencies // Qtr: " + str(quarter) + " // " + str(stat))
          plt.ylabel("Number of plays")
          plt.xlabel("Yards from scoring")
          plt.legend(handles=[line_2, line_3])
          plt.savefig("Generated_Graphs/" + team + "/" + str(quarter) + "/" + str(stat) + "/" + team + "_" + str(quarter) + "_" + str(stat) + "_line")
          plt.close()

          bar_1 = plt.bar(np.arange(11),run_list,0.35,label="Runs")
          bar_2 = plt.bar(np.arange(11) + 0.35,pass_list,0.35,label="Passes")
          plt.xticks(np.arange(11) + 0.35 / 2, ('0-10', '10-20', '20-30', '30-40','40-50', '50-60', '60-70', '70-80','80-90', '> 90'))
          plt.title(team + " Play Tendencies // Qtr: " + str(quarter) + " // " + str(stat))
          plt.ylabel("Number of plays")
          plt.xlabel("Yards from scoring")
          plt.legend(loc='best')
          plt.savefig("Generated_Graphs/" + team + "/" + str(quarter) + "/" + str(stat) + "/" + team + "_" + str(quarter) + "_" + str(stat) + "_bar")
          plt.close()
      except:
        pass
