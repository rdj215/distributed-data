import json

# Assign json from scraped site to data var 
with open('C:/Users/ryanj\dev-projects\distributed-data-app\web_crawler\web_crawler\crawler\spiders\election_board_officials.json') as file:
    data = json.load(file)


def roles_by_ward(data):
    d = {}
    for record in data:
        if not d[record['ward']]:
            d[record['ward']] = 1

print(data)

