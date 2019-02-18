from itertools import groupby, ifilter
import itertools

def group(all_data):
    grouped_data = []
    # Sort and group by the passer
    sorted_passers = sorted(all_data, key = takePasser) 
    grouped_passers = groupby(sorted_passers, lambda item: item['passer_player_id'])
    # Loop over each passer
    for passer_id, grouped_content in grouped_passers: 
        passer_group = []
        # Sort and group each receiver that exists for the passer
        sorted_receivers = sorted(grouped_content, key = takeReceiver)
        grouped_receivers = groupby(sorted_receivers, lambda item: item['receiver_player_id'])
        # Loop over each receiver
        for receiver_id, grouped_content_receivers in grouped_receivers:
                receiver_group = []
                # Add like receivers to the same array
                for content in grouped_content_receivers:
                        receiver_group.append(content)
                # Associate the receiver with the passer
                passer_group.append(receiver_group)
        # Add the passer to the list of passers
        grouped_data.append(passer_group)            
    print("Data Grouping Completed")
    
    # Return an array with the following structure
    # - Passer
    # -- Receiver
    # --- Play
    # --- Play
    # --- Play
    # -- Receiver
    # --- Play
    # - Passer
    # .....
    # ..... etc
    
    return grouped_data

def takePasser(elem):
        return elem['passer_player_id']

def takeReceiver(elem):
        return elem['receiver_player_id']
