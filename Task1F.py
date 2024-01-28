from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()

print(inconsistent_typical_range_stations(stations))