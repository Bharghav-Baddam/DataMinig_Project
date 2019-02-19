from itertools import groupby, ifilter
import itertools

def group(all_data):
    grouped_data = []
    # Sort and group by the passer
    sorted_passers = sorted(all_data, key = takePasser) 
    grouped_passers = groupby(sorted_passers, lambda item: item['passer_player_name'])
    # Loop over each passer
    for passer_name, grouped_content in grouped_passers: 
        passer_group = []
        # Sort and group each receiver that exists for the passer
        sorted_receivers = sorted(grouped_content, key = takeReceiver)
        grouped_receivers = groupby(sorted_receivers, lambda item: item['receiver_player_name'])
        # Loop over each receiver
        for receiver_name, grouped_content_receivers in grouped_receivers:
                receiver_group = []
                # Sort and group each throw to the receiver by quarter
                sorted_quarters = sorted(grouped_content_receivers, key = takeQuarter)
                grouped_quarters = groupby(sorted_quarters, lambda item: item['qtr'])
                # Loop over each quarter:
                for quarter_id, grouped_content_quarter in grouped_quarters:
                        quarter_group = []
                        # Sort and group each throw to the receiver by complete or incomplete
                        sorted_completions = sorted(grouped_content_quarter, key = takeCompletion)
                        grouped_completions = groupby(sorted_completions, lambda item: item['complete_pass'])
                        # Loop over each completion (1) or non completion (0)
                        for completion_id, grouped_content_completion in grouped_completions:
                                completion_group = []
                                for final_content in grouped_content_completion:
                                        completion_group.append(final_content)
                                quarter_group.append(completion_group)
                        receiver_group.append(quarter_group)
                passer_group.append(receiver_group)
        grouped_data.append(passer_group)            
    print("Data Grouping Completed")
    
    # Return an array with the following structure
    # - Passer
    # -- Receiver
    # --- Quarter
    # ---- Completion (Yes or No)
    # ----- Play
    # ----- Play
    # .... etc
    
    return grouped_data

def takePasser(elem):
        return elem['passer_player_id']

def takeReceiver(elem):
        return elem['receiver_player_id']

def takeQuarter(elem):
        return elem['qtr']

def takeCompletion(elem):
        return elem['complete_pass']
