from floodsystem.warning import flood_warning
from floodsystem.stationdata import build_station_list, update_water_levels
import random

def test_flood_warning():
    # Get stations data with water level and generate a random sample
    stations=build_station_list()
    update_water_levels(stations)
    random.shuffle(stations)
    stations_sample=stations[:10]
    
    # Testing
    try:
        flood_warning(stations_sample)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pass
    
    