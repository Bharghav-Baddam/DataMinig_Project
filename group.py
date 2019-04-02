from itertools import groupby, ifilter
import itertools
import os
import json

# File Structure
# -Teams
# --Quarter
# ---W/L/T ?

team_directory = os.curdir + "/Teams"

def group(all_data):
        try:  # create a new directory to store the files
                os.mkdir(team_directory)
        except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
                pass # directory exists   
        grouped_data = []
        # Sort and group by teams
        sorted_teams = sorted(all_data, key = takeTeam) 
        grouped_teams = groupby(sorted_teams, lambda item: item['Team'])
        # Loop over each team
        for team_name, grouped_content in grouped_teams: 
                try:  # create a new directory to store the files
                        os.mkdir(team_directory + "/" + team_name)
                except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
                        pass # directory exists   
                team_group = []
                # Sort and group by each quarter for the team
                sorted_quarters = sorted(grouped_content, key = takeQuarter)
                grouped_quarters = groupby(sorted_quarters, lambda item: item['Quarter'])
                # Loop over each quarter
                for quarter_id, grouped_content_quarters in grouped_quarters:
                        try:  # create a new directory to store the files
                                os.mkdir(team_directory + "/" + team_name + "/" + quarter_id)
                        except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
                                pass # directory exists
                        quarter_group = []
                        # Sort and group by win/loss/tie
                        sorted_winnin_lossing_tied = sorted(grouped_content_quarters, key = takeDifferential)
                        grouped_winnin_lossing_tied = groupby(sorted_winnin_lossing_tied, lambda item: item['Winning_Losing_Tied'])
                        for win_loss_tie_id, grouped_winnin_lossing_tied_content in grouped_winnin_lossing_tied:
                                try:  # create a new directory to store the files
                                        os.mkdir(team_directory + "/" + team_name + "/" + quarter_id + "/" + win_loss_tie_id)
                                except OSError as file_error:  # if the directory exists then don't create a new one and don't crash
                                        pass # directory exists
                                win_lose_tie = []
                                for final_content in grouped_winnin_lossing_tied_content:
                                        win_lose_tie.append(final_content)
                                with open(team_directory + "/" + team_name + "/" + quarter_id + "/" + win_loss_tie_id + "/" + 'data.json', 'w') as data_dump:
                                        json.dump(win_lose_tie, data_dump)  # write the items list to the file
                                quarter_group.append(win_lose_tie)
                        team_group.append(quarter_group)
                grouped_data.append(team_group)
        print("Data Dump Complete")
        return grouped_data

def takeTeam(elem):
        return elem['Team']

def takeQuarter(elem):
        return elem['Quarter']

def takeDifferential(elem):
        return elem['Winning_Losing_Tied']
