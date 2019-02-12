import csv
def scrape():
    all_data = []
    with open('PlayByPlay.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            all_data.append(row)
    print("Data Collection Completed")
    return all_data