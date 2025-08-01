import requests
import time
import csv

SEASON_ID = "3de05c27-da01-4ede-9319-f5b3f16dfb1f"
BASE_URL = f"https://api.faceit.com/leaderboards/v1/leaderboards/by-season/{SEASON_ID}"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    # Optionally add cookies from authenticated browser session if needed
}

def fetch_leaderboard(season_id, offset=0, limit=50):
    url = f"{BASE_URL}?offset={offset}&limit={limit}"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        return resp.json().get("items", [])
    else:
        print(f"Error {resp.status_code}: {resp.text}")
        return []

def get_all_teams(season_id):
    teams = []
    offset = 0
    while True:
        items = fetch_leaderboard(season_id, offset)
        if not items:
            break
        teams.extend(items)
        offset += len(items)
        time.sleep(1)
    return teams

if __name__ == "__main__":
    all_teams = get_all_teams(SEASON_ID)
    print(f"Found {len(all_teams)} entries")
    # Example: export CSV
    with open("teams.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "nickname", "player_id", "team_id", "elo"])
        for e in all_teams:
            writer.writerow([
                e.get("rank"),
                e.get("nickname"),
                e.get("player_id"),
                e.get("team_id"),
                e.get("elo", "")
            ])
    print("Exported to teams.csv")
