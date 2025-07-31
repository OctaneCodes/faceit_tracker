import requests
import time

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
ORGANIZER_ID = "08b06cfc-74d0-454b-9a51-feda4b6b18da"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

def get_championships_by_organizer(organizer_id):
    championships = []
    offset = 0
    limit = 50  # max 100 allowed, safer to use 50
    while True:
        url = f"https://open.faceit.com/data/v4/championships"
        params = {
            "organizer_id": organizer_id,
            "offset": offset,
            "limit": limit
        }
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch championships: {response.status_code} {response.text}")
            break
        
        data = response.json()
        items = data.get("items", [])
        if not items:
            break
        
        championships.extend(items)
        offset += len(items)
        
        if len(items) < limit:
            # no more items
            break
        
        # Rate limiting: Faceit allows ~20 requests per minute (check docs to confirm)
        time.sleep(3)  # wait 3 seconds before next request
    
    return championships

def main():
    all_champs = get_championships_by_organizer(ORGANIZER_ID)
    print(f"Found {len(all_champs)} championships for organizer {ORGANIZER_ID}")
    for champ in all_champs:
        print(f"- {champ.get('name')} (ID: {champ.get('championship_id')})")

if __name__ == "__main__":
    main()
