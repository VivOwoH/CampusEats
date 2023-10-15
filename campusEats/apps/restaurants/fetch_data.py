import requests
import json
# from models import *
import re


# Step 1: Fetch data from Google Maps API and store in JSON
def fetch_google_maps_data(api_key):
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": "-33.886930,151.209439",  # Replace with the coordinates of USYD
        "radius": 1000,  # 1km radius
        "type": "cafe",
        "key": 'AIzaSyAxBAGRJmEsJw6gQDwFeoWSRKzjIecNyVA',
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    with open("restaurant_data.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
    return data
# Function to extract URL from HTML attribution
def extract_url_from_html(html):
    match = re.search(r'href="(.*?)"', html)
    if match:
        return match.group(1)
    return ""
# Step 2: Create a JSON fixture file in the desired format
def create_fixture(data):
    results = data.get("results", [])
    fixture_data = []

    for index, place in enumerate(results, start=1):
        name = place["name"]
        location = place.get("vicinity", "")
        description = ", ".join(place.get("types", []))

        # Extract the URL from the first HTML attribution
        # html_attributions = place.get("photos", [{}])[0].get("html_attributions", [])
        # image_url = extract_url_from_html(html_attributions[0]) if html_attributions else ""

        photo_reference = place.get("photos", [{}])[0].get("photo_reference", "")
        if photo_reference:
            # Construct the image URL
            image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
        else:
            image_url = ""

        rating = place.get("rating", None)

        fixture_item = {
            "model": "restaurants.Restaurant",
            "pk": index,
            "fields": {
                "Name": name,
                "Location": location,
                "Description": description,
                "ImageURL": image_url,
                "Rating": rating
            }
        }
        fixture_data.append(fixture_item)

    # Write the fixture data to a JSON file
    with open("fixtures/restaurants.json", "w") as fixture_file:
        json.dump(fixture_data, fixture_file, indent=2)


# # Step 2: Populate Django model from JSON
# def populate_model_from_json():
#     with open("restaurant_data.json", "r") as json_file:
#         data = json.load(json_file)

#     for place in data.get("results", []):
#         name = place["name"]
#         location = place.get("vicinity", "")
#         description = ", ".join(place.get("types", []))
#         image_url = place.get("photos", [{}])[0].get("photo_reference", "")
#         rating = place.get("rating", None)

#         # Create a new Restaurant object and save it
#         restaurant = Restaurant(Name=name, Location=location, Description=description, ImageURL=image_url, Rating=rating)
#         restaurant.save()


if __name__ == "__main__":
    api_key = "AIzaSyAxBAGRJmEsJw6gQDwFeoWSRKzjIecNyVA"

    # Perform both steps
    data = fetch_google_maps_data(api_key)
    # populate_model_from_json()
    results = data.get("results", [])

# Create a JSON fixture file in the desired format
    create_fixture(data)
    # Iterate through the results and access individual entries
    for place in results:
        name = place["name"]
        location = place.get("vicinity", "")
        description = ", ".join(place.get("types", []))
        # image_url = place.get("photos", [{}])[0].get("photo_reference", "")
        # image_url = place.get("photos", [{}])[0].get("html_attributions", [])
        # Extract the ImageURL from html_attributions
        # Extract the URL from the first HTML attribution
        # html_attributions = place.get("photos", [{}])[0].get("html_attributions", [])
        # image_url = extract_url_from_html(html_attributions[0]) if html_attributions else ""
        # Extract the Image URL
        photo_reference = place.get("photos", [{}])[0].get("photo_reference", "")
        if photo_reference:
            # Construct the image URL
            image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
        else:
            image_url = ""



        # Use the retrieved data as needed
        print(f"Name: {name}, Location: {location}, Description: {description}, Image URL: {image_url}")
        
        break

# // python manage.py loaddata apps/restaurants/fixtures/restaurants.json