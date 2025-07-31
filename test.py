import requests

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
player_nickname = "dyragu"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

# 1. Get player info to get player ID
player_resp = requests.get(
    f"https://open.faceit.com/data/v4/players?nickname={player_nickname}",
    headers=HEADERS
)
player_data = player_resp.json()
player_id = player_data.get("player_id")
if not player_id:
    print("Player not found")
    exit()

# 2. Get player's match history
matches_resp = requests.get(
    f"https://open.faceit.com/data/v4/players/{player_id}/history",
    headers=HEADERS,
    params={"game": "csgo", "offset": 0, "limit": 100}  # adjust pagination
)
matches_data = matches_resp.json()
matches = matches_data.get("items", [])

# 3. Extract unique leagues from matches
league_ids = set()
for match in matches:
    league_id = match.get("league_id")
    if league_id:
        league_ids.add(league_id)

print(f"Player {player_nickname} played in leagues:")
for lid in league_ids:
    print(f"- {lid}")
