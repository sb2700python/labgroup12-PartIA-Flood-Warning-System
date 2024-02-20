from .station import call_relative_water_level
from .station import call_typical_range_consistent
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels, fetch_measure_levels_safe
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit, predict_highest_water_level
from floodsystem.flood import stations_level_over_threshold

def stations_level_over_threshold(stations, tol):

    valid_stations = []
    for station in stations:
        if call_typical_range_consistent(station) is True:
            valid_stations.append(station)

    risk_stations = []

    for station in valid_stations:
        level = call_relative_water_level(station)
        if level != None:
            if level > tol:
                risk_stations.append((station.name, level))

    
    sorted_risk_stations = sorted(risk_stations, key=lambda x: x[1], reverse=True)

    return sorted_risk_stations
    
def stations_highest_rel_level(stations,N):

    valid_stations = []
    for station in stations:
        if call_typical_range_consistent(station) is True:
            valid_stations.append(station)

    risk_stations = []

    for station in valid_stations:
        level = call_relative_water_level(station)
        if level != None:
            risk_stations.append((station.name, level))

    sorted_risk_stations = sorted(risk_stations, key=lambda x: x[1], reverse=True)

    most_at_risk = sorted_risk_stations[:N]
    
    return most_at_risk

    

    


    
