from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
import random
from haversine import haversine, Unit
from floodsystem.geo import rivers_by_station_number


def test_station_by_distance():
    stations = build_station_list()

    coord=(random.uniform(51,53), random.uniform(-1, 1))
    x=stations_by_distance(stations,coord)
    for i in range(len(x) - 1):
        assert x[i][1] <= x[i+1][1]

def test_stations_within_radius():
    stations = build_station_list()

    centre=(random.uniform(51,53), random.uniform(-1, 1))
    r=random.uniform(5,15)
    x=stations_within_radius(stations,centre,r)
    for i in range(len(x) - 1):
        assert haversine(x[i].coord, centre)<=r
    
    y = [item for item in stations if item not in x]
    for i in range(len(y) - 1):
        assert haversine(y[i].coord, centre)>=r
        
def test_river_with_station():
    stations = build_station_list()

    x=sorted(rivers_with_station(stations))
    for element in stations:
        assert element.river in x
        
def test_stations_by_river():
    stations = build_station_list()
    x=stations_by_river(stations)
    for element in stations:
        assert element.name in x[element.river]
    
      
def test_rivers_by_station_number(): 
    stations = build_station_list()

    try:
        rivers_by_station_number(stations,N =9.0)
        rivers_by_station_number(stations,N ='9')

    except TypeError as e:
        assert str(e) == 'Please input a valid integer'

    else:
        assert False, 'Expected TypeError, but no exception was raised'


