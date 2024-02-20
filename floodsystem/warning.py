from .station import call_relative_water_level
from .station import call_typical_range_consistent
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels, fetch_measure_levels_safe
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit, predict_highest_water_level



def flood_warning(stations,dt1=10, dt2=3, p=4):
    # Consider highest water level predicted by curve-fitting of degree p in the next dt2 days based on past dt1 days

    towns={}
    # Relative water level >2.0 for severe
    severe=set()
    # 1.5-2.0 for high
    high=set()
    # 1.0-1.5 for moderate
    moderate=set()
    # <1.0 for low
    low=set()
    

          
    for element in stations:
        
        # Safe fetch to avoid value error caused by corrupted data, return two empty lists which would be passed later
        dates, levels = fetch_measure_levels_safe(element.measure_id, dt=datetime.timedelta(days=dt1))
        
        # Check if dates is a list of datetime.date
        if all(isinstance(date, datetime.date) for date in dates):
        # Check if levels is a list of float
            if all(isinstance(level, float) for level in levels):
                # Check level and dates have equal length and are not empty, also pass stations with corrupted dates and/or level data
                if len(dates)==len(levels)!=0:
                    # Check the station has typical range and latest level
                    if hasattr(element, 'typical_range') and element.typical_range is not None and hasattr(element, 'latest_level') and element.latest_level is not None:                      
                        # predict the highest relative water level in next dt2 days
                        predicted_relative_level=predict_highest_water_level(dates,levels,p,dt2)/element.typical_range[1]
                        latest_relative_level=element.latest_level/element.typical_range[1]
                        # Use the higher one of current level and predicted level to access the risk
                        risk_key=max(predicted_relative_level,latest_relative_level)
                        if predicted_relative_level>latest_relative_level:
                            status="predicted"
                        else:
                            status="current"
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
                        
                        # Check the station has town, and generate a dict where the towns are keys to risk_key, risk and status
                        if hasattr(element, 'town') and element.town is not None and element.town not in towns:
                            towns[element.town]=(risk_key,risk,status)
                        elif risk_key>towns[element.town][0]:
                            towns[element.town]=(risk_key,risk,status)
    
    # Sort the dict based on risk_key, in descending order                    
    sorted_towns = dict(sorted(towns.items(), key=lambda x: x[1][0], reverse=True))
    
    return sorted_towns, severe, high, moderate, low