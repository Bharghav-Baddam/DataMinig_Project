from scrape import scrape
from group import group

def run():
    data = scrape()
    group_data = group(data)
    #  Define more tasks here

if __name__ == '__main__' :
    run()