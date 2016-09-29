import json
import requests
from datetime import datetime

# Initialize some ish
datestring ='%Y-%m-%d %H:%M:%S'
kill_information = []
year = 2016

def kill_times( json_obj, kill_hours={} ):
    if(len(json_obj) > 0):
        for i in range(0, len(json_obj)):
            hour_of_kill = datetime.strptime(json_obj[i]['killTime'], datestring).hour
            if hour_of_kill in kill_hours:
                kill_hours[hour_of_kill] += 1
            else:
                kill_hours[hour_of_kill] = 1
        return kill_hours

def get_alliance_kills(alliance_name, alliance_id, year, page = 1):
    print('Kill data for Alliance: ' + alliance_name + ' ID: ' + str(alliance_id))
    print('Fetching https://zkillboard.com/api/year/'+str(year)+'/allianceID/'+ str(alliance_id) +'/kills/page/'+str(page)+'/')
    r = requests.get('https://zkillboard.com/api/year/'+str(year)+'/allianceID/'+ str(alliance_id) +'/kills/page/'+str(page)+'/')
    json_request = {'data': r.json(), 'status_code': r.status_code}
    return(json_request)

with open('alliance.1.json') as json_file:
    data = json.load(json_file)

# Test run on 10 Alliances
for x in range(0, 10):
    kill_hours = {}
    page = 1
    alliance_data = get_alliance_kills(data['items'][x]['name'], data['items'][x]['id'], year, str(page))

    if len(alliance_data['data']) > 0:
        while(len(alliance_data['data']) == 200):
            kill_hours = kill_times(alliance_data['data'], kill_hours)
            page += 1
            alliance_data = get_alliance_kills(data['items'][x]['name'], data['items'][x]['id'], year, str(page))

        kill_hours = kill_times(alliance_data['data'], kill_hours)


    kill_information += [{'alliance_name': data['items'][x]['name'], 'alliance_id': data['items'][x]['id'], 'kill_hours': kill_hours}]

    #print(kill_information)

with open('kill_stats.json', 'w') as json_file:
    json.dump(kill_information, json_file, indent=4, ensure_ascii=False)
