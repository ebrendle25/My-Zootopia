import json

def load_data(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    name = animal.get("name")
    diet = characteristics.get("diet")
    location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if location:
        print(f"Location: {location}")
    if animal_type:
        print(f"Type: {animal_type}")
    print()
