from itertools import groupby, ifilter
import itertools

def group(all_data):
    grouped_data = []
    print("Data Grouping Completed")
    sorted_data = sorted(all_data, key = takePasser)
    grouped_groupby = groupby(sorted_data, lambda item: item['passer_player_id'])
    for passer_id, grouped_content in grouped_groupby:
        passer_group = []
        for content in grouped_content:
                passer_group.append(content)
        grouped_data.append(passer_group)
    return grouped_data

def takePasser(elem):
        return elem['passer_player_id']
