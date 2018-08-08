from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import json

with urllib.request.urlopen("https://sports.news.naver.com/wfootball/schedule/index.nhn") as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    jstag  = soup.find("body").find('div', {"id":"wrap"}).find_all('script', {'type':'text/javascript'})#.find('div', {'id':'content'}).find('div', {'class':'schedule_month_area'}).find('div', {'class':'schedule_month_table'}).find('table').find('tbody').find('tr')
    ScheduleTag = jstag[-4]
    ScheduleText = ScheduleTag.get_text()
    ScoreboardText = ScheduleText[ScheduleText.find('scoreboardList')-1:]
    Newlineindex = ScoreboardText.find('\n')
    ScoreboardText = ScoreboardText[17:Newlineindex-2]
    #json으로 변환
    try:
        ScoreboardJson = json.loads(ScoreboardText)
        with open('scoreboard.json', 'w') as f:
            json.dump(ScoreboardJson, f, indent=4)
            print('==== Success To Retrieve ====')
    except:
        print('==== Failure To Retrieve ====')
        print(ScoreboardText)
        exit()

    # try:
    #     with open('scoreboard.json', 'r') as f:
    #         print(json.load(f))
    # except:
    #     print('==== Failure To DataLoad ====')
    #     exit()
