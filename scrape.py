import csv
with open('PlayByPlay.csv', 'rb') as csvfile:
     spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
     for row in spamreader:
         print (row['desc'] + "\n")

