import requests

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"

url = "https://open.faceit.com/data/v4/leagues"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    leagues = response.json().get("items", [])
    for league in leagues:
        print(f"League ID: {league['league_id']}, Name: {league['name']}")
else:
    print(f"Error fetching leagues: {response.status_code} - {response.text}")


a14b8616-45b9-4581-8637-4dfd0b5f6af8