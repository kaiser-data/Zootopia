import requests
with open("API_KEY_NINJA.txt", "r") as f:
    API_KEY = f.read()

URL = "https://api.api-ninjas.com/v1/animals"
PARAMS = {
    "name": "fox"
}
headers = {
    "X-Api-Key": API_KEY
}

response = requests.get(URL, headers=headers, params=PARAMS)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")


