import json
import sys
import os
import glob
import json
import Orange

graph_dir = os.curdir + "/Association_Rules"
print(graph_dir)
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
        
      path = 'Teams/{}/{}/{}/*.json'.format(team, str(quarter), str(stat))
      try:
        txtfiles = []
        ls=[]
        for item in glob.glob(path):
            txtfiles.append(item)

        for i in txtfiles:
            for line in open(i).readlines():
                data = json.loads(line)
                for length in range(len(data)):
                    if int(data[length]['Yards_Away_From_Scoring']) <= 10:
                        field = "0-10Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 10 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 20:
                        field = "10-20Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 20 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 30:
                        field = "20-30Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 30 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 40:
                        field = "30-40Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 40 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 50:
                        field = "40-50Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 50 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 60:
                        field = "50-60Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 60 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 70:
                        field = "60-70Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 70 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 80:
                        field = "70-80Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 80 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 90:
                        field = "80-90Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 90 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 100:
                        field = "90-100Yrds"
                    if data[length]['Passer_Name'] not in 'NA':
                        ls.append(str(
                            data[length]['Passer_Name'] +
                            ',' + data[length]['Receiver_Name']))
        # write data to the text file: data.basket
        f = open('data.basket', 'w')
        for item in ls:
            f.write(item + '\n')
        f.close()

        # Load data from the text file: data.basket
        data = Orange.data.Table("data.basket")


        # Identify association rules with supports at least 0.1
        rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.1)
        output_file = open("Association_Rules/" + team + "/" + str(quarter) + "/" + str(stat) + "/" + team + "_" + str(quarter) + "_" + str(stat) + "_passer.txt","w+")
        # write rules to file
        print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
        output_file.write("%4s %4s  %s" % ("Supp", "Conf", "Rule"))
        output_file.write("\n")
        for r in rules[:]:
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)
            output_file.write("%4.1f %4.1f  %s" % (r.support, r.confidence, r))
            output_file.write("\n")
        output_file.close()
        os.remove("data.basket")
      except Exception as ex:
        print ex
        pass
