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
