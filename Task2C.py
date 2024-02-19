from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    risk_stations = stations_highest_rel_level(stations,10)
    for i in range(len(risk_stations)):
        print(risk_stations[i])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()