from nba_api.stats.endpoints import scoreboardv2
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
	data = get(BASE_URL + ALL_JSON, verify=False).json()
	links = data['links']
	return links

def get_scoreboard():
	scoreboard = get_links()["currentScoreboard"]
	data = get(BASE_URL + scoreboard).json()['games']
	
	for game in data:
		home_team = game["hTeam"]
		away_time = game["vTeam"]
		clock = game['clock']
		period = game['period']
	
		print(f"{home_team} vs {away_team}, {clock}, {period}")
		
get_scoreboard()
