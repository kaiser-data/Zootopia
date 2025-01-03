import requests

def get_api_key():
    with open("API_KEY_NINJA.txt", "r") as f:
        API_KEY = f.read()
    return API_KEY

def get_animals(animal):
    API_KEY = get_api_key()
    URL = "https://api.api-ninjas.com/v1/animals"
    PARAMS = {
        "name": animal
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


def main():
    animal = input("Enter a name of an animal: ")
    get_animals(animal)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()