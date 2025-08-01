import requests

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
MATCH_ID = "1-df4a39a2-c812-4ffb-85a3-e97547a11038"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

def get_match_details(match_id):
    url = f"https://open.faceit.com/data/v4/matches/{match_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    match_details = get_match_details(MATCH_ID)
    if match_details:
        print(f"Match ID: {match_details.get('match_id')}")
        print(f"Status: {match_details.get('status')}")
        print(f"Game: {match_details.get('game_name')}")
        print(f"Competition Name: {match_details.get('competition_name')}")
        print(f"Competition ID: {match_details.get('competition_id')}")
        
        # Hosting entity info
        entity_id = match_details.get('entity_id')
        entity_type = match_details.get('entity_type')
        print(f"Hosting Entity ID: {entity_id}")
        print(f"Hosting Entity Type: {entity_type}")
        
        print("Teams:")
        for team_key, team_data in match_details.get('teams', {}).items():
            print(f"  {team_key}: {team_data.get('name')}")
            print(f"    Players:")
            for player in team_data.get('roster', []):
                print(f"      - {player.get('nickname')}")
    else:
        print("Failed to get match details.")