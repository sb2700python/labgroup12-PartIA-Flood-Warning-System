# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None #new attribute

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        d += "   latest level:  {}".format(self.latest_level)
        return d

    def typical_range_consistent(self):
        '''Inconsistent if high<low or if range doesn't exist'''
        if self.typical_range is None:
            return False
        
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        
        else:
            return True
        
    def relative_water_level(self):
        if self.typical_range_consistent() == False or self.latest_level == None:
            return None
        else:
            range_low = self.typical_range[0]
            range_high = self.typical_range[1]
            ratio = (self.latest_level - range_low)/(range_high - range_low)
            return ratio
    

def inconsistent_typical_range_stations(stations):
    '''if the typical range is not consistent, the name of the station is added to a list 
    which is then sorted alphabetically'''
    inconsistent_stations = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == True:
            pass
        else:
            inconsistent_stations.append(station.name)
    

    return sorted(inconsistent_stations)

def call_relative_water_level(station):
    return station.relative_water_level()

def call_typical_range_consistent(station):
    return station.typical_range_consistent()

            