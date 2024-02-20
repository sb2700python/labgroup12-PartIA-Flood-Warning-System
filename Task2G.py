from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels, fetch_measure_levels_safe
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit, predict_highest_water_level
from floodsystem.flood import stations_level_over_threshold

def run():
    
    # Get stations data with water level
    # Fetching all stations data will take very very long so we test for 100 of them
    stations=build_station_list()[:10]
    update_water_levels(stations)
    
    # Relative water level of 2.0 for severe
    severe=[]
    for element in stations_level_over_threshold(stations,2.0):
        severe.append (element[0])
        
    # Relative water level of 1.5-2.0 for high
    high=[]
    for element in stations_level_over_threshold(stations,1.5):
        high.append(element[0])
            
    #  1.0-1.5 for moderate
    moderate=[]
    for element in stations_level_over_threshold(stations,1.0):
        moderate.append(element[0])
            
    # Lower than 1.0 for low
    low=stations

    
    # Consider highest water level predicted by curve-fitting in the next 3 days
    dt1=10  
    dt2=3
    p=4
          
    for element in stations:
        dates, levels = fetch_measure_levels_safe(element.measure_id, dt=datetime.timedelta(days=dt1))
        
        # Check if dates is a list of datetime.date
        if all(isinstance(date, datetime.date) for date in dates):
        # Check if levels is a list of float
            if all(isinstance(level, float) for level in levels):
                if len(dates)==len(levels)!=0:
                    if hasattr(element, 'typical_range') and element.typical_range is not None:
                        h=predict_highest_water_level(dates,levels,p,dt2)
                        r=h/element.typical_range[1]
                        if (h > element.latest_level):
                            if r>2.0 and element not in severe:
                                severe.append(element.name)
            
                            if 1.5<r<2.0 and element not in high:
                                high.append(element.name)
                
                            if 1.0<r<2.0 and element not in moderate:
                                moderate.append(element.name)
                
    # Subtract higher risk form lower risk
    low=[element for element in low if element not in moderate and element not in high and element not in severe]
    moderate=[element for element in moderate if element not in high and element not in severe]
    high=[element for element in high if element not in severe]
    
    
    # Find towns at severe risk
    towns_at_severe_risk=[]
    for element in severe:
        for station in stations:
            if station.name==element and station.town not in towns_at_severe_risk:
                towns_at_severe_risk.append((station.town,station.latest_level/station.typical_range[1]))
                
    
    print("Towns at severe risk are:",towns_at_severe_risk)
    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
            
        
        
    
    
    
