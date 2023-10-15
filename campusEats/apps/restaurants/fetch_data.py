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
        "fields": "name,rating,formatted_phone_number,opening_hours,price_level,takeout,dine_in,delivery,reservable,serves_vegetarian_food,serves_wine,serves_beer",
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
        "key": api_key,
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

        rating = place.get("rating", False)

        is_open = details.get("opening_hours", {}).get("open_now")
            
        # Check if opening hours are available
        opening_hours = details.get("opening_hours", {}).get("weekday_text", [])
        
        if opening_hours:
            open_dates = "\n".join(opening_hours)
        else:
            open_dates = "Opening hours not available."

            
        # is_open = place.get("opening_hours", {}).get("open_now", False)
        # open_dates = place.get("open_dates", [])

        phone = place.get("formatted_phone_number", "")
        price_level = place.get("price_level", None)
        # New fields
        takeout = place.get("takeout", None)  # Use None for unknown values
        dine_in = place.get("dine_in", None)  # Use None for unknown values
        delivery = place.get("delivery", None)  # Use None for unknown values
        reservable = place.get("reservable", None)  # Use None for unknown values
        serves_vegetarian_food = place.get("serves_vegetarian_food", None)  # Use None for unknown values
        serves_wine = place.get("serves_wine", None)  # Use None for unknown values
        serves_beer = place.get("serves_beer", None)  

        # Convert None values to False if they remain None
        # price_level = False if price_level is None else price_level
        takeout = False if takeout is None else takeout
        dine_in = False if dine_in is None else dine_in
        delivery = False if delivery is None else delivery
        reservable = False if reservable is None else reservable
        serves_vegetarian_food = False if serves_vegetarian_food is None else serves_vegetarian_food
        serves_wine = False if serves_wine is None else serves_wine
        serves_beer = False if serves_beer is None else serves_beer


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
                "Phone": phone,
                "PriceLevel": price_level,
                "Takeout": takeout,
                "Dine_in": dine_in,
                "Delivery": delivery,
                "Reservable": reservable,
                "Serves_vegetarian_food": serves_vegetarian_food,
                "Serves_wine": serves_wine,
                "Serves_beer": serves_beer,
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
            # print(details)
            # break
            if details:
                # Extract the last three fields
                # print(details)
                # break
                formatted_phone_number = details.get("formatted_phone_number", "")
                is_open = details.get("opening_hours", {}).get("open_now")
            
                # Check if opening hours are available
                opening_hours = details.get("opening_hours", {}).get("weekday_text", [])
                
                if opening_hours:
                    open_dates = "\n".join(opening_hours)
                else:
                    open_dates = "Opening hours not available."

                # Extract additional fields
                price_level = details.get("price_level")
                                # Extract additional fields
                # price_level = details.get("price_level")
                takeout = details.get("takeout")
                dine_in = details.get("dine_in")
                delivery = details.get("delivery")
                reservable = details.get("reservable")
                serves_vegetarian_food = details.get("serves_vegetarian_food")
                serves_wine = details.get("serves_wine")
                serves_beer = details.get("serves_beer")


                # Append the new fields to the existing data
                place["formatted_phone_number"] = formatted_phone_number
                place["is_open"] = is_open
                # place["open_dates"] = opening_hours
                place["price_level"] = price_level if price_level is not None else None
                place["takeout"] = takeout
                place["dine_in"] = dine_in
                place["delivery"] = delivery
                place["reservable"] = reservable
                place["serves_vegetarian_food"] = serves_vegetarian_food
                place["serves_wine"] = serves_wine
                place["serves_beer"] = serves_beer
                place["open_dates"] = open_dates
                # print(f"Name: {place['is_open']}, hours: {place['open_dates']}")


            restaurant_details.append(place)
            # print(restaurant_details)
            # break

    # Write the restaurant details to a new JSON fixture file
    with open("restaurant_details_fixture.json", "w") as details_file:
        json.dump(restaurant_details, details_file, indent=2)
    input_file = "restaurant_details_fixture.json"
    output_file = "fixtures/restaurants.json"

    create_fixture(input_file, output_file, api_key)
    print(len(restaurant_details))




# // python manage.py loaddata apps/restaurants/fixtures/restaurants.json
# https://developers.google.com/maps/documentation/places/web-service/search-nearby#maps_http_places_nearbysearch-txt