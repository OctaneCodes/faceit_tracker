import requests

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
COMPETITION_ID = "a14b8616-45b9-4581-8637-4dfd0b5f6af8"  # e.g., the entity_id from match details

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

def get_matches_from_competition(competition_id, limit=50, offset=0):
    url = f"https://open.faceit.com/data/v4/matches"
    params = {
        "entity_id": competition_id,
        "entity_type": "competition",  # this is the type FACEIT expects for competitions
        "limit": limit,
        "offset": offset
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    offset = 0
    limit = 50
    all_matches = []

    while True:
        data = get_matches_from_competition(COMPETITION_ID, limit=limit, offset=offset)
        if not data:
            break
        
        matches = data.get("items", [])
        all_matches.extend(matches)
        
        if len(matches) < limit:
            # No more matches to fetch
            break
        
        offset += limit

    print(f"Total matches fetched: {len(all_matches)}")
    for match in all_matches:
        print(f"Match ID: {match.get('match_id')}, Status: {match.get('status')}")
