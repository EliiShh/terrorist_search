import folium
import os


def search_in_all_to_map(avgs:list):
    list_avgs = [event['_source'] for event in avgs]
    initial_location = [list_avgs[0]["latitude"], list_avgs[0]["longitude"]]
    map = folium.Map(location=initial_location)

    for i in list_avgs:
        cords = (i["latitude"], i["longitude"])
        folium.Marker(cords,
                      popup=f'date: {i["date"]}, summary:, '
                            f'{i["summary"]}').add_to(map)

    function_dir = os.path.dirname(__file__)
    map.save(f'{function_dir}\map.html')

