from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()


#rivers_by_station_number(stations, 9)

result = rivers_by_station_number(stations, N=9)
print(result)