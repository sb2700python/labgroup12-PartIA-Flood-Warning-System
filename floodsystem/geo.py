# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""



from .utils import sorted_by_key
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    station_and_distance = [0] * len(stations)
    i = 0
    for station in stations:
        station_and_distance[i] = (station, haversine(station.coord, p))
        i += 1
    return sorted_by_key(station_and_distance, 1)

def stations_within_radius(stations, centre, r):
    stations_distance=stations_by_distance(stations,centre)
    stations_in=[]
    for elements in stations_distance:
        if elements[1]<r:
            stations_in.append(elements[0])
    return stations_in

def rivers_with_station(stations):
    rivers=set([])
    for station in stations:
        rivers.add(station.river)
    return rivers


def stations_by_river(stations):
    rivers={}
    for station in stations:
        if station.river not in rivers:
            rivers[station.river]=[station.name]
        elif station.river in rivers:
            rivers[station.river].append(station.name)
    return rivers