# Use this file to define functions that will output to files
def analysis(all_data):
    analysis = open("analysis.txt","w+")
    for passer in all_data:
        output_passer = True
        for receiver in passer:
            output_receiver = True
            for quarter in receiver:
                output_quarter = True
                for completion in quarter:
                    output_completion = True
                    for attempt in completion:
                        if(output_passer):
                            analysis.write("Passer: " + attempt['passer_player_name'] + "\n")
                            output_passer = False
                        if(output_receiver):
                            analysis.write("-- Receiver: " + attempt['receiver_player_name'] + "\n")
                            output_receiver = False
                        if(output_quarter):
                            analysis.write("-- -- Quarter: " + attempt['qtr'] + "\n")
                            output_quarter = False
                        if(output_completion):
                            comp = ""
                            if(attempt['complete_pass'] == "1"):
                                    comp = "Yes"
                            else:
                                    comp = "No" 
                            analysis.write("-- -- -- Completed Pass?: " + comp + "\n")
                            output_completion = False
                        analysis.write("-- -- -- -- Yards Gained : " + attempt['yards_gained'] + " // Pass Type: " + attempt['pass_length'] + "\n")
                    
    analysis.close
    print("Analysis Output Completed")

def statistics(all_data):
    statistics = open("statistics.txt","w+")
    for passer in all_data:
        output_passer = True
        for receiver in passer:
            output_receiver = True
            for quarter in receiver:
                is_complete = 0
                total_complete = 0
                output_quarter = True
                for completion in quarter:
                    for attempt in completion:
                        if(output_passer):
                            statistics.write("Passer: " + attempt['passer_player_name'] + "\n")
                            output_passer = False
                        if(output_receiver):
                            statistics.write("-- Receiver: " + attempt['receiver_player_name'] + "\n")
                            output_receiver = False
                        if(output_quarter):
                            statistics.write("-- -- Quarter " + attempt['qtr'] + " Accuracy: ")
                            output_quarter = False
                        if(attempt['complete_pass'] == "1"):
                            is_complete = is_complete + 1
                            total_complete = total_complete + 1
                        else:
                            total_complete = total_complete + 1 
                statistics.write("" + str(is_complete) + " / " + str(total_complete) + "\n")
    statistics.close
    print("Statistics Output Completed")