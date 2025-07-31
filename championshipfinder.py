import requests
import time

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
GAME_ID = "csgo"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

# Step 1: Get championships for csgo
champ_url = "https://open.faceit.com/data/v4/championships"
params = {"game": GAME_ID, "limit": 5}  # adjust limit

resp = requests.get(champ_url, headers=headers, params=params)
if resp.status_code != 200:
    print(f"Error getting championships: {resp.status_code} {resp.text}")
    exit()

championships = resp.json().get("items", [])

for champ in championships:
    champ_id = champ.get("championship_id")
    print(f"Championship: {champ.get('name')} (ID: {champ_id})")

    # If you have tournament IDs linked here (often not directly), you'd use them to get teams:
    # For demo, let's pretend to have a tournament ID:
    # tournament_id = "some_id"
    # teams_url = f"https://open.faceit.com/data/v4/tournaments/{tournament_id}/teams"
    # Then call to get teams per tournament...

    # You can extend this if you can find tournament IDs from the championship data
    time.sleep(0.5)

