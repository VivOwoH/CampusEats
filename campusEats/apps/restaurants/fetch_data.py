import requests
import json
from restaurants.models import Restaurant

# Step 1: Fetch data from Google Maps API and store in JSON
def fetch_google_maps_data(api_key):
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": "-33.886930,151.209439",  # Replace with the coordinates of USYD
        "radius": 5000,  # 5km radius
        "type": "restaurant",
        "key": api_key,
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    with open("restaurant_data.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

# Step 2: Populate Django model from JSON
def populate_model_from_json():
    with open("restaurant_data.json", "r") as json_file:
        data = json.load(json_file)

    for place in data.get("results", []):
        name = place["name"]
        location = place.get("vicinity", "")
        description = ", ".join(place.get("types", []))
        image_url = place.get("photos", [{}])[0].get("photo_reference", "")
        rating = place.get("rating", None)

        # Create a new Restaurant object and save it
        restaurant = Restaurant(Name=name, Location=location, Description=description, ImageURL=image_url, Rating=rating)
        restaurant.save()

if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"

    # Perform both steps
    fetch_google_maps_data(api_key)
    populate_model_from_json()
# // python manage.py loaddata apps/restaurants/fixtures/restaurants.json