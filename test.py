import requests
import time

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
tournament_id = "f56331e8-131a-4c50-b7db-eec8b010ff98"  # Replace with your tournament ID

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

matches_url = f"https://open.faceit.com/data/v4/tournaments/{tournament_id}/matches"

def get_teams_from_tournament_matches(tournament_id):
    response = requests.get(matches_url, headers=headers)
    time.sleep(1.1)  # Rate limiter: wait 1.1 seconds after each request

    if response.status_code == 200:
        data = response.json()
        matches = data.get("items", [])
        team_ids = set()

        for match in matches:
            teams = match.get("teams", {})
            team1 = teams.get("faction1", {})
            team2 = teams.get("faction2", {})

            if team1.get("team_id"):
                team_ids.add(team1["team_id"])
            if team2.get("team_id"):
                team_ids.add(team2["team_id"])

        print(f"Teams found in matches for tournament {tournament_id}:")
        for tid in team_ids:
            print(f"- {tid}")
    else:
        print(f"Failed to fetch matches for tournament {tournament_id}: {response.status_code} {response.text}")

if __name__ == "__main__":
    get_teams_from_tournament_matches(tournament_id)
