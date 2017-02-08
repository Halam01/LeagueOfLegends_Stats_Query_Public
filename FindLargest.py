'''
Created on Jan 22, 2015

@author: Hanna
'''

import json
import urllib.parse
import urllib.request
import SummonerInfo

def get_url(summonerID: int, season : str) -> str:
    IDstr = str(summonerID)
    return SummonerInfo.BASE_URL + '/lol/na/v1.3/stats/by-summoner/' + IDstr + '/ranked?season='+season+'&api_key='+ SummonerInfo.API_KEY


if __name__ == '__main__':
    '''Getting IDs'''
    names = input('Enter summoner name: ')
    sums = [names]
    response = SummonerInfo.get_response(SummonerInfo.build_url(sums))
    ids = SummonerInfo.get_id(response)
    '''Getting Stats'''
    season = input('Choose a season:')
    for id in ids:
        url = get_url(id, season)
        stats = SummonerInfo.get_response(url)
        print('Stats for {sum} in {seas}:'.format(sum = names, seas = season))
        for k in stats['champions']:
            if k['id'] == 0:
                for i in k['stats']:
                    if i == 'totalDamageDealt':
                        print('Your total damage dealt is: ' + str(k['stats'][i]))
                    if i == 'totalDamageTaken':
                        print('Your total damage taken is: ' + str(k['stats'][i]))
                    if i == 'totalHeal':
                        print('Your total damage healed is: '  + str(k['stats'][i]))
                    if i == 'maxChampionsKilled':
                        print('Your maximum number of kills in a single game is: ' + str(k['stats'][i]))
                    if i == 'maxNumDeaths':
                        print('The most you have died in a single game is: ' + str(k['stats'][i]))
                    if i == 'totalMinionKills':
                        print('The total number of minions you have killed is: ' + str(k['stats'][i]))
                    if i == 'totalGoldEarned':
                        print('You earned a total of ' + str(k['stats'][i]) + ' gold.')
                    if i == 'maxTimeSpentLiving':
                        seconds = k['stats'][i]
                        minutes = 0
                        hours = 0
                        if seconds >= 60:
                            minutes = round(seconds/60)
                            seconds = round(seconds%60)
                            if minutes >= 60:
                                hours = round(minutes/60)
                                minutes = round(minutes%60)
                        print('The longest you have lived in a single game is: {h}hours {m} minutes and {s} seconds.'.format(h = hours, m = minutes, s = seconds))
                    if i == 'maxLargestCriticalStrike':
                        print('Your Largest Critical Strike is: ' + str(k['stats'][i]))
                    if i == 'maxTimePlayed':
                        seconds = k['stats'][i]
                        minutes = 0
                        hours = 0
                        if seconds >= 60:
                            minutes = round(seconds/60)
                            seconds = round(seconds%60)
                            if minutes >= 60:
                                hours = round(minutes/60)
                                minutes = round(minutes%60)
                        print('Your longest game took: {h}hours {m} minutes and {s} seconds.'.format(h = hours, m = minutes, s = seconds))
                        

