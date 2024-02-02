# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""



from .utils import sorted_by_key
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    'Given a list of Monitoringstation class, return a list of turples of stations and distance, sorted by distance'
    station_and_distance = [0] * len(stations)
    i = 0
    for station in stations:
        station_and_distance[i] = (station, haversine(station.coord, p))
        i += 1
    return sorted_by_key(station_and_distance, 1)

def stations_within_radius(stations, centre, r):
    '''returns a list of stations within a given radius'''
    stations_distance=stations_by_distance(stations,centre)
    stations_in=[]
    for elements in stations_distance:
        if elements[1]<r:
            stations_in.append(elements[0])
    return stations_in

def rivers_with_station(stations):
    'Return the rivers with the given stations'
    rivers=set([])
    for station in stations:
        rivers.add(station.river)
    return rivers


def stations_by_river(stations):
    'Return a library with rivers as keys to stations'
    rivers={}
    for station in stations:
        if station.river not in rivers:
            rivers[station.river]=[station.name]
        elif station.river in rivers:
            rivers[station.river].append(station.name)
    return rivers

def rivers_by_station_number(stations,N):
    """ determines the N rivers with the greatest number of monitoring stations"""
    if type(N) != int:
        raise TypeError('Please input a valid integer')

    river_count = {}
    #count how many monitoring stations each river has
    for station in stations:
        if station.river not in river_count:
            river_count[station.river] = 1
        else:
            river_count[station.river] += 1
    
    #This turns the dict into a list of tuples, and sorts them by the number of stations but in reverse order

    sorted_rivers = sorted(river_count.items(), key=lambda x: x[1], reverse=True)

    Nth_entry = sorted_rivers[N-1][1] if N <= len(sorted_rivers) else 0

    result = [(river, count) for river, count in sorted_rivers if count >= Nth_entry]

    return result