'''
This module is used in handling map creation
'''
import progressbar
import folium

from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim


def find_coords(user_data: dict) -> dict:
    """
    Find each user location in coordinates and return the modified dict
    with each user coordinates
    """

    for i, user in enumerate(user_data):
        # Define the geolocator with project_name
        geolocator = Nominatim(user_agent="WF")

        location = geolocator.geocode(user['location'])

        if location != None:
            # print(i/len(movies) * 100, flush=True)
            user['location'] = (location.latitude, location.longitude)
        else:
            # Skip if there's any bad data
            user['location'] = None

    return user_data


def load_map(user_data: dict):
    """
    Loads the map with the friends locations.
    """
    mapp = folium.Map()

    loc_fg = folium.FeatureGroup(name="User Locations")
    marker_cluster = folium.plugins.MarkerCluster().add_to(loc_fg)


    for user in user_data:
        if user['location'] != None:
            popup = user['name']
            folium.Marker(location=user['location'], popup=popup).add_to(marker_cluster)

    mapp.add_child(loc_fg)
    mapp.add_child(folium.LayerControl())
    mapp.save("flaskr/templates/Friends.html")


if __name__ == '__main__':
    pass