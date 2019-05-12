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
        for file in glob.glob(path):
            txtfiles.append(file)
        count=-1

        for i in txtfiles:

            for line in open(i).readlines():
                data = json.loads(line)
                for length in range(len(data)):
                    count += 1
                    if int(data[length]['Yards_Away_From_Scoring']) > 1 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 30:
                        field = "0-30Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 30 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 60:
                        field = "30-60Yrds"
                    elif int(data[length]['Yards_Away_From_Scoring']) > 60 and int(
                            data[length]['Yards_Away_From_Scoring']) <= 90:
                        field = "60-90Yrds"
                    else:
                        field = "90-100Yrds"
                    ls.append(str(
                            field+','+data[length]['Pass_Direction']+','+ data[length]['Passer_Name']+
                            ',' + data[length]['Receiver_Name']))


        # write data to the text file: data.basket
        f = open('original.basket', 'w')
        for item in ls:
            f.write(item + '\n')
        f.close()

        # Load data from the text file: data.basket
        data = Orange.data.Table("original.basket")


        # Identify association rules with supports at least 0.1
        rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.1)


        # print out rules
        print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
        for r in rules[:]:
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

        ls=[]
        for line in open('original.basket').readlines():
            ls.append(line)
        ls0=[]
        for i in ls:
            ls0.append(i.split(','))

        ls1=[]
        for i in ls0:
            if(i[2] not in ls1):
                ls1.append(i[2])

        count=0
        for i in ls1:
            count+=1
            for j in ls0:
                if(i==j[2]):
                    f = open('data_'+str(count)+'.basket', 'a')
                    f.write(j[1]+','+j[2]+','+j[3] + '\n')
                f.close()

        data = Orange.data.Table("data_1.basket")


        # Identify association rules with supports at least 0.2
        rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.2)

        output_file = open("Association_Rules/" + team + "/" + str(quarter) + "/" + str(stat) + "/" + team + "_" + str(quarter) + "_" + str(stat) + "_direction.txt","w+")
        # print out rules
        print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
        output_file.write("%4s %4s  %s" % ("Supp", "Conf", "Rule"))
        output_file.write("\n")
        for r in rules[:]:
            output_file.write("%4.1f %4.1f  %s" % (r.support, r.confidence, r))
            output_file.write("\n")
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

        i = 0
        while i < count:
            i = i + 1
            os.remove('data_' + str(i) + '.basket')

        os.remove("original.basket")
      except Exception as ex:
        print ex
        pass
