from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius





def run():
    stations  = build_station_list()

    centre=(52.2053, 0.1218)
    r=10
    station_in=stations_within_radius(stations,centre,r)
    station_in_data=[]
    for station in station_in:
        station_in_data.append(station.name)

    print(station_in_data)
    
if __name__ == "__main__":
    run()