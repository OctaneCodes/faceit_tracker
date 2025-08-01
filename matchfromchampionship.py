import requests

# Replace with your actual FACEIT API key
API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"

# Replace with the championship ID you want to query
CHAMPIONSHIP_ID = "c930bc70-7428-4b1e-af65-c9deb797f53"

# Base headers for the API request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

def get_matches_for_championship(championship_id):
    url = f"https://open.faceit.com/data/v4/matches?entity_id={championship_id}&entity_type=championship&limit=50"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        matches = data.get("items", [])
        
        if not matches:
            print("No matches found for this championship.")
            return
        
        for match in matches:
            print(f"Match ID: {match.get('match_id')}")
            print(f"Status: {match.get('status')}")
            
            teams = match.get('teams', {})
            team_names = [team.get('name') for team in teams.values()]
            print(f"Teams: {team_names}")
            print("---")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    get_matches_for_championship(CHAMPIONSHIP_ID)
