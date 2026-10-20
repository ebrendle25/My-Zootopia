import json

DATA_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_file(file_path):
    """Read a text file and return its content as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(file_path, content):
    """Write content to a text file, replacing any existing content."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


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
        animal_info += f"Name: {name}<br/>\n"
    if diet:
        animal_info += f"Diet: {diet}<br/>\n"
    if first_location:
        animal_info += f"Location: {first_location}<br/>\n"
    if animal_type:
        animal_info += f"Type: {animal_type}<br/>\n"
    animal_info += "<br/>\n"
    return animal_info


def main():
    """Fill the HTML template with the animal data and save the result."""
    animals_data = load_json(DATA_FILE)
    html_template = read_file(TEMPLATE_FILE)

    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)

    html_page = html_template.replace(PLACEHOLDER, animals_info)
    write_file(OUTPUT_FILE, html_page)


if __name__ == "__main__":
    main()