import requests
from typing import List, Dict

def fetch_data(animal: str, api_key: str) -> List[Dict]:
    """
    Fetch animal data from the API based on the given animal name.

    Args:
        animal (str): Name of the animal to fetch data for.
        api_key (str): API key for authenticating the request.

    Returns:
        List of dictionaries containing data about animals.
    """

    api_url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal}
    headers = {"X-Api-Key": api_key}

    # get response
    response = requests.get(api_url, headers=headers, params=params)

    # Check if the response is successful, otherwise return an empty list.
    if response.status_code == 200:
        animal_data = response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        animal_data = []

    return animal_data