import json

def ExtractGameId():

    try:
        with open('scoreboard.json', 'r') as f:
            js = json.load(f)
            gameid = None
            for match in js:
                if match['homeTeamName'] == '토트넘' or match['awayTeamName'] == '토트넘':
                    gameidIndex = match['textRelayURI'].find('gameId')+7
                    gameid = match['textRelayURI'][gameidIndex:].strip()
                    print("gameid : " + gameid)
            if gameid is None:
                print("토트넘 경기가 없습니다.")
            
    except:
        print('==== Failure To DataLoad ====')
        exit()

    return gameid