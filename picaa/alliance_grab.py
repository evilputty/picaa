import json
import requests

currentpage = 1

# Todo: Add cache info


# Get list of EVE alliances
print('Fetching: https://crest-tq.eveonline.com/alliances/?page='+str(currentpage))
r = requests.get('https://crest-tq.eveonline.com/alliances/?page='+str(currentpage))
json_data = r.json()
with open('alliance.' + str(currentpage) +'.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)
currentpage += 1
# Get number of pages
pages =  json_data['pageCount']
print("Number of pages: " + str(pages))


while currentpage < pages+1:
    print('Fetching: https://crest-tq.eveonline.com/alliances/?page='+str(currentpage))
    r = requests.get('https://crest-tq.eveonline.com/alliances/?page='+str(currentpage))
    json_data = r.json()
    with open('alliance.' + str(currentpage) +'.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
    currentpage += 1
