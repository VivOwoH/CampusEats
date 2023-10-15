import requests
import json
# from models import *
import re

def fetch_place_details(api_key, place_id):
    # endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    # params = {
    #     "fields": "name,rating,formatted_phone_number",
    #     "place_id": place_id,
    #     "key": api_key,
    # }

    endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "fields": "name,rating,formatted_phone_number,address_components,opening_hours",
        "place_id": place_id,
        "key": api_key,
    }


    response = requests.get(endpoint, params=params)
    data = response.json()
    
    return data.get("result", {})  # Extract the result object


# Step 1: Fetch data from Google Maps API and store in JSON
def fetch_google_maps_data(api_key):
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": "-33.886930,151.209439",  # Replace with the coordinates of USYD
        "radius": 1000,  # 1km radius
        "type": "restaurant",
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
def create_fixture(input_file, output_file, api_key):
    with open(input_file, "r") as json_file:
        data = json.load(json_file)

    results = data  # Assuming data is a list of restaurants

    fixture_data = []

    for index, place in enumerate(results, start=1):
        name = place.get("name", "")
        location = place.get("vicinity", "")
        description = ", ".join(place.get("types", []))

        photo_reference = place.get("photos", [{}])[0].get("photo_reference", "")
        if photo_reference:
            image_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
        else:
            image_url = ""

        rating = place.get("rating", None)
        is_open = place.get("opening_hours", {}).get("open_now", False)
        open_dates = place.get("open_dates", [])

        phone = place.get("formatted_phone_number", "")

        fixture_item = {
            "model": "restaurants.Restaurant",
            "pk": index,
            "fields": {
                "Name": name,
                "Location": location,
                "Description": description,
                "ImageURL": image_url,
                "Rating": rating,
                "Is_open": is_open,
                "Open_dates": open_dates,
                "Phone": phone
            }
        }

        fixture_data.append(fixture_item)

    # Write the fixture data to a JSON file
    with open(output_file, "w") as fixture_file:
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
    # create_fixture(data)
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

    with open("restaurant_data.json", "r") as json_file:
        data = json.load(json_file)

    restaurant_details = []

    # for place in data.get("results", []):
    #     place_id = place.get("place_id")
    #     if place_id:
    #         details = fetch_place_details(api_key, place_id)
    #         restaurant_details.append(details)

    # # Write the restaurant details to a new JSON file
    # with open("restaurant_details.json", "w") as details_file:
    #     json.dump(restaurant_details, details_file, indent=2)

    for place in data.get("results", []):
        place_id = place.get("place_id")
        if place_id:
            details = fetch_place_details(api_key, place_id)
            if details:
                # Extract the last three fields
                formatted_phone_number = details.get("formatted_phone_number", "")
                is_open = details.get("opening_hours", {}).get("open_now", False)
                open_dates = details.get("opening_hours", {}).get("weekday_text", [])

                # Append the last three fields to the existing data
                place["formatted_phone_number"] = formatted_phone_number
                place["is_open"] = is_open
                place["open_dates"] = open_dates

            restaurant_details.append(place)

    # Write the restaurant details to a new JSON fixture file
    with open("restaurant_details_fixture.json", "w") as details_file:
        json.dump(restaurant_details, details_file, indent=2)
    input_file = "restaurant_details_fixture.json"
    output_file = "fixtures/restaurants.json"

    create_fixture(input_file, output_file, api_key)




# // python manage.py loaddata apps/restaurants/fixtures/restaurants.json
# https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt