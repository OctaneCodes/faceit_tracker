import requests

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
team_id = "00e73bea-fe0f-4083-aa1a-02392ba2401f"

url = f"https://open.faceit.com/data/v4/teams/{team_id}"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    team_data = response.json()

    print(f"Team Name: {team_data.get('name')}")
    print(f"Nickname: {team_data.get('nickname')}")
    print(f"Avatar: {team_data.get('avatar')}")
    print(f"Region: {team_data.get('region', 'N/A')}")
    print(f"Roster:")

    for player in team_data.get("members", []):
        print(f" - Nickname: {player['nickname']} (Player ID: {player['user_id']})")
else:
    print(f"Error {response.status_code}: {response.text}")
