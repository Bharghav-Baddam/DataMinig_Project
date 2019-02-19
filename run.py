from scrape import scrape
from group import group

def run():
    data = scrape()
    group(data)
    # define more tasks here
    print("Run Completed Successfully")

if __name__ == '__main__' :
    run()