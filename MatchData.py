import urllib.request, urllib.parse, urllib.error
import json

def IsStarting(gameid):
    
    year = gameid[:4]
    month = gameid[4:6]
    
    url = "https://sportsdata.pstatic.net/data//worldfootball/{}/{}/{}.json".format(year, month, gameid)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js:
        print('==== Failure To Retrieve ====')
        print(data)
        exit()
    #출장 안함
    son = False
    for home_away in js["lineup"].values():
        for playerId in home_away.values():
            if playerId["player_full_name"] == "손흥민" and playerId["sub"] == "No":
                #선발출장
                son = True
            elif playerId["player_full_name"] == "손흥민" and playerId["sub"] == "Yes":
                #후보명단
                son = False

    return son
