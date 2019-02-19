from scrape import scrape
from group import group
from output import analysis, statistics

def run():
    data = scrape()
    grouped_data = group(data)
    analysis(grouped_data)
    statistics(grouped_data)
    # define more tasks here
    print("Run Completed Successfully")

if __name__ == '__main__' :
    run()