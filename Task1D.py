from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river




def run():
    stations = build_station_list()

    rivers1=sorted(rivers_with_station(stations))
    print(len(rivers1),"stations, first 10:",rivers1[:10])

    rivers2=stations_by_river(stations)
    print(sorted(rivers2["River Aire"]))
    print(sorted(rivers2["River Cam"]))
    print(sorted(rivers2["River Thames"]))
    
if __name__ == "__main__":
    run()