import csv
all_data = []
with open('PlayByPlay.csv', 'rb') as csvfile:
     reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
     for row in reader:
         all_data.append(row)
print("Data Collection Completed")

#  Possible ideas:
#  Predict for each quarterback, who are they most likely going to pass to when trailing in the 4th quarter