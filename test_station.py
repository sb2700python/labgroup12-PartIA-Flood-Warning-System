# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    station1 = MonitoringStation(station_id='1', measure_id='1', label='Station1', coord=(1.23, 4.56), typical_range=(100, 10), river='x', town='y')
    assert station1.typical_range_consistent() is False
    station2 = MonitoringStation(station_id='2', measure_id='2', label='Station2', coord=(1.23, 4.56), typical_range=None, river='x', town='y')
    assert station2.typical_range_consistent() is False
    station3 = MonitoringStation(station_id='3', measure_id='3', label='Station3', coord=(1.23, 4.56), typical_range=(10, 100), river='x', town='y')
    assert station3.typical_range_consistent() is True


def test_inconsistent_typical_range_stations():
    station1 = MonitoringStation(station_id='1', measure_id='1', label='Station1', coord=(1.23, 4.56), typical_range=(100, 10), river='x', town='y')
    stations = [station1]
    result1 = inconsistent_typical_range_stations(stations)
    assert result1 == ['Station1']

    station2 = MonitoringStation(station_id='2', measure_id='2', label='Station2', coord=(1.23, 4.56), typical_range=None, river='x', town='y')
    stations = [station2]
    result2 = inconsistent_typical_range_stations(stations)
    assert result2 == ['Station2']

    station3 = MonitoringStation(station_id='3', measure_id='3', label='Station3', coord=(1.23, 4.56), typical_range=(10, 100), river='x', town='y')
    stations = [station3]
    result3 = inconsistent_typical_range_stations(stations)
    assert result3 == []

