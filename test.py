import requests
import time

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
tournament_id = "3de05c27-da01-4ede-9319-f5b3f16dfb1f"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

matches_url = f"https://open.faceit.com/data/v4/tournaments/{tournament_id}/matches"

def get_matches_with_retry(url, headers, retries=3, delay=3):
    for attempt in range(retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 500:
            print(f"[Attempt {attempt+1}] Server error 500. Retrying in {delay} seconds...")
            time.sleep(delay)
        else:
            print(f"Non-500 error: {response.status_code} {response.text}")
            break
    return None

def get_teams_from_tournament_matches(tournament_id):
    data = get_matches_with_retry(matches_url, headers)
    if not data:
        print(f"Failed to fetch matches for tournament {tournament_id}.")
        return

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

if __name__ == "__main__":
    get_teams_from_tournament_matches(tournament_id)
