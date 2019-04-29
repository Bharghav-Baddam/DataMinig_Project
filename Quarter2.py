import glob
import os
import json
import Orange


path='./ARI/1/Losing/*.json'
path1='./ARI/1/Losing/*'
path3='./ARI/*/*/*.json'
path2='./ARI/1/Losing/'
path4='./ARI/2/*/*.json'

# files = []
# for i in os.listdir(path2):
#     if i.endswith('.json'):
#         files.append(open(i))
# for i in files:
#     print(i)

txtfiles = []
ls=[]
for file in glob.glob(path4):
    txtfiles.append(file)


for i in txtfiles:
    for line in open(i).readlines():
        data = json.loads(line)
        for length in range(len(data)):
            if int(data[length]['Yards_Away_From_Scoring']) <= 10:
                field = "feild1"
            elif int(data[length]['Yards_Away_From_Scoring']) > 10 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 20:
                field = "feild2"
            elif int(data[length]['Yards_Away_From_Scoring']) > 20 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 30:
                field = "feild3"
            elif int(data[length]['Yards_Away_From_Scoring']) > 30 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 40:
                field = "feild4"
            elif int(data[length]['Yards_Away_From_Scoring']) > 40 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 50:
                field = "feild5"
            elif int(data[length]['Yards_Away_From_Scoring']) > 50 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 60:
                field = "feild6"
            elif int(data[length]['Yards_Away_From_Scoring']) > 60 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 70:
                field = "feild7"
            elif int(data[length]['Yards_Away_From_Scoring']) > 70 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 80:
                field = "feild8"
            elif int(data[length]['Yards_Away_From_Scoring']) > 80 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 90:
                field = "feild9"
            elif int(data[length]['Yards_Away_From_Scoring']) > 90 and int(
                    data[length]['Yards_Away_From_Scoring']) <= 100:
                field = "feild10"
            if data[length]['Quarter'] == '1':
                quarter = 'Quarter1'
            if data[length]['Quarter'] == '2':
                quarter = 'Quarter2'
            if data[length]['Quarter'] == '3':
                quarter = 'Quarter3'
            if data[length]['Quarter'] == '4':
                quarter = 'Quarter4'
            if data[length]['Quarter'] == '5':
                quarter = 'Quarter5'
            # ls.append(str(quarter+','+field+','+data[length]['Passer_Name']+
            #           ','+data[length]['Receiver_Name']))
            # ls.append(str(
            #     quarter + ',' + field + ','+ data[length]['Winning_Losing_Tied']+',' + data[length]['Passer_Name'] +
            #     ',' + data[length]['Receiver_Name']))
            if data[length]['Runner_Name'] not in 'NA':
                ls.append(str(
                    quarter + ',' + field + ',' + data[length]['Runner_Name'] +
                    ',' + data[length]['Receiver_Name']))
            else:
                ls.append(str(
                quarter +','+ data[length]['Passer_Name']+
                ',' + data[length]['Receiver_Name']))
ls.append('K.Warner'+','+'D.Anderson')

# write data to the text file: data.basket
f = open('data.basket', 'w')
for item in ls:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.1)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = rules[0]
for idx, d in enumerate(data):
    print '\nUser {0}: {1}'.format(idx, ls[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)
