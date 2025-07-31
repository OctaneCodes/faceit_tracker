import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FACEIT_API_KEY", "8b57056a-712d-450f-9015-8caeaf5f6d3c")
BASE_URL = "https://open.faceit.com/data/v4"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

tournament_id = "49e7fd30-ae54-469c-ac03-ce5a6ecbe2eb"  # replace with your tournament ID

def get_teams_for_tournament(tournament_id):
    url = f"{BASE_URL}/tournaments/{tournament_id}/teams"
    teams = []
    offset = 0
    limit = 100

    while True:
        params = {"offset": offset, "limit": limit}
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code != 200:
            print("Failed to fetch teams.")
            print(response.status_code, response.text)
            return []

        data = response.json()
        items = data.get("items", [])
        if not items:
            break

        for team in items:
            team_id = team.get("team_id")
            nickname = team.get("nickname") or team.get("name")
            print(f"Team: {nickname} (ID: {team_id})")
            teams.append((team_id, nickname))

        if len(items) < limit:
            break
        offset += limit

    return teams

if __name__ == "__main__":
    teams = get_teams_for_tournament(tournament_id)
    print(f"\nTotal teams found: {len(teams)}")
