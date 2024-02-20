from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels, fetch_measure_levels_safe
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit, predict_highest_water_level
from floodsystem.warning import flood_warning

def run():
    
    # Get stations data with water level
    # Fetching all 2200+ stations data will take very very long so we test for 100 of them
    stations=build_station_list()[:100]
    update_water_levels(stations)

    # Produce warning for towns based on stations
    sorted_towns, severe, high, moderate, low=flood_warning(stations)
    
    n=10
    top_n_risk_towns = dict(list(sorted_towns.items())[:n])
    print(top_n_risk_towns)
    print(severe)                        
                        
                        
                            


    
    

    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
            
        
        
    
    
    
