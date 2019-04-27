import csv
from collections import OrderedDict

def scrape():
        all_data = []
        with open('Data.csv', 'rb') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
                for row in reader:
                        if ((row.get('passer_player_name') != 'NA' and row.get('receiver_player_name') != 'NA') or row.get('rusher_player_name') != 'NA'):
                                score = int(row.get('total_home_score')) - int(row.get('total_away_score'))
                                win_loss_tie = ""
                                if (row.get('home_team') != row.get('posteam')):
                                        score = int(row.get('total_away_score')) - int(row.get('total_home_score'))
                                if(score > 0):
                                        win_loss_tie = "Winning"
                                elif(score < 0):
                                        win_loss_tie = "Losing"
                                else:
                                        win_loss_tie = "Tied"
                                all_data.append(OrderedDict([
                                ('Team', row.get('posteam')),
                                ('Score_Differential', str(score)),
                                ('Winning_Losing_Tied', win_loss_tie),
                                ('Time_Remaining_In_Seconds', row.get("game_seconds_remaining")),
                                ('Quarter', row.get('qtr')),
                                ('Yards_Away_From_Scoring', str(100 - int(row.get('yardline_100')))),
                                ('Passer_Name', row.get('passer_player_name')),
                                ('Receiver_Name', row.get('receiver_player_name')),
                                ('Pass_Type', row.get('pass_length')),
                                ('Pass_Direction', row.get('pass_location')),
                                ('Pass_Complete', row.get('complete_pass')),
                                ('Runner_Name', row.get('rusher_player_name')),
                                ('Runner_Gap', row.get('run_gap')),
                                ('Yards_Gained', row.get('yards_gained')),
                                ]))

        print("Data Collection Completed")
        return all_data