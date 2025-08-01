import requests

API_KEY = "8b57056a-712d-450f-9015-8caeaf5f6d3c"
ORGANIZER_ID = "08b06cfc-74d0-454b-9a51-feda4b6b18da"  # you said you have this

url = f"https://open.faceit.com/data/v4/organizers/{ORGANIZER_ID}/championships"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    for champ in data.get("items", []):
        print(f"Championship Name: {champ['name']}")
        print(f"Championship ID: {champ['championship_id']}")
        print(f"Start date (timestamp): {champ['championship_start']}")
        print("---")
else:
    print(f"Error {response.status_code}: {response.text}")

'''url = f"https://open.faceit.com/data/v4/organizers/{ORGANIZER_ID}"
response = requests.get(url, headers=headers)
print(response.json())'''

