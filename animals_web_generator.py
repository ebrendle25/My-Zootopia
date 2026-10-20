"""
Generate an HTML page with information about animals.

Reads the animal data from animals_data.json, fills it into the
placeholder of animals_template.html and saves the result as animals.html.
"""

import json

DATA_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_json(file_path):
    """Load a JSON file and return its content, or None if that fails."""
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: {file_path} does not contain valid JSON.")
    except OSError as error:
        print(f"Error: could not read {file_path}: {error}")
    return None


def read_file(file_path):
    """Read a text file and return its content as a string, or None if that fails."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as error:
        print(f"Error: could not read {file_path}: {error}")
    return None


def write_file(file_path, content):
    """Write content to a text file, replacing any existing content.

    Returns True if the file was written, False if writing failed.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except OSError as error:
        print(f"Error: could not write {file_path}: {error}")
        return False
    return True


def serialize_animal(animal):
    """Return the name, diet, first location and type of an animal as text.

    Fields that are missing in the data are left out.
    """
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    name = animal.get("name")
    diet = characteristics.get("diet")
    first_location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    animal_info = '<li class="cards__item">'
    if name:
        animal_info += f'<div class="card__title">{name}</div>'
    animal_info += '<div class="card__text">'
    animal_info += '<ul>'
    if diet:
        animal_info += f'<li><strong>Diet:</strong> {diet}</li>'
    if first_location:
        animal_info += f'<li><strong>Location:</strong> {first_location}</li>'
    if animal_type:
        animal_info += f'<li><strong>Type:</strong> {animal_type}</li>'
    animal_info += "</ul>"
    animal_info += "</div>"
    animal_info += "</li>"
    return animal_info


def main():
    """Fill the HTML template with the animal data and save the result."""
    animals_data = load_json(DATA_FILE)
    if animals_data is None:
        return
    html_template = read_file(TEMPLATE_FILE)
    if html_template is None:
        return
    if animals_data is None or html_template is None:
        return

    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)

    html_page = html_template.replace(PLACEHOLDER, animals_info)
    if write_file(OUTPUT_FILE, html_page):
        print(f"Website was successfully generated to the file {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
