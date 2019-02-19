import csv
def scrape():
        all_data = []
        with open('PlayByPlay.csv', 'rb') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
                for row in reader:
                        if (row['passer_player_id'] != 'NA' and row['receiver_player_id'] != 'NA'):
                                all_data.append(row)

        print("Data Collection Completed")
        return all_data