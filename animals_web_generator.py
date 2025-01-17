from dotenv import load_dotenv
from typing import List, Dict
import data_fetcher
import os


def serialize_animal(animal_obj: Dict) -> str:
    """
    Converts an animal object into an HTML list item, presenting its details in a
    structured format.

    Args:
        animal_obj (Dict): Dictionary containing animal details.

    Returns:
        str: HTML string representing the animal in list item format.
    """
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">\n<ul>\n'

    # Add specific animal characteristics if available
    characteristics = animal_obj.get("characteristics", {})
    if "diet" in characteristics:
        output += f"<li><strong>Diet</strong>: {characteristics['diet']}</li>\n"
    if "locations" in animal_obj and animal_obj["locations"]:
        output += (
            f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"
        )
    if "type" in characteristics:
        output += f"<li><strong>Type:</strong> {characteristics['type']}</li>\n"
    if "skin_type" in characteristics:
        output += (
            f"<li><strong>Skin-type:</strong> {characteristics['skin_type']}</li>\n"
        )
    if "lifespan" in characteristics:
        output += (
            f"<li><strong>Lifespan:</strong> {characteristics['lifespan']}</li>\n"
        )
    if "top_speed" in characteristics:
        output += (
            f"<li><strong>Top Speed:</strong> {characteristics['top_speed']}</li>\n"
        )
    if "slogan" in characteristics:
        output += (
            f"<li><strong>Slogan:</strong> {characteristics['slogan']}</li>\n"
        )

    output += '</ul>\n</div>\n</li>\n'
    return output


def create_string_animal_data(animals_data: List[Dict]) -> str:
    """
    Generates a concatenated HTML string representing multiple animals.

    Args:
        animals_data (List[Dict]): List of animal dictionaries.

    Returns:
        str: Combined HTML string of all animals as list items.
    """
    return ''.join(serialize_animal(animal) for animal in animals_data)


def read_html_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    Reads and returns the content of an HTML file.

    Args:
        file_path (str): Path to the HTML template file.

    Returns:
        str: Content of the file as a string.
    """
    with open(file_path, "r", encoding = encoding) as handle:
        return handle.read()


def get_skin_type_list(animals_data: List[Dict]) -> List[str]:
    """
    Extracts a unique list of skin types from the provided animal data.

    Args:
        animals_data (List[Dict]): List of animal dictionaries.

    Returns:
        List[str]: Unique list of lowercase skin types.
    """
    return list({
        animal['characteristics']['skin_type'].lower()
        for animal in animals_data
        if 'skin_type' in animal['characteristics']
    })


def filter_feature_animals_data(
    animals_data: List[Dict], feature: str, feature_kind: str
) -> List[Dict]:
    """
    Filters animal data by matching a specific characteristic feature.

    Args:
        animals_data (List[Dict]): List of animal dictionaries.
        feature (str): Key to filter by (e.g., 'skin_type').
        feature_kind (str): Desired feature value (e.g., 'fur').

    Returns:
        List[Dict]: List of filtered animal dictionaries.
    """
    return [
        animal
        for animal in animals_data
        if feature in animal['characteristics']
        and animal['characteristics'][feature].lower() == feature_kind.lower()
    ]


def main() -> None:
    """
    Main function to orchestrate the loading, filtering, and HTML generation
    for animal data.
    """
    # get API key from environment variable
    load_dotenv()
    api_key = os.getenv('API_KEY')

    # Fetch data based on user input
    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name, api_key)

    # Display available skin types
    skin_type_list = get_skin_type_list(animals_data)
    print("Available Skin Types:", skin_type_list)

    # Filter by skin type if the user provides a valid input
    user_choice_skin_type = input(
        "Please Enter skin_type to filter (if no or wrong, no filtering): "
    ).strip().lower()
    if user_choice_skin_type in skin_type_list:
        animals_data = filter_feature_animals_data(
            animals_data, "skin_type", user_choice_skin_type
        )
        print(f"Filtering animals with skin_type: {user_choice_skin_type}")
    else:
        print("No filtering applied or invalid skin type entered.")

    # Serialize data to HTML format
    string_animal_data = create_string_animal_data(animals_data)
    #if no animal data headline is created wit this statement
    if not string_animal_data:
        string_animal_data = (
            '<h2>The animal you searched for does not exist.</h2>'
        )

    # Load and populate HTML template
    html_template_string = read_html_file('animals_template.html')
    html_template_string = html_template_string.replace(
        '__REPLACE_ANIMALS_INFO__', string_animal_data
    )

    # Save the resulting HTML to an output file
    with open('animals.html', 'w') as outfile:
        outfile.write(html_template_string)

    print("Generated 'animals.html' successfully.")


if __name__ == '__main__':
    main()
