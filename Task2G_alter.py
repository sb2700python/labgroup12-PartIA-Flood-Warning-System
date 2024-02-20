from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels, fetch_measure_levels_safe
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit, predict_highest_water_level
from floodsystem.flood import stations_level_over_threshold

def run():
    
    # Get stations data with water level
    # Fetching all 2200+ stations data will take very very long so we test for 100 of them
    stations=build_station_list()[:100]
    update_water_levels(stations)

    
    # Consider highest water level predicted by curve-fitting in the next 3 days
    dt1=10  
    dt2=3
    p=4
    towns={}
    severe=set()
    high=set()
    moderate=set()
    low=set()
    

          
    for element in stations:
        dates, levels = fetch_measure_levels_safe(element.measure_id, dt=datetime.timedelta(days=dt1))
        
        # Check if dates is a list of datetime.date
        if all(isinstance(date, datetime.date) for date in dates):
        # Check if levels is a list of float
            if all(isinstance(level, float) for level in levels):
                if len(dates)==len(levels)!=0:
                    if hasattr(element, 'typical_range') and element.typical_range is not None and hasattr(element, 'latest_level') and element.latest_level is not None:                      
                        predicted_relative_level=predict_highest_water_level(dates,levels,p,dt2)/element.typical_range[1]
                        latest_relative_level=element.latest_level/element.typical_range[1]
                        risk_key=max(predicted_relative_level,latest_relative_level)
                        if risk_key>=2.0:
                            risk="severe"
                            severe.add(element.name)
                        elif 1.5<risk_key<2.0:
                            risk="high"
                            high.add(element.name)
                        elif 1.0<risk_key<=1.5:
                            risk="moderate"
                            moderate.add(element.name)
                        else:
                            risk="low"
                            low.add(element.name)
                        
                        if element.town not in towns:
                            towns[element.town]=(risk_key,risk)
                        elif risk_key>towns[element.town][0]:
                            towns[element.town]=(risk_key,risk)
                        
    sorted_towns = dict(sorted(towns.items(), key=lambda x: x[1][0], reverse=True))
    top_10_risk_towns = dict(list(sorted_towns.items())[:10])
    print(top_10_risk_towns)
    print(severe)                        
                        
                        
                            


    
    

    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
            
        
        
    
    
    
