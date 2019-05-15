# Use this file to define functions that will output to files
import json
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

stats_dir = os.curdir + "/Generated_Stats"
try:  # create a new directory to store the files
    os.mkdir(stats_dir)
except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
    pass # directory exists   

Teams = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAC","JAX","KC","LA","LAC","MIA","MIN","NE","NO","NYG","NYJ","OAK","PHI","PIT","SD","SEA","SF","STL","TB","TEN","WAS"]
Quarters = ["1","2","3","4","5"]
Status = ["Winning","Losing","Tied"]
for team in Teams:
  try:  # create a new directory to store the files
      os.mkdir(stats_dir + "/" + team)
  except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
      pass # directory exists 
  for quarter in Quarters:
    try:  # create a new directory to store the files
      os.mkdir(stats_dir + "/" + team + "/" + str(quarter))
    except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
        pass # directory exists 
    for stat in Status:
      try:  # create a new directory to store the files
        os.mkdir(stats_dir + "/" + team + "/" + str(quarter) + "/" + str(stat))
      except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
          pass # directory exists 
        
      file_name = 'Teams/{}/{}/{}/data.json'.format(team, str(quarter), str(stat))
      try:
        with open(file_name, 'r') as json_file:
          data = json.load(json_file)
          y = []
          indices = dict()
          for play in data:
              term = play['Receiver_Name']
              if(indices.has_key(term) == False):
                  indices.update({term:1})
              else:
                  i = indices.get(term)
                  indices.update({term: i + 1})
              y.append(indices.get(term))
          print(indices)
          sorted_view = [ (v,k) for k,v in indices.iteritems() ]
          sorted_view.sort(reverse=False)

          for key,value in sorted_view:
            print(str(key) + " => " + str(value))
  
        output_file = open("Generated_Stats/" + team + "/" + str(quarter) + "/" + str(stat) + "/" + team + "_" + str(quarter) + "_" + str(stat) + "_passing_attempts_stats.txt","w+")
        output_file.write("Quarter: " + str(quarter) + " when " + str(stat) + "\n")
        output_file.write("Number of times with ball => Player Name \n")
        for key,value in sorted_view:
            if value == 'NA':
                value = 'Run Play'
            output_file.write(str(key) + " => " + str(value) + "\n")
      except:
        pass

#### RUNS ####
for team in Teams:
  try:  # create a new directory to store the files
      os.mkdir(stats_dir + "/" + team)
  except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
      pass # directory exists 
  for quarter in Quarters:
    try:  # create a new directory to store the files
      os.mkdir(stats_dir + "/" + team + "/" + str(quarter))
    except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
        pass # directory exists 
    for stat in Status:
      try:  # create a new directory to store the files
        os.mkdir(stats_dir + "/" + team + "/" + str(quarter) + "/" + str(stat))
      except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
          pass # directory exists 

      file_name = 'Teams/{}/{}/{}/data.json'.format(team, str(quarter), str(stat))
      try:
        with open(file_name, 'r') as json_file:
          data = json.load(json_file)
          y = []
          indices = dict()
          for play in data:
              term = play['Runner_Gap']
              if(indices.has_key(term) == False):
                  indices.update({term:1})
              else:
                  i = indices.get(term)
                  indices.update({term: i + 1})
              y.append(indices.get(term))
          print(indices)
          sorted_view = [ (v,k) for k,v in indices.iteritems() ]
          sorted_view.sort(reverse=False)

          for key,value in sorted_view:
            print(str(key) + " => " + str(value))
  
        output_file = open("Generated_Stats/" + team + "/" + str(quarter) + "/" + str(stat) + "/" + team + "_" + str(quarter) + "_" + str(stat) + "_runner_gap_stats.txt","w+")
        output_file.write("Quarter: " + str(quarter) + " when " + str(stat) + "\n")
        output_file.write("Number of times run to gap => Gap name \n")
        for key,value in sorted_view:
            if value == 'NA':
                value = 'Pass Play'
            output_file.write(str(key) + " => " + str(value) + "\n")
      except:
        pass